# Builder: hull picker on top, Essentials grouping, Disabled category

Restructures the builder's left parts-locker so it reads top-to-bottom in build order.

## What changed
- **① Choose a hull** — chassis selection moves from the right-panel dropdown to an image-tile picker at the top of the left panel (nothing can be placed without a hull). Right panel keeps a read-only chassis readout. Switching hull still confirms before clearing the build.
- **② Essentials** — a new always-open group listing the parts required for a valid trampler (Reactor / Steering / Captain / Entrance), grouped by category with dividers, so mandatory vs optional is obvious. Essential parts are moved out of their normal categories (no duplication).
- **③** the remaining optional categories as before (collapsible).
- **④ Disabled** — surfaces the 4 parts the game ships but flags disabled (`DISABLED_PARTS` in builderCore), badged "SOON", placeable for preview.

## Scope / notes
- Only `Builder.jsx`, `builder.css`, `builderCore.js` touched. No data or 3D-scene changes.
- Verified it compiles and renders on local `:3000` via a headless browser (hull picker = 17 tiles, Essentials = 21 parts, Disabled = 4, chassis readout present, no code-level console errors). Not yet interactively click-tested.
- First of a few builder PRs — behaviour fixes (move-between-levels, allow-invalid-placement) and bigger features (randomiser, naming, sand-dune ground) will follow as separate PRs.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
