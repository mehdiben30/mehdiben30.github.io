# Mehdi Benbarka's portfolio

A small, responsive portfolio of public AI research and software projects.

Live site: https://mehdiben30.github.io/

## Run locally

From this folder:

```powershell
python -m http.server 4173 --bind 127.0.0.1
```

Open http://127.0.0.1:4173. The site uses HTML and CSS, native radio controls and disclosures, SVG diagrams, and self-hosted WOFF2 fonts. It has no package installation, build step, runtime API, or JavaScript dependency.

## Edit the portfolio

- `index.html`: name, introduction, project descriptions, links, and diagrams.
- `styles.css`: layout, typography, colours, responsive and print styles.
- `assets/favicon.svg`: browser icon.
- `assets/fonts/`: Newsreader and Public Sans fonts, with their open-source licenses.
- `design.md` and `SPEC.md`: design tokens, responsive rules, interaction behavior, and project scope.
- `404.html`: missing-page screen.
- `sitemap.xml` and `robots.txt`: search-engine discovery.

Add a project by copying an `<article class="project">` block. Give its heading a unique ID, update the project number and total count, and check that all links are accessible without signing in. Label incomplete features accurately.

## Hosting

The repository is `mehdiben30/mehdiben30.github.io`, with GitHub Pages serving `/` on `main`. The `.nojekyll` file makes the site a plain static publication. Pushing to `main` publishes changes automatically.

In GitHub: **Settings → Pages → Deploy from a branch → main → /(root)**.

For another hostname, update the canonical URL, Open Graph URL, sitemap, and robots file. Configure a custom domain through GitHub Pages settings before adding a matching `CNAME` file.

## Design and content decisions

- A 1200 px content area, a 12-column desktop grid, and a 4 px spacing scale. Project visuals and copy stack on smaller screens.
- Newsreader for display text and Public Sans for reading and navigation. Both are self-hosted, with system fallbacks.
- Warm neutral backgrounds and a rust accent derived from `#a13d2d`; text contrast is checked against actual backgrounds.
- Native links, an observation-point radio group, expandable details, a keyboard skip link, visible focus, and reduced-motion support.
- Diagrams explain methods; they do not represent measured results.
- Initial descriptions were checked against public repository documentation on 2026-09-08. AutoProbe is explicitly marked as in development. All linked project materials are public.
- GitHub is the contact/profile link. No email address, employment history, or qualifications are inferred.

## Verification

With Python Playwright and Chrome installed:

```powershell
python scripts/check_site.py
```

The check starts a temporary local server and verifies five desktop/mobile widths, internal links, keyboard navigation, observation selection, expandable notes, font loading, JavaScript-free rendering, and text contrast. Screenshots and a check record are written into the git-ignored `.preview/` directory.
