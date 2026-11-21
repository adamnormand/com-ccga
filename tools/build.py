#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Static site generator for com-ccga (CCGA · GCAC network).

Usage:  python3 tools/build.py          (run from the repo root)
Writes plain HTML into the repo root (EN) and /fr/ (FR). No dependencies.
Edit content in tools/content_national.py and tools/content_regions.py, then rebuild and commit.
"""
import os, re, sys, html, posixpath, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content_national import NATIONAL
from content_regions import REGIONS, facts as facts_html

SECTIONS = [NATIONAL] + REGIONS
BYKEY = {s["key"]: s for s in SECTIONS}
LANGS = ["en", "fr"]
OTHER = {"en": "fr", "fr": "en"}
YEAR = 2026
INSTAGRAM = "https://www.instagram.com/ccga_aux_gcac/"
CUR = ' aria-current="true"'
CURP = ' aria-current="page"'
SARCOM = "https://sms.ccga-gcac.ca/"   # placeholder target for the "SARCOM Login" button — confirm

T = {  # UI strings
 "network": {"en": 'CCGA · GCAC<span class="xl"> Network</span>', "fr": '<span class="xl">Réseau </span>GCAC · CCGA'},
 "emerg": {"en": "Marine emergency", "fr": "Urgence maritime"},
 "switch": {"en": "Français", "fr": "English"},
 "join": {"en": "Join", "fr": "Joindre"},
 "donate": {"en": "Donate", "fr": "Donner"},
 "menu": {"en": "Menu", "fr": "Menu"},
 "skip": {"en": "Skip to content", "fr": "Passer au contenu"},
 "tagline": {"en": "Saving lives on the water", "fr": "Sauver des vies sur l'eau"},
 "charity": {"en": "A volunteer charity — donations needed.", "fr": "Un organisme de bienfaisance bénévole — vos dons comptent."},
 "bn": {"en": "Charitable registration number (BN): 870298494RR0001", "fr": "Numéro d'enregistrement d'organisme de bienfaisance (NE) : 870298494RR0001"},
 "quick": {"en": "Quick links", "fr": "Liens rapides"},
 "fed": {"en": "The federation", "fr": "La fédération"},
 "contact": {"en": "Contact", "fr": "Contact"},
 "privacy": {"en": "Privacy", "fr": "Confidentialité"},
 "access": {"en": "Accessibility", "fr": "Accessibilité"},
 "ccg": {"en": "Canadian Coast Guard", "fr": "Garde côtière canadienne"},
 "ccgurl": {"en": "https://www.canada.ca/en/canadian-coast-guard.html", "fr": "https://www.canada.ca/fr/garde-cotiere-canadienne.html"},
 "copy": {"en": "© {y} Canadian Coast Guard Auxiliary (National) Inc. · Garde côtière auxiliaire canadienne (nationale) inc.",
          "fr": "© {y} Garde côtière auxiliaire canadienne (nationale) inc. · Canadian Coast Guard Auxiliary (National) Inc."},
 "back": {"en": "National site", "fr": "Site national"},
 "region": {"en": "Region", "fr": "Région"},
 "emergnum": {"en": "Emergency", "fr": "Urgence"},
 "area": {"en": "Area", "fr": "Territoire"},
 "visit": {"en": "Visit", "fr": "Visiter"},
 "home": {"en": "Home", "fr": "Accueil"},
 "regional_home": {"en": "Overview", "fr": "Aperçu"},
 "in_section": {"en": "In this section", "fr": "Dans cette section"},
 "sarcom": {"en": 'SARCOM<span class="xl"> Login</span>', "fr": '<span class="xl">Connexion </span>SARCOM'},
}

# ---------------------------------------------------------------- paths
def page_path(sec, key, lang):
    """URL path (no leading slash, trailing slash) of a page."""
    pg = sec["pages"][key]
    parts = []
    if lang == "fr": parts.append("fr")
    if sec["path"][lang]: parts.append(sec["path"][lang])
    if pg["slug"][lang]: parts.append(pg["slug"][lang])
    return "/".join(parts) + ("/" if parts else "")

def rel(from_path, to_path):
    """Relative href between two directory-style paths ('' = site root)."""
    frm = "/" + from_path
    to = "/" + to_path
    r = posixpath.relpath(to, frm if frm.endswith("/") else posixpath.dirname(frm))
    if r == ".": r = "./"
    elif not r.endswith("/"): r += "/"
    return r

def asset(from_path, name):
    return posixpath.relpath("/assets/" + name, "/" + from_path) if from_path else "assets/" + name

# ---------------------------------------------------------------- shared blocks
def region_cards(lang, here):
    out = ['<div class="regions">']
    for r in REGIONS:
        out.append(f'<a class="rcard" href="{rel(here, page_path(r, "index", lang))}"><span class="rname">{r["name"][lang]}</span>'
                   f'<span class="rorg">{r["org"][lang]}</span><span class="rarea">{r["area"][lang]}</span>'
                   f'<span class="rfig">{r["figure"][lang]}</span></a>')
    out.append("</div>")
    return "".join(out)

def region_table(lang, here):
    rows = "".join(f'<tr><td><a href="{rel(here, page_path(r, "index", lang))}">{r["name"][lang]}</a></td><td>{r["area"][lang]}</td><td>{r["emergency"][lang]}</td></tr>' for r in REGIONS)
    return (f'<div class="card"><table><thead><tr><th>{T["region"][lang]}</th><th>{T["area"][lang]}</th><th>{T["emergnum"][lang]}</th></tr></thead>'
            f'<tbody>{rows}</tbody></table></div>')

def region_list(lang, here):
    return '<ul class="plain">' + "".join(
        f'<li><a href="{rel(here, page_path(r, "contact", lang))}">{r["name"][lang]}</a></li>' for r in REGIONS) + "</ul>"

def fill(body, sec, key, lang, here):
    pg = sec["pages"][key]
    def rlink(m):
        k = m.group(1)
        if k not in sec["pages"]: raise KeyError(f"{sec['key']}: unknown page '{k}' in {key}")
        return rel(here, page_path(sec, k, lang))
    def nlink(m):
        return rel(here, page_path(NATIONAL, m.group(1), lang))
    body = re.sub(r"\{r:([a-z0-9-]+)\}", rlink, body)
    body = re.sub(r"\{n:([a-z0-9-]+)\}", nlink, body)
    if "{facts}" in body: body = body.replace("{facts}", facts_html(pg["facts"][lang]))
    body = body.replace("{regioncards}", region_cards(lang, here))
    body = body.replace("{regiontable}", region_table(lang, here))
    body = body.replace("{regionlist}", region_list(lang, here))
    return body

# ---------------------------------------------------------------- icons (inline SVG)
IG = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor"/></svg>'
LIFE = '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8" fill="none" stroke="#fff" stroke-width="5"/><g stroke="#C8102E" stroke-width="2.2"><line x1="12" y1="2" x2="12" y2="7"/><line x1="12" y1="17" x2="12" y2="22"/><line x1="2" y1="12" x2="7" y2="12"/><line x1="17" y1="12" x2="22" y2="12"/></g></svg>'
LOCK = '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="5" y="10" width="14" height="11" rx="2" fill="currentColor"/><path d="M8 10V7a4 4 0 0 1 8 0v3" fill="none" stroke="currentColor" stroke-width="2"/></svg>'

# ---------------------------------------------------------------- page template
def render(sec, key, lang):
    pg = sec["pages"][key]
    here = page_path(sec, key, lang)
    other = OTHER[lang]
    is_nat = sec is NATIONAL
    css = asset(here, "site.css")
    crest = asset(here, "ccga-crest.png")
    title = pg["title"][lang]
    site = NATIONAL["org"][lang]
    full_title = f"{title} | {sec['short'][lang] + ' · ' if not is_nat else ''}{site}" if key != "index" or not is_nat else f"{site} · {T['tagline'][lang]}"
    desc = (pg.get("hero", {}).get(lang, (None, None))[1] if pg.get("hero") else None) or sec.get("lead", {}).get(lang) or T["tagline"][lang]

    # network dropdown
    net_items = [f'<li><a href="{rel(here, page_path(NATIONAL, "index", lang))}"{CUR if is_nat else ""}>{NATIONAL["name"][lang]}</a></li>']
    for r in REGIONS:
        cur = ' aria-current="true"' if r is sec else ""
        net_items.append(f'<li><a href="{rel(here, page_path(r, "index", lang))}"{cur}>{r["short"][lang]}</a></li>')
    network = (f'<details class="network"><summary>☰ {T["network"][lang]}</summary><ul>{"".join(net_items)}</ul></details>')

    switch = rel(here, page_path(sec, key, other))
    emergency = sec["emergency"][lang]

    topbar = f"""<div class="topbar"><div class="wrap topbar-in">
{network}
<p class="emerg">{LIFE}<b>{T['emerg'][lang]}:</b> <span>{emergency}</span></p>
<div class="top-right"><a class="lang" href="{switch}" lang="{other}" hreflang="{other}" data-short="{other.upper()}">{T['switch'][lang]}</a>
<a class="ico" href="{INSTAGRAM}" rel="noopener" aria-label="Instagram">{IG}</a>
<a class="sarcom" href="{SARCOM}" rel="noopener">{LOCK}{T['sarcom'][lang]}</a></div>
</div></div>"""

    # main nav
    nav_items = []
    if not is_nat:
        nav_items.append((page_path(sec, "index", lang), T["regional_home"][lang], key == "index"))
    for k in sec["nav"]:
        nav_items.append((page_path(sec, k, lang), sec["pages"][k]["title"][lang] if is_nat else short_title(sec, k, lang), k == key or key in sec["pages"][k].get("sub", [])))
    nav = "".join(f'<li><a href="{rel(here, p)}"{CURP if cur else ""}>{html.escape(lbl)}</a></li>' for p, lbl, cur in nav_items)
    join_href = rel(here, page_path(sec, sec["join"], lang))
    don_href = rel(here, page_path(sec, sec["donate"], lang))

    brand_sub = f'<span class="brand-sub">{sec["name"][lang]}</span>' if not is_nat else ""
    header = f"""<header class="site-header"><div class="wrap header-in">
