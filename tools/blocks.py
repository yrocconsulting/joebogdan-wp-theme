"""Tiny helpers that emit valid WordPress block markup.

Page copy lives in tools/pages.py and is written with these helpers so the
generated content/pages/*.html opens cleanly in the block editor.
"""
import html
import json


def _attrs(d):
    d = {k: v for k, v in d.items() if v not in (None, "", False)}
    return " " + json.dumps(d, ensure_ascii=False, separators=(",", ":")) if d else ""


def _cls(*names):
    return " ".join(n for n in names if n)


def esc(text):
    """Escape text but keep the small amount of inline markup we author (<a>, <strong>, <em>)."""
    return text


def p(text, cls=None):
    c = f' class="{cls}"' if cls else ""
    return f"<!-- wp:paragraph{_attrs({'className': cls})} -->\n<p{c}>{esc(text)}</p>\n<!-- /wp:paragraph -->"


def h(text, level=2, cls=None):
    a = {"level": level if level != 2 else None, "className": cls}
    return f'<!-- wp:heading{_attrs(a)} -->\n<h{level} class="{_cls("wp-block-heading", cls)}">{esc(text)}</h{level}>\n<!-- /wp:heading -->'


def ul(items, cls=None):
    lis = "".join(f"<!-- wp:list-item -->\n<li>{esc(i)}</li>\n<!-- /wp:list-item -->" for i in items)
    return f'<!-- wp:list{_attrs({"className": cls})} -->\n<ul class="{_cls("wp-block-list", cls)}">{lis}</ul>\n<!-- /wp:list -->'


def ol(items, cls=None):
    lis = "".join(f"<!-- wp:list-item -->\n<li>{esc(i)}</li>\n<!-- /wp:list-item -->" for i in items)
    return f'<!-- wp:list{_attrs({"ordered": True, "className": cls})} -->\n<ol class="{_cls("wp-block-list", cls)}">{lis}</ol>\n<!-- /wp:list -->'


def group(*inner, cls=None, tag=None):
    t = tag or "div"
    a = {"tagName": tag if tag and tag != "div" else None, "className": cls}
    body = "\n".join(inner)
    return f'<!-- wp:group{_attrs(a)} -->\n<{t} class="{_cls("wp-block-group", cls)}">{body}</{t}>\n<!-- /wp:group -->'


def button(label, url, outline=False):
    cls = "is-style-outline" if outline else None
    return (
        f"<!-- wp:button{_attrs({'className': cls})} -->\n"
        f'<div class="{_cls("wp-block-button", cls)}"><a class="wp-block-button__link wp-element-button" href="{html.escape(url, quote=True)}">{label}</a></div>\n'
        "<!-- /wp:button -->"
    )


def buttons(*btns):
    return "<!-- wp:buttons -->\n<div class=\"wp-block-buttons\">" + "\n".join(btns) + "</div>\n<!-- /wp:buttons -->"


def sc(code):
    return f"<!-- wp:shortcode -->\n{code}\n<!-- /wp:shortcode -->"


# ---- composed sections --------------------------------------------------

def section(*inner, tone="ivory", narrow=False, id=None, extra=None):
    wrap_cls = "wrap wrap-narrow" if narrow else "wrap"
    cls = _cls("section", f"section-{tone}", extra)
    g = group(group(*inner, cls=wrap_cls), cls=cls, tag="section")
    if id:
        # Group anchors are sourced from the element's id attribute.
        g = g.replace(f'<section class="wp-block-group {cls}">', f'<section id="{id}" class="wp-block-group {cls}">', 1)
    return g


def head(eyebrow, title, lede=None, center=True):
    parts = [p(eyebrow, "eyebrow"), h(title, 2, "section-title")]
    if lede:
        parts.append(p(lede, "section-lede"))
    return group(*parts, cls="section-head" if center else "section-head section-head-left")


def card(title, text, link=None, icon_cls=None):
    parts = [h(title, 3), p(text)]
    if link:
        parts.append(p(f'<a href="{link[1]}">{link[0]} →</a>', "card-link"))
    return group(*parts, cls=_cls("card", icon_cls))


def cards(*cs, cols=3):
    return group(*cs, cls=f"card-grid card-grid-{cols}")


def split(left, right, cls=None):
    return group(group(*left, cls="split-a"), group(*right, cls="split-b"), cls=_cls("split", cls))


def faq(title, qas, eyebrow="Frequently Asked Questions"):
    items = "".join(f'[jb_q q="{q}"]{a}[/jb_q]' for q, a in qas)
    return sc(f'[jb_faq title="{title}" eyebrow="{eyebrow}"]{items}[/jb_faq]')


def form_section(eyebrow, title, lede, bullets, form_type, id=None, tone="navy"):
    copy = [p(eyebrow, "eyebrow"), h(title, 2, "section-title"), p(lede)]
    if bullets:
        copy.append(ul(bullets, "check-list"))
    return section(group(group(*copy, cls="split-form-copy"), sc(f'[jb_form type="{form_type}"]'), cls="split-form"), tone=tone, id=id)


def page(*sections):
    return "\n\n".join(sections) + "\n"
