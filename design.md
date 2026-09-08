# Portfolio design

## Current direction

The user requested simplicity and more projects. Use a compact, single-column page with the person's name, a short introduction, and text project entries.

## Tokens

| Token | Value |
| --- | --- |
| `--background` | `#ffffff` |
| `--text` | `#242424` |
| `--muted` | `#626262` |
| `--line` | `#e5e5e5` |
| `--note` | `#f6f6f6` |
| `--font` | `-apple-system, BlinkMacSystemFont, "Segoe UI", Arial, sans-serif` |
| `--width` | `800px` |
| `--gutter` | `24px`, `20px` below 600 px |

## Layout and type

- Name: 32 px / 1.25, weight 600; 28 px on phones.
- Project title: 19 px / 1.4, weight 600.
- Descriptions: 15 px / 1.65; metadata 12 px / 1.5; links 13 px.
- Spacing: 4, 8, 12, 16, 20, 24, 32, 40, 64 px.
- Header padding: 64 px top / 40 px bottom; 40 px / 32 px on phones.
- Project rows: 24 px vertical padding; 20 px on phones. A light rule separates entries.
- At 600 px, project metadata moves below the title.

## Interaction

- Plain underlined links; native disclosures for existing research details.
- Visible 2 px focus outline with 4 px offset; keyboard skip link.
- No animation or JavaScript. System fonts require no font downloads.
- Text contrast floor: 4.5:1 on the actual background.

## Version history

- 2026-09-08 v1: Editorial redesign, self-hosted fonts, semantic palette, and native observation explorer.
- 2026-09-08 v1.1: Improved phone reading order and minimum type sizes; diagram lines now exceed 3:1 contrast. Removed the unused --space-32 token.
- 2026-09-08 v1.2: Marked the overall visual direction as rejected following direct user feedback. Existing tokens document the implementation, not accepted preferences.

- 2026-09-08 v2: Replaced the rejected editorial style with the simple project list explicitly requested by the user. Superseded the previous type, color, spacing, and interaction tokens.
