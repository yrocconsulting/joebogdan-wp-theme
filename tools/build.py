"""Regenerate content/ from tools/pages.py.

    python3 tools/build.py
"""
import json
import pathlib

import pages
import posts

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "content"


def main():
    (OUT / "pages").mkdir(parents=True, exist_ok=True)
    manifest = {"pages": [], "menus": {}, "categories": [], "front_page": "home", "posts_page": "insights"}
    for slug, title, parent, template, body, seo_title, seo_desc, service, order, excerpt in pages.PAGES:
        (OUT / "pages" / f"{slug}.html").write_text(body, encoding="utf-8")
        manifest["pages"].append({
            "slug": slug, "title": title, "parent": parent, "template": template or "",
            "file": f"pages/{slug}.html", "seo_title": seo_title or "", "seo_description": seo_desc or "",
            "service": service or "", "audience": pages.AUDIENCE.get(slug, ""), "menu_order": order, "excerpt": excerpt or "",
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
    if problems:
        raise SystemExit("SEO length check failed:\n  " + "\n  ".join(problems))
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(pages.PAGES)} pages, {len(posts.POSTS)} posts")


if __name__ == "__main__":
    main()
