"""Regenerate content/ from tools/pages.py.

    python3 tools/build.py
"""
import json
import pathlib

import pages

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
            "service": service or "", "menu_order": order, "excerpt": excerpt or "",
        })
    for location, items in pages.MENUS.items():
        manifest["menus"][location] = [
            {"title": t, "page": s, "children": [{"title": ct, "page": cs} for ct, cs in kids]}
            for t, s, kids in items
        ]
    manifest["categories"] = [{"slug": s, "name": n, "description": d} for s, n, d in pages.CATEGORIES]
    (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {len(pages.PAGES)} pages")


if __name__ == "__main__":
    main()
