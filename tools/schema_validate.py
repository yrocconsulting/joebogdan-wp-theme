"""Validate JSON-LD on pages against the schema.org vocabulary.

    python3 tools/schema_validate.py schemaorg-current-https.jsonld URL [URL ...]
    python3 tools/schema_validate.py schemaorg-current-https.jsonld --file urls.txt

Checks that every @type exists and every property is defined for that type
(or one of its parent types). Download the vocabulary from
https://schema.org/version/latest/schemaorg-current-https.jsonld
"""
import json
import re
import sys
import urllib.request


def load_vocab(path):
    graph = json.load(open(path))["@graph"]
    parents, props = {}, {}
    as_list = lambda v: v if isinstance(v, list) else [v]
    for node in graph:
        nid = node["@id"].replace("schema:", "")
        types = as_list(node["@type"])
        if "rdfs:Class" in types:
            parents[nid] = [p["@id"].replace("schema:", "") for p in as_list(node.get("rdfs:subClassOf", [])) if p]
        if "rdf:Property" in types:
            props[nid] = {d["@id"].replace("schema:", "") for d in as_list(node.get("schema:domainIncludes", [])) if d}
    return parents, props


def ancestors(t, parents, seen=None):
    seen = seen or set()
    if t in seen:
        return seen
    seen.add(t)
    for p in parents.get(t, []):
        ancestors(p, parents, seen)
    return seen


def check(node, parents, props, path, errors):
    if isinstance(node, list):
        for i, n in enumerate(node):
            check(n, parents, props, f"{path}[{i}]", errors)
        return
    if not isinstance(node, dict):
        return
    types = node.get("@type")
    types = types if isinstance(types, list) else ([types] if types else [])
    lineage = set()
    for t in types:
        if t not in parents:
            errors.append(f"{path}: unknown type {t}")
        lineage |= ancestors(t, parents)
    for key, val in node.items():
        if key.startswith("@"):
            continue
        if types:
            if key not in props:
                errors.append(f"{path}: unknown property {key}")
            elif not props[key] & lineage:
                errors.append(f"{path}: {key} not valid on {'/'.join(types)}")
        check(val, parents, props, f"{path}.{key}", errors)


def main():
    vocab, *rest = sys.argv[1:]
    urls = open(rest[1]).read().split() if rest[:1] == ["--file"] else rest
    parents, props = load_vocab(vocab)
    total = 0
    for url in urls:
        html = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "schema-check"}), timeout=30).read().decode()
        errors = []
        for raw in re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S):
            data = json.loads(raw)
            for i, node in enumerate(data.get("@graph", [data])):
                check(node, parents, props, f"#{i}:{node.get('@type')}", errors)
        total += len(errors)
        print(f"{'OK ' if not errors else 'ERR'} {url}")
        for e in errors:
            print("    " + e)
    print(f"{len(urls)} URLs, {total} schema errors")


if __name__ == "__main__":
    main()
