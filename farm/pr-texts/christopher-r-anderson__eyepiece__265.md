# fix(ui): keep the brand mark on home and center the header row

## What

- The brand now renders mark + wordmark on every page, including home. Previously home hid the telescope mark (wordmark-only), which read as "the logo disappears on home" — the distinction is now: the wordmark yields to the header search field at narrow widths, and home keeps it at all widths since it has no header search.
- The header row is vertically centered: `paddingBlock` was `16px 10px`, which offset the flex content box 3px below the bar's true center. Now symmetric `13px`, keeping the bar height at ~62–66px.
- Wordmark hardening, matching its sibling mark:
  - `?no-inline` on the import — the SVG is referenced via a `#group` fragment, which breaks silently if Vite inlines the asset as a data URI. It survived only because the file (7.1KB) exceeds the 4KB inline limit.
  - intrinsic `width`/`height` attributes instead of `height` + `width: auto` CSS, so it no longer depends on intrinsic-ratio sizing of an SVG flex item.

## Verified

- prettier, eslint, tsc, unit suite all green.
- Checked in the browser (dev server): home and album pages, mark + wordmark on both, `mdDown:d_none` present only where the search field renders.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
