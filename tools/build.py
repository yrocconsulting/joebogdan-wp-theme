"""Regenerate content/ from tools/pages.py.

    python3 tools/build.py
"""
import json
import pathlib
import re

import pages
import posts

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "content"


# Phrases daily posts may not contain (Regulation Z triggering terms, guarantees,
# the unaffiliated competitor domain, em dashes). Fix the copy; never loosen these.
BANNED = [
    (r"\d(\.\d+)?\s?%\s*(apr|interest|fixed|adjustable|rate|down)", "interest rate, APR or down-payment percentage"),
    (r"\b(rates?|apr|yield)\b[^.<]{0,30}?\b\d+(\.\d+)?\s?%", "a specific rate or APR"),
    (r"\b(30|15|20|10)-year\b[^.<]{0,40}?\b\d+(\.\d+)?\s?%", "a specific mortgage rate"),
    (r"\$\s?[\d,.]+\s*(k\b|thousand)?\s*(down|per month|a month|/mo|monthly)", "a payment or down-payment amount"),
    (r"\b(no|zero|0%?|nothing)[ -]down\b", "a down-payment claim"),
    (r"\b(down payment|payment)s?\s+(of|as low as|starting at|from)\s+\$?\d", "a down-payment or payment amount"),
    (r"\bguarantee(d|s)?\b", "a guarantee"),
    (r"\b(lowest|best) (rates?|price|fees)\b", "a superlative pricing claim"),
    (r"\bpre-?approved in\b", "a speed promise"),
    (r"joebogdan\.com", "the unaffiliated competitor site"),
    (r"\u2014", "an em dash"),
]


def compliance_issues(text):
    plain = re.sub(r"<[^>]+>", " ", text)
    plain = re.sub(r"<!--.*?-->", " ", plain)
    found = []
    for pattern, why in BANNED:
        m = re.search(pattern, plain, re.I)
        if m:
            found.append(f"{why}: \"{m.group(0)}\"")
    return found


def main():
    (OUT / "pages").mkdir(parents=True, exist_ok=True)
    manifest = {"pages": [], "menus": {}, "categories": [], "front_page": "home", "posts_page": "insights"}
    for slug, title, parent, template, body, seo_title, seo_desc, service, order, excerpt in pages.PAGES:
        (OUT / "pages" / f"{slug}.html").write_text(body, encoding="utf-8")
        manifest["pages"].append({
            "slug": slug, "title": title, "parent": parent, "template": template or "",
            "file": f"pages/{slug}.html", "seo_title": seo_title or "", "seo_description": seo_desc or "",
            "service": service or "", "audience": pages.AUDIENCE.get(slug, ""), "old_slugs": pages.OLD_SLUGS.get(slug, []), "menu_order": order, "excerpt": excerpt or "",
        })
    for location, items in pages.MENUS.items():
        manifest["menus"][location] = [
            {"title": t, "page": s, "children": [{"title": ct, "page": cs} for ct, cs in kids]}
            for t, s, kids in items
        ]
    (OUT / "posts").mkdir(parents=True, exist_ok=True)
    manifest["posts"] = []
    for post in posts.POSTS:
        (OUT / "posts" / f"{post['slug']}.html").write_text(post["content"], encoding="utf-8")
        entry = {k: v for k, v in post.items() if k != "content"}
        entry["file"] = f"posts/{post['slug']}.html"
        manifest["posts"].append(entry)
    manifest["categories"] = [{"slug": s, "name": n, "description": d} for s, n, d in pages.CATEGORIES]
    problems = []
    for item in manifest["pages"] + manifest["posts"]:
        if not 30 <= len(item["seo_title"]) <= 65:
            problems.append(f"title {len(item['seo_title'])}: {item['seo_title']}")
        if not 110 <= len(item["seo_description"]) <= 165:
            problems.append(f"description {len(item['seo_description'])}: {item['slug']}")
    for cat in manifest["categories"]:
        if not 110 <= len(cat["description"]) <= 165:
            problems.append(f"category description {len(cat['description'])}: {cat['slug']}")
    slugs = [i["slug"] for i in manifest["pages"] + manifest["posts"]]
    problems += [f"duplicate slug: {s}" for s in sorted({s for s in slugs if slugs.count(s) > 1})]
    cats = {c["slug"] for c in manifest["categories"]}
    images = {f.name for f in (ROOT / "theme/joe-bogdan-mlo/assets/images").iterdir()}
    for post in posts.POSTS:
        if post["category"] not in cats:
            problems.append(f"unknown category {post['category']}: {post['slug']}")
        if post.get("image") and post["image"] not in images:
            problems.append(f"missing image {post['image']}: {post['slug']}")
    for post in posts.POSTS:
        if post["slug"] in posts.DAILY_SLUGS:
            text = " ".join([post["title"], post["excerpt"], post["seo_title"], post["content"]])
            problems += [f"compliance ({post['slug']}): {m}" for m in compliance_issues(text)]
    if problems:
        raise SystemExit("SEO length check failed:\n  " + "\n  ".join(problems))
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(pages.PAGES)} pages, {len(posts.POSTS)} posts")


if __name__ == "__main__":
    main()
