# Portfolio design system

Updated: 2026-09-08

## Direction

An editorial portfolio for AI research and software. Large serif headlines establish a personal voice; concise project descriptions lead to public reports and code. Rust identifies selected states and actions. Diagram colors encode structure and execution state, never measured performance.

## Tokens

All colors below use sRGB. Spacing uses a 4 px base. These values are implemented in the root declaration in `styles.css`.

| Token | Value |
| --- | --- |
| `--canvas` | `#f7f4f0` |
| `--surface` | `#efeae4` |
| `--ink` | `#24221e` |
| `--muted` | `#6c6760` |
| `--line` | `#d5cec3` |
| `--accent` | `#a13d2d` |
| `--accent-hover` | `#8c3527` |
| `--accent-soft` | `#f9edeb` |
| `--inverse-muted` | `#c1bcb3` |
| `--inverse-line` | `#787268` |
| `--inverse-accent` | `#de9387` |
| `--display` | `Newsreader, Georgia, 'Times New Roman', serif` |
| `--body` | `'Public Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif` |
| `--space-1` | `4px` |
| `--space-2` | `8px` |
| `--space-3` | `12px` |
| `--space-4` | `16px` |
| `--space-6` | `24px` |
| `--space-8` | `32px` |
| `--space-10` | `40px` |
| `--space-12` | `48px` |
| `--space-16` | `64px` |
| `--space-20` | `80px` |
| `--space-24` | `96px` |
| `--type-label` | `11px` |
| `--type-small` | `13px` |
| `--type-body` | `16px` |
| `--type-intro` | `18px` |
| `--type-heading` | `clamp(44px, 4.1vw, 60px)` |
| `--type-plate` | `clamp(32px, 3.2vw, 46px)` |
| `--type-hero` | `clamp(76px, 8.7vw, 128px)` |
| `--content-width` | `1200px` |
| `--page-gutter` | `64px` |
| `--duration` | `180ms` |
| `--ease` | `cubic-bezier(.2,.65,.3,1)` |

## Typography

- Newsreader: display headings and wordmark; normal and italic, optical sizing enabled. Georgia is the fallback.
- Public Sans: body copy, labels, navigation, and diagram explanations; normal and italic. System sans-serif is the fallback.
- Variable WOFF2 files are served from `assets/fonts/`. Latin, Latin Extended, punctuation, and arrows are included. Font licenses are adjacent to the files.
- Headline line-height: 0.99; project title: 1.03; diagram title: 1.08; body: 1.65; project description: 1.75.
- Tracking: headline -0.045em, project heading -0.04em, diagram heading -0.035em, uppercase labels 0.1em.

## Layout

- Desktop: a 12-column grid with 24 px gutters, a 1200 px maximum content area, and 64 px minimum page margins. Section margins are 80?96 px; the header is 104 px tall.
- Project visuals span seven columns. Copy spans four with one separating column. The second project reverses the visual order on desktop.
- At 1100 px, page margins become 40 px and project copy uses five columns.
- At 760 px, project copy precedes the visual in a single column; page margins become 24 px. The header is 88 px tall.
- At 420 px, page margins become 20 px and hero type uses clamp(40px, 12.3vw, 60px).
- Diagrams remain legible within the page; horizontal scrolling is not part of the layout.

## Interaction

- Native anchors, details/summary, and radio inputs work with JavaScript disabled.
- Each observation radio shows one explanation. Native arrow keys move through the group; the chosen label has a rust border and a bottom rule. Focus has a separate 2 px outline offset by 4 px.
- Links have 44 px minimum target height; filled project links and disclosures have 48 px minimum height.
- Hover feedback uses 180 ms transitions and cubic-bezier(.2,.65,.3,1). Link arrows translate by 2 px. Transitions and smooth scrolling apply only when reduced motion is not requested.
- No automatic animation, scroll interception, or content entrance delay.

## Version history

- 2026-09-08 v1: Editorial redesign, self-hosted fonts, semantic palette, and native observation explorer.
- 2026-09-08 v1.1: Improved phone reading order and minimum type sizes; diagram lines now exceed 3:1 contrast. Removed the unused --space-32 token.
