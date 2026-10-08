"""SEO + structured-data audit.

    python3 tools/seo_audit.py URL [URL ...]      or      python3 tools/seo_audit.py --file urls.txt

Checks title, meta description, canonical, robots, Open Graph, H1/heading
order, image alt text and the JSON-LD graph on each URL.
"""
import json
import re
import sys
import urllib.request
from html.parser import HTMLParser

UA = "Mozilla/5.0 (SEO audit) Chrome/128"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta = {}
        self.links = []
        self.headings = []
        self.imgs = []
        self.ld = []
        self._in = None
        self._buf = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self._in, self._buf = "title", ""
        elif tag == "meta":
            key = a.get("name") or a.get("property")
            if key:
                self.meta[key] = a.get("content", "")
        elif tag == "link":
            self.links.append(a)
        elif tag in ("h1", "h2", "h3", "h4"):
            self._in, self._buf = tag, ""
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "script" and a.get("type") == "application/ld+json":
            self._in, self._buf = "ld", ""

    def handle_endtag(self, tag):
        if self._in == "title" and tag == "title":
            self.title = self._buf.strip()
            self._in = None
        elif self._in == tag and tag in ("h1", "h2", "h3", "h4"):
            self.headings.append((tag, re.sub(r"\s+", " ", self._buf).strip()))
            self._in = None
        elif self._in == "ld" and tag == "script":
            self.ld.append(self._buf)
            self._in = None

    def handle_data(self, data):
        if self._in:
            self._buf += data


def types(node):
    t = node.get("@type")
    return t if isinstance(t, list) else [t]


def audit(url):
    html = urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=30).read().decode("utf-8", "replace")
    pg = Page()
    pg.feed(html)
    issues, info = [], []

    t = pg.title
    if not t:
        issues.append("missing <title>")
    elif not 30 <= len(t) <= 65:
        issues.append(f"title length {len(t)} (aim 30-65): {t}")
    d = pg.meta.get("description", "")
    if not d:
        issues.append("missing meta description")
    elif not 110 <= len(d) <= 165:
        issues.append(f"description length {len(d)} (aim 110-165)")
    canon = [l.get("href") for l in pg.links if l.get("rel") == "canonical"]
    if len(canon) != 1:
        issues.append(f"canonical tags: {len(canon)}")
    elif canon[0].rstrip("/") != url.rstrip("/"):
        issues.append(f"canonical mismatch: {canon[0]}")
    for og in ("og:title", "og:description", "og:url", "og:image", "og:type"):
        if not pg.meta.get(og):
            issues.append(f"missing {og}")
    robots = pg.meta.get("robots", "")
    if "noindex" in robots:
        info.append(f"robots: {robots}")

    h1s = [h for h in pg.headings if h[0] == "h1"]
    if len(h1s) != 1:
        issues.append(f"H1 count {len(h1s)}")
    last = 1
    for tag, text in pg.headings:
        level = int(tag[1])
        if level > last + 1:
            issues.append(f"heading jumps h{last}→{tag}: {text[:50]}")
        last = level
    for img in pg.imgs:
        if "alt" not in img:
            issues.append(f"img without alt: {img.get('src', '')[-50:]}")

    graph = []
    for raw in pg.ld:
        try:
            data = json.loads(raw)
        except ValueError as e:
            issues.append(f"invalid JSON-LD: {e}")
            continue
        graph += data.get("@graph", [data])
    ids = {n.get("@id") for n in graph if n.get("@id")}
    for n in graph:
        for key, val in n.items():
            refs = val if isinstance(val, list) else [val]
            for r in refs:
                if isinstance(r, dict) and set(r) == {"@id"} and r["@id"] not in ids:
                    issues.append(f"schema: {types(n)[0]}.{key} → unresolved {r['@id']}")
    found = sorted({t for n in graph for t in types(n)})
    return t, d, found, issues, info


def main():
    args = sys.argv[1:]
    urls = open(args[1]).read().split() if args[:1] == ["--file"] else args
    total = 0
    for url in urls:
        try:
            title, desc, found, issues, info = audit(url)
        except Exception as e:  # noqa: BLE001
            print(f"\n{url}\n  ERROR {e}")
            total += 1
            continue
        total += len(issues)
        print(f"\n{url}\n  schema: {', '.join(found)}")
        for i in info:
            print(f"  · {i}")
        for i in issues:
            print(f"  ✗ {i}")
    print(f"\n{len(urls)} URLs, {total} issues")


if __name__ == "__main__":
    main()
