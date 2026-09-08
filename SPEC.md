# Portfolio frontend

## Status: simplified implementation; locally verified

## User request

"for now i just want simplicity and that you add my other proejcts to the portfolio"

## Current scope

A simple English page containing the person's name, a short introduction, a GitHub profile link, and nine project entries:

1. Attempt vs Outcome
2. Calibrate Once?
3. AutoProbe
4. PatternLens
5. GPT Implementation
6. Few-shot Clustering with LLMs
7. IceBreaker
8. Car Rental API
9. Docker Classification Workflow

Descriptions are based on the public repositories and, for IceBreaker and the clustering project, the existing public portfolio source in `intelligent-canvas-exhibit`. The clustering link is explicitly labeled as a reference paper. IceBreaker has no invented or disabled project link. The duplicate GPT repository, empty repositories, introductory notebook, forks, and the older portfolio itself are omitted.

## Behavior and content

- `design.md` records the simple layout and tokens.
- One column, standard fonts, white background, readable text links, and compact rows.
- Existing research method and limitation notes remain in native disclosures.
- Projects in development are labeled. No performance results, personal credentials, or launch dates are inferred.
- Works without JavaScript or downloaded fonts.
- GitHub Pages serves the root of main.

## Verification

Check desktop and phone widths, horizontal overflow, project count, internal links, keyboard navigation, disclosures, text contrast, and the missing-page return link. Inspect screenshots before publication and check the deployed files afterward.

## Pending preference

The user has been asked whether to also mention private projects. The current version uses public material only.

## Version history

- 2026-09-08 v1: Implemented the editorial direction and native observation explorer. Verification in progress.
- 2026-09-08 v1.1: Verified five complete browser scenarios plus eleven intermediate widths, text and diagram contrast, font loading, keyboard controls, and preserved research descriptions and links.
- 2026-09-08 v1.2: User rejected the overall design. Reopened visual direction; previous technical verification must not be read as user approval.

- 2026-09-08 v2: Implemented the user-requested simple layout and expanded the page from two to nine documented projects.
