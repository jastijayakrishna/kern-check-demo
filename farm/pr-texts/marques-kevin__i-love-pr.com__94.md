# feat: self-host Geist Sans, Mono, and Pixel Square

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
Fixes #93

Replace the Lexend + IBM Plex Mono Google Fonts CDN with a self-hosted Geist family (OFL). This is a Vite app, so fonts are loaded without `next/font` or the Next-only `geist` package.

## Mapping

- **Geist Sans** (`Geist Variable` via `@fontsource-variable/geist`) → body, buttons, settings, gallery, landing, tabs, labels, panel titles. `--font-sans`, `--font-heading`, and `--font-display` stay on Sans.
- **Geist Mono** (`Geist Mono Variable` via `@fontsource-variable/geist-mono`) → tokens, code, PAT, settings keys. `--font-mono`.
- **Geist Pixel Square** (vendored woff2 from [geist-font v1.7.2](https://github.com/vercel/geist-font/releases/tag/v1.7.2) + OFL) → chart data only: ticks, legends, tooltips, and StatCard numbers. New `--font-pixel` / `font-pixel`.

Pixel is not applied to tabs, toolbar, form labels, paragraphs, panel titles, buttons, empty states, or landing copy.

## Install

- Import Fontsource `wght.css` from `src/main.tsx`.
- Vendor only `GeistPixel-Square.woff2` and `OFL.txt` under `src/assets/fonts/`.
- Drop the Google Fonts `@import` in `src/index.css`.

## Wire-up

- `html` stays `font-sans`.
- StatCard value → `font-pixel`; label stays Sans.
- dither-kit ticks / legend / tooltip (and block-legend / reference-line) → `font-pixel`.
- Remaining Recharts charts (scatter + ranking charts) → ticks, legend, tooltip use `font-pixel`.
- PAT / settings token fields stay `font-mono`.

## Verification

`npm run check` is green locally. GitHub CI is green.

Computed styles on the demo `acme/widgets` workspace:

- Gallery heading → `Geist Variable`
- StatCard number → `Geist Pixel Square` (`font-pixel`)
- StatCard label / tabs → `Geist Variable`
- Dither chart ticks → `Geist Pixel Square`
- Settings token + ignored bots → `Geist Mono Variable`
- No `fonts.googleapis` / Lexend / IBM Plex in served or production CSS
- Production build ships Fontsource Geist/Mono woff2 subsets plus `GeistPixel-Square-*.woff2`

[Gallery Geist Sans](https://cursor.com/agents/bc-e9e34e32-2b49-44a8-812b-c2e872582519/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fgallery_geist_sans.webp)
[StatCard Pixel Square numbers](https://cursor.com/agents/bc-e9e34e32-2b49-44a8-812b-c2e872582519/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fdashboard_statcard_pixel.webp)
[Dither chart ticks and tooltip Pixel Square](https://cursor.com/agents/bc-e9e34e32-2b49-44a8-812b-c2e872582519/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fdither_chart_tick_tooltip_pixel.webp)
[Settings token and keys Geist Mono](https://cursor.com/agents/bc-e9e34e32-2b49-44a8-812b-c2e872582519/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fsettings_token_geist_mono.webp)
[geist_fonts_gallery_dashboard_settings.mp4](https://cursor.com/agents/bc-e9e34e32-2b49-44a8-812b-c2e872582519/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fgeist_fonts_gallery_dashboard_settings.mp4)


<sub>To show artifacts inline, <a href="https://cursor.com/dashboard/cloud-agents#my-pull-requests">enable</a> in settings.</sub>
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-e9e34e32-2b49-44a8-812b-c2e872582519?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-e9e34e32-2b49-44a8-812b-c2e872582519&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/