<a class="brand" href="{rel(here, page_path(sec, 'index', lang))}"><img src="{crest}" alt="" width="40" height="62"><span class="brand-text">{site.replace('Auxiliary', '<br>Auxiliary').replace('auxiliaire', '<br>auxiliaire', 1)}{brand_sub}</span></a>
<input type="checkbox" id="navtoggle" class="nav-toggle"><label for="navtoggle" class="menu-btn" aria-label="Menu">{T['menu'][lang]}</label>
<nav class="menu" aria-label="{T['menu'][lang]}"><ul>{nav}</ul>
<div class="cta"><a class="btn btn-ghost" href="{join_href}">{T['join'][lang]}</a><a class="btn" href="{don_href}">{T['donate'][lang]} →</a></div></nav>
</div></header>"""

    # hero / page head
    if pg.get("hero"):
        h1, sub = pg["hero"][lang]
        eyebrow = sec["org"][lang] if not is_nat else site
        head = f"""<section class="hero" style="background-image:linear-gradient(100deg,rgba(14,34,56,.94) 0%,rgba(20,48,79,.82) 55%,rgba(20,48,79,.45) 100%),url('{asset(here, "rescue-boat.jpg")}')"><div class="wrap"><p class="eyebrow light">{eyebrow}</p><h1>{h1}</h1><p class="hero-sub">{sub}</p>
