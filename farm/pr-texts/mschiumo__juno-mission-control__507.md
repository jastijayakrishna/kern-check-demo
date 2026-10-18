# feat: redesign Active Trades trade cards per design handoff

## Summary
Rebuilds the Active Trades panel in Trade Management to the design handoff spec (`Trade cards redesign.zip`):

- **Header**: sparkline logo tile, title + mono position count, collapse chevron, restyled search / Select All / Refresh (spinning ↻ while loading); bulk Move-to-Potential and Delete keep working
- **Cards**: identity row (select box / mono ticker / LONG-SHORT triangle badge / timestamp), bordered 3×2 hairline metric grid (Entry · Stop · Target / Profit · Risk · Shares) with the entry→target % as a pill, control row (Order Placed toggle + Edit / Close Trade / Delete), always-editable notes field with ~500ms debounced autosave
- **Fonts**: IBM Plex Sans/Mono via the existing `--font-plex-*` next/font variables
- **Target %** now reads as gain toward target (shorts flip sign, per the handoff's data) — applied consistently on cards, closed positions, and the Trading Mode strip
- All prior behavior preserved: inline cell editing, multi-select, drag-and-drop reorder (incl. touch), search, collapse, order-placed persistence + group reorder

## Hardening (from multi-agent review)
- Notes drafts retire on blur; saves serialized per trade (no out-of-order PUT races, no stale shadowing of Edit-modal saves)
- Notes field is a 1-row textarea (preserves multi-line notes), shields the card's long-press touch drag, and disables card dragging while focused so drag-to-select-text works
- Notes autosave no longer triggers self/strip refetch loops
- Order-placed persistence gained a hydration guard (initial empty map could clobber stored flags on remount)
- Metric grid falls back to 2 columns under 480px; skeleton height matches real cards; checkbox-style controls expose `role`/`aria-checked`

## Test plan
- `tsc --noEmit` and eslint clean (no new issues)
- Verified against a mock-data harness in headless Chrome: layout matches the prototype at desktop width, no horizontal overflow at 375px, and interactions exercised end-to-end (select / select-all, order-placed toggle + localStorage persistence + group reorder, collapse, search filter, inline edit open/cancel, notes debounce = exactly one serialized PUT with newlines preserved, draft retired on blur, card `draggable` off while notes focused)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
