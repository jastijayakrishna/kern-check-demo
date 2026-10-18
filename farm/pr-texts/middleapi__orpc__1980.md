# chore(content): scroll long twoslash lines instead of overflowing the code block

Long lines in twoslash code blocks ran past the code frame on desktop (see the Pino integration page, where the option comments spilled out of the block). Twoslash code now scrolls horizontally inside its frame like every other block, at every viewport width, and hover popups keep working on top of the scroller.

## Fixes

- Twoslash blocks scroll sideways instead of overflowing. Blume keeps them `overflow: visible` so its absolutely positioned popups can escape, and only wraps lines below 640px; the popups are now `position: fixed` at every width (previously only on mobile), so the inner code element can be the scroller.
- Hover popups open under their token with the hover bridge at all widths, follow the token when the page or the code scrolls with a mouse, and are dismissed on touch scroll as before. `twoslash-mobile.ts` is renamed to `twoslash-popups.ts` since it now runs everywhere; the desktop-only CSS placement, `::before` bridge, and flip rules are gone.
- Two completion-list examples (client-side, contract implementation) gain the spacer comment lines the other examples already use, so their lists stay inside the scroller instead of being clipped.

## Testing

- Dev server at 1400×900, 768×1024, and 375×812: code scrolls within its frame with no page overflow on the Pino page; popup placement, scroll following, tap pin, touch-scroll dismissal, and outside-tap close verified; no console or server errors.
- All five completion-list examples measured against their code box at mobile and desktop widths; all fit.
- `pnpm eslint` clean on the changed files.
