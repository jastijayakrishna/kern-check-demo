# Builder: free placement (red-flag invalid) + move parts between decks

Second builder PR (independent of #10). Makes placement non-blocking so users can rearrange freely, and lets a placed part change decks.

## What changed
- **Place / rotate / move never block.** A part dropped or rotated into an invalid spot (overlap / no socket / off-grid) now lands anyway and **glows red** in the scene, instead of the action being silently rejected. This fixes the old "can't rotate 180° because the rotated footprint doesn't currently fit → delete, re-add, rotate, replace" dance, and enables the stage-aside workflow (park a part somewhere temporarily, free up the spot, then move it back).
- **Pulsing inspector banner** lists every invalid part + the reason ("no connection to the rig", "overlaps …", etc). Click a row to select that part and jump to its deck.
- **Move parts between decks:** changing the deck level (rail ▲/▼ or R/F) with a placed part *selected* now carries that part to the new deck, instead of only changing the view level.

## Implementation
- `invalidPlacements(state)` in `builderCore.js` → `Map<plId, reason>`.
- `BuilderScene.jsx`: new `invalidIds` prop; invalid parts get a red emissive tint (`partMaterials`).
- `Builder.jsx`: `place`/`rotate`/`movePlacement` drop their reject/revert paths; new `changeLevel()` carries a selected part; pulsing warning banner.
- `builder.css`: warning + pulse styles.

## Verification
Ran locally — injecting a floating part correctly flags **"S.Trs Auxiliary Corridor — no connection to the rig"** in the pulsing banner and red-tints it; no code-level console errors. The owner couldn't interactively click-test yet, so give the place/rotate/move flow a poke before merging.

Visual chosen: static red 3D part + pulsing inspector banner (no continuous render loop added to the scene — a true per-frame 3D pulse can come later, ideally with the builder-perf pass).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
