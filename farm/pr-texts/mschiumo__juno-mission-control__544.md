# fix: visibly fade paused habits + styled paused tooltip

## What

The pause-a-habit feature (#529) shipped with a fade that never rendered: the dnd-kit inline style set `opacity: 1` on every non-dragging card, which silently overrides the class-based `opacity-50` paused fade (and the `opacity-60` disabled fade). Paused cards showed the badge but looked identical to active ones.

## Changes

- **Fix the fade**: inline opacity is now only set while dragging, so the class-based fades actually apply.
- **Clearer inert styling**: paused card content fades to 40% *and* goes grayscale (mutes the emoji and streak colors), with a dashed border and no orange hover accent.
- **Stylized tooltip** (custom, not the browser `title`): hovering a paused card shows a styled tooltip — orange "Habit paused" header with pause icon, explanation that the habit won't count toward progress/stats/streaks, and how to resume.
- **Mobile**: no hover on touch — the "paused" badge is now a tappable button (with pause glyph) that toggles the same tooltip; tapping anywhere else dismisses it. Tooltip is anchored to the card's full width so it can't clip horizontally in the scroll list.
- The fade lives on the inner row, not the card container, so the tooltip and the ⋯ actions strip (with the Resume button) render at full opacity.

## Verification

Verified on a local prod-mode dev server with mocked habit data via headless Chrome at 800px and 375px: fade + grayscale clearly distinguish the paused card, tooltip renders correctly at both widths, tap-toggle and outside-tap dismiss confirmed. `npm run build` passes.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
