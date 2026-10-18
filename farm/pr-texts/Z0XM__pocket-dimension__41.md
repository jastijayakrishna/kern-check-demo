# Add draggable grid tile layout for Zeo in-call video

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Implements Phase 1 of personal in-call tile layout for Zeo. The fixed CSS auto-grid is replaced with a **12-column square-cell canvas** powered by GridStack.js. Each user can arrange their own view independently.

## How it works

- **Grid geometry:** 12 columns (8 on narrow screens), square cells sized as `floor(stageWidth / cols)`, rows derived from available height above the control dock.
- **Edit mode:** Toggle via the layout button in the control bar or `L`. Grid lines appear; tiles become draggable/resizable.
- **Locked 16:9 ratio:** Resize snaps to preset footprints only — S (6×4), M (9×5), L (11×6), XL (12×7) grid cells.
- **Persistence:** Layout saved to `localStorage` per room slug (`zeo:call-layout:{slug}`) in grid units.
- **Auto-placement:** New participants get sensible default positions when no saved layout exists.

## Key files

- `apps/zeo/src/lib/call/grid/*` — metrics, tile sizes, layout engine, storage, auto-place
- `apps/zeo/src/lib/components/call/GridCanvas.svelte` — GridStack host + participant tiles
- `ControlBar.svelte` — layout edit toggle
- `CallExperience.svelte` — layout state + persistence

## Not in scope (Phase 2+)

- Screen-share layout integration
- Reset layout action
- Layout sync across participants
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-fca786d8-4aa9-4229-b9da-13cdd2339e84"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-fca786d8-4aa9-4229-b9da-13cdd2339e84"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>


