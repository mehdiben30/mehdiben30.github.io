# Mehdi Benbarka's portfolio

Live site: https://mehdiben30.github.io/

A simple HTML and CSS page with research and software projects. No build step, JavaScript, or external font requests are required.

## Run locally

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173.

## Edit

- `index.html`: introduction, project descriptions, and links.
- `styles.css`: typography, spacing, and responsive layout.
- `404.html` and `assets/favicon.svg`: missing-page screen and browser icon.
- `design.md` and `SPEC.md`: current design and content scope.

Each project is an `<article class="project">` with a unique heading ID. Keep descriptions concise and link only to the intended public materials. The existing research details use native disclosures.

## Verify

With Python Playwright and Chrome installed:

```powershell
python scripts/check_site.py
```

The script checks desktop/mobile layout, keyboard navigation, project count, disclosures, internal links, the 404 page, and text contrast. Screenshots and verification output go into the ignored `.preview/` directory.

## Hosting

GitHub Pages publishes `/` from `main` in `mehdiben30/mehdiben30.github.io`. Pushing to `main` updates the site. `.nojekyll` keeps it a plain static publication.
