# Portfolio frontend

## Status: implemented and verified

## Purpose

Give Mehdi Benbarka's public research and software projects a distinctive, readable presentation. The working audience is AI research teams and collaborators; this is an assumption pending user feedback. A visitor should be able to identify the focus, understand each project's question, and reach its report or code without opening the technical notes.

## Scope

- English static portfolio for Attempt vs Outcome and AutoProbe.
- Expressive typography, a responsive editorial grid, bespoke method diagrams, and an observation-point explorer.
- Preserve project descriptions, public destinations, research limitations, and AutoProbe's development status.
- Consistent homepage, favicon, and missing-page treatment.
- GitHub Pages deployment from the root of `main`.

## Design and behavior

- `design.md` records the token system. `--display` is for headings and `--body` for reading; `--accent` marks actions and selected states.
- The hero introduces the person and research focus. Selected work presents the research study first and evaluation tooling second.
- Pending, rejected, and applied are native radio controls. Each selects an explanatory paragraph. This is a study-design illustration; it does not run an AI model or show measured scores.
- Method and scope remain available through native disclosures.
- AutoProbe's diagram illustrates a task family, related tasks, and repeated runs; its caption states that development is ongoing.
- JavaScript and external runtime services are not required. Fonts and their licenses are served locally.
- The existing contact destination is the public GitHub profile.

## Acceptance checks

- No horizontal overflow at 320, 390, 768, 1024, and 1440 px.
- Navigation, observation selection by mouse and arrow keys, disclosures, and the 404 return link work with JavaScript disabled.
- Text palette pairs meet a 4.5:1 contrast floor on actual surfaces.
- Font requests succeed, and desktop and phone screenshots are visually reviewed.
- Public files match the verified local version after publication.

## Open issues

- The audience preference remains open; the implementation uses the research audience assumption.
- No outstanding implementation issues. Desktop and phone screenshots have been reviewed.

## Version history

- 2026-09-08 v1: Implemented the editorial direction and native observation explorer. Verification in progress.
- 2026-09-08 v1.1: Verified five complete browser scenarios plus eleven intermediate widths, text and diagram contrast, font loading, keyboard controls, and preserved research descriptions and links.