<p><a class="btn" href="{join_href}">{T['join'][lang]}</a> <a class="btn btn-light" href="{don_href}">{T['donate'][lang]} →</a></p></div></section>"""
    else:
        crumbs = f'<a href="{rel(here, page_path(NATIONAL, "index", lang))}">{T["home"][lang]}</a>'
        if not is_nat:
            crumbs += f' › <a href="{rel(here, page_path(sec, "index", lang))}">{sec["name"][lang]}</a>'
        parent = next((k for k in sec["nav"] if key in sec["pages"][k].get("sub", [])), None)
        if parent:
            crumbs += f' › <a href="{rel(here, page_path(sec, parent, lang))}">{sec["pages"][parent]["title"][lang]}</a>'
        head = f'<section class="pagehead"><div class="wrap"><p class="crumbs">{crumbs}</p><h1>{title}</h1></div></section>'

    body = fill(pg["body"][lang], sec, key, lang, here)

    # sub-page links for parents
    if pg.get("sub"):
        links = "".join(f'<a class="chip" href="{rel(here, page_path(sec, k, lang))}">{sec["pages"][k]["title"][lang]}</a>' for k in pg["sub"])
        body = f'<nav class="wrap subnav" aria-label="{T["in_section"][lang]}">{links}</nav>' + body

    # footer
    quick_keys = ["about", "regions", "what-we-do", "volunteer", "donate", "news", "careers", "contact"]
    quick = "".join(f'<li><a href="{rel(here, page_path(NATIONAL, k, lang))}">{NATIONAL["pages"][k]["title"][lang]}</a></li>' for k in quick_keys)
    fed = f'<li><a href="{rel(here, page_path(NATIONAL, "index", lang))}">{NATIONAL["name"][lang]}</a></li>' + "".join(
        f'<li><a href="{rel(here, page_path(r, "index", lang))}">{r["short"][lang]}</a></li>' for r in REGIONS) + \
        f'<li><a href="{T["ccgurl"][lang]}" rel="noopener">{T["ccg"][lang]}</a></li>'
    footer = f"""<div class="banner" style="background-image:url('{asset(here, "rescue-boat.jpg")}')" role="presentation"></div>
