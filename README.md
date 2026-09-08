# Mehdi Benbarka's portfolio

A small, responsive portfolio of public AI research and software projects.

Intended address: https://mehdiben30.github.io/

## Run locally

From this folder:

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173. The site uses plain HTML and CSS, with an SVG favicon. It has no package installation, build step, runtime API, or JavaScript dependency.

## Edit the portfolio

- `index.html`: name, introduction, project descriptions, links, and diagrams.
- `styles.css`: layout, typography, colours, responsive and print styles.
- `assets/favicon.svg`: browser icon.
- `404.html`: missing-page screen.
- `sitemap.xml` and `robots.txt`: search-engine discovery.

Add a project by copying an `<article class="project">` block. Give its heading a unique ID, update the project number and total count, and check that all links are accessible without signing in. Label incomplete features accurately.

## Hosting

The repository is intended to be `mehdiben30/mehdiben30.github.io`, with GitHub Pages serving `/` on `main`. The `.nojekyll` file makes the site a plain static publication. Once Pages is enabled, pushing to `main` publishes changes automatically.

In GitHub: **Settings → Pages → Deploy from a branch → main → /(root)**.

For another hostname, update the canonical URL, Open Graph URL, sitemap, and robots file. Configure a custom domain through GitHub Pages settings before adding a matching `CNAME` file.

## Design and content decisions

- A 1120 px content area, an 8 px spacing scale, and project rows with room for the explanation and diagram.
- Georgia for display text; the system sans-serif stack for body and navigation. Both use installed fonts, avoiding external font requests.
- Warm neutral backgrounds and a green accent derived from `#315c48`; text contrast is checked against actual backgrounds.
- Native links and expandable details, a keyboard skip link, visible focus, and reduced-motion support.
- Diagrams explain methods; they do not represent measured results.
- Initial descriptions were checked against public repository documentation on 2026-09-08. AutoProbe is explicitly marked as in development. All linked project materials are public.
- GitHub is the contact/profile link. No email address, employment history, or qualifications are inferred.

## Verification

With Python Playwright and Chrome installed:

```powershell
python scripts/check_site.py
```

The check starts a temporary local server and verifies desktop/mobile layout, internal links, keyboard navigation, expandable notes, JavaScript-free rendering, and text contrast. Screenshots and a check record are written into the git-ignored `.preview/` directory.
