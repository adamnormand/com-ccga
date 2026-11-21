# com-ccga — Canadian Coast Guard Auxiliary · Garde côtière auxiliaire canadienne

A single static website for the CCGA federation: the **National** site plus six **regional subsites**, in English and French. It's plain HTML and CSS with no JavaScript, no build step on the server, and no tracking. It's hosted on GitHub Pages.

The design follows the national demo (`ccgagcac.kinsta.cloud`): a network bar, a marine-emergency strip, a language toggle, the SARCOM button, the crest header with Join/Donate, and the navy footer. The content comes from the live sites, read on 2026-11-21.

| Section | EN | FR | Source |
|---|---|---|---|
| National | `/` | `/fr/` | ccga-gcac.ca |
| Pacific — RCMSAR | `/pacific/` | `/fr/pacifique/` | rcmsar.com |
| Coastal Nations | `/coastal-nations/` | `/fr/nations-cotieres/` | cn-cga.ca |
| Central & Arctic | `/central-arctic/` | `/fr/centre-arctique/` | ccga-ca.com |
| Québec | `/quebec/` | `/fr/quebec/` | gcac-q.ca (FR source, translated to EN) |
| Maritimes | `/maritimes/` | `/fr/maritimes/` | ccga-m.ca |
| Newfoundland & Labrador | `/newfoundland-labrador/` | `/fr/terre-neuve-labrador/` | ccga-nl.ca |

There are 90 pages (45 EN + 45 FR) plus a `404.html`. Every page links to its counterpart in the other language.

## Editing

The content lives in `tools/content_national.py` and `tools/content_regions.py` as one EN/FR HTML string per page. The layout, header and footer live in `tools/build.py`, and the styles in `assets/site.css`.

```
python3 tools/build.py      # regenerates every index.html (Python 3.8+, no packages)
git add -A && git commit -m "Update content" && git push
```

Never edit the generated `index.html` files by hand, because the next build overwrites them.

Link placeholders you can use in content:
- `{r:key}` links to a page in the same section.
- `{n:key}` links to a National page.
- `{facts}`, `{regioncards}`, `{regiontable}` and `{regionlist}` insert shared blocks.

## Publishing on GitHub Pages

1. Go to Settings → Pages → Deploy from branch → `main` / root.
2. For a custom domain, add a `CNAME` file containing the bare domain, then point DNS:
   - `@` A records: 185.199.108.153 / .109.153 / .110.153 / .111.153
   - `www` CNAME: `<github-user>.github.io`
   - Remove the old A/CNAME records. Don't touch MX, TXT/SPF or DKIM records.
3. Turn on Enforce HTTPS once the certificate has been issued.

All links are relative, so the site also works at `https://<user>.github.io/com-ccga/` before the domain moves. The `404.html` uses root links, so it only works correctly on the custom domain.

## To confirm before going public

- **SARCOM Login** currently points to `sms.ccga-gcac.ca` as a placeholder (`SARCOM` in `build.py`).
- **Facebook** is left out because the page ID wasn't readable. Only Instagram (`ccga_aux_gcac`) is linked.
- **CanadaHelps FR link** (`/fr/organismesdebienfaisance/...`) needs to be tested.
- **Figures differ between sources.** The regional sites' own numbers were used:
  - RCMSAR: 29 stations / 950+ volunteers (the national page says 31 / 974).
  - C&A: 1,013 members / 83 vessels (the national page says 926 / 102).
  - Maritimes: 800 / ~400 (the national page says 721 / 380).
- **Coastal Nations:** the Nation each board pair represents was shown only as images on cn-cga.ca, so the Nation names still need to be filled in.
- **Maritimes programs page** (safety checks, Kids Don't Float, Bobbie) is a summary. The details need to come from CCGA-M.
- **Maritimes / NL emergency strip** shows VHF 16 / *16 / 911 only, because no JRCC number was published on their sites.
- **News page** has headlines and summaries only. The full articles weren't migrated.
- **Hero photo** (`assets/rescue-boat.jpg`) is the demo's 960 px footer banner. Replace it with a high-resolution photo.
- **Crest** (`assets/ccga-crest.png`) was captured from the demo at 120 px. Swap in the official vector file if one is available.
- Regional contact pages still link to each region's current website and member login during the transition.