<footer class="site-footer"><div class="wrap fgrid">
<div><p class="fhead">{T['tagline'][lang]}</p><p>{NATIONAL['org']['en']} / {NATIONAL['org']['fr']}</p><p class="small">{T['bn'][lang]}</p><p class="small">{T['charity'][lang]}</p></div>
<div><p class="flabel">{T['quick'][lang]}</p><ul>{quick}</ul></div>
<div><p class="flabel">{T['fed'][lang]}</p><ul>{fed}</ul></div>
<div><p class="flabel">{T['contact'][lang]}</p><p>{sec['contact_block'][lang]}</p></div>
</div>
<div class="wrap fbottom"><p><a href="{rel(here, page_path(NATIONAL, 'privacy', lang))}">{T['privacy'][lang]}</a> · <a href="{rel(here, page_path(NATIONAL, 'accessibility', lang))}">{T['access'][lang]}</a></p>
<p>{T['copy'][lang].format(y=YEAR)}</p></div></footer>"""

    return f"""<!DOCTYPE html>
<html lang="{lang}-CA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="alternate" hreflang="{other}" href="{switch}">
<link rel="icon" href="{asset(here, 'favicon.svg')}" type="image/svg+xml">
<link rel="apple-touch-icon" href="{asset(here, 'apple-touch-icon.png')}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css}">
</head>
<body class="sec-{sec['key']}">
<a class="skip" href="#main">{T['skip'][lang]}</a>
{topbar}
{header}
<main id="main">
{head}
{body}
</main>
{footer}
</body>
</html>
"""

def short_title(sec, k, lang):
    t = sec["pages"][k]["title"][lang]
    # trim region suffixes in nav: "Contact RCMSAR" -> "Contact"
    for pre in ("Contact", "Joindre", "Volunteer", "Devenir bénévole", "About", "À propos", "Donate", "Donner"):
        if t.startswith(pre) and t != pre:
            return {"Joindre": "Contact", "Devenir bénévole": "Bénévolat", "Volunteer": "Volunteer"}.get(pre, pre)
    return t

# ---------------------------------------------------------------- main
def main():
    written = []
    for sec in SECTIONS:
        for key in sec["pages"]:
            for lang in LANGS:
                p = page_path(sec, key, lang)
                out = os.path.join(ROOT, p, "index.html")
                os.makedirs(os.path.dirname(out), exist_ok=True)
                with open(out, "w", encoding="utf-8") as f:
                    f.write(render(sec, key, lang))
                written.append(p or "/")
    # 404
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(render_404())
    print(f"{len(written)} pages written")

def render_404():
    return """<!DOCTYPE html><html lang="en-CA"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Page not found · Page introuvable</title><link rel="icon" href="/favicon.svg"><style>body{font-family:Inter,Segoe UI,Roboto,Arial,sans-serif;margin:0;min-height:100vh;display:grid;place-items:center;background:#0E2238;color:#fff;text-align:center;padding:24px}a{color:#fff}h1{font-size:28px}p{color:#DCE4EC}</style></head>
<body><div><h1>Page not found · Page introuvable</h1><p>Marine emergency / Urgence maritime : VHF 16 · *16 · 911</p><p><a href="/">Home</a> · <a href="/fr/">Accueil</a></p></div></body></html>
"""

if __name__ == "__main__":
    main()
