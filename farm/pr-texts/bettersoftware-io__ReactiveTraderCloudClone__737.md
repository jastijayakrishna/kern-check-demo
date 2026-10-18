# fix(layout-dockview): dispose persists only a layout a user arranged

> [!WARNING]
> **This is a PARTIAL fix for the dockview 1px sash, and a green `visual.yml` after it merges does NOT mean the sash is fixed.**
>
> The sash divergence has **two carriers**, and this PR closes only one:
>
> | carrier | where it bites | status |
> |---|---|---|
> | **B** — StrictMode / remount dispose-flush persists a pre-settle blob | dev builds, the visual host (where goldens are shot), `key={activeTab}` remounts | ✅ **closed here** |
> | **A** — single mount: dockview's ResizeObserver proportionally rescales a 981px seed to 980px | **production builds** with an eager mount | ❌ **still open** |
>
> StrictMode's double mount happens only in development. **In a production build carrier B never exists, so A is the whole bug.** The goldens are captured under StrictMode, so this PR can turn all six scenarios green while a production user on an eager mount still gets the 1px sash. Measured, not inferred: with StrictMode switched off in the host, a single eager mount on the unfixed engine still renders 637/329.
>
> **The default-engine re-flip stays blocked on A.** Main is unaffected today: React's dockview engine is lazily imported, so it constructs at the settled size.

Fixes one of the two carriers of the dockview 1px sash divergence that reddened main's post-merge `visual.yml` after the default flip (#725, reverted in #731). **Does not re-flip the default**, and does not touch either bridge.

## The bug, measured

On the visual host (`app/fx-dockview`, React dockview mounted eagerly), StrictMode builds the engine twice:

```
engine #1  constructs at 981px (chrome above not yet settled)   → seed @ 981
           StrictMode dispose → unconditional flush writes a blob, grid h=981
engine #2  constructs at 980px — the CORRECT size — but restores #1's blob
           → dockview rescales 981 → 980 and loses a pixel on the tiles/blotter sash
           → 637/329, where the goldens and Solid have 638/328
```

The surviving engine was built at the right size. What broke it was `dispose()` persisting an engine nobody had touched as if it were a user's saved layout.

## The fix

`dispose()` now flushes only once a pointer has gone down inside the container since construction.

- Layer 3 persists **arrangement**: sash drags, DnD, restacks, and the maximize/collapse/pop-out buttons, all of which live inside the container.
- Everything else that mutates the grid before a user touches it is rebuilt on the next construction: pins, the dynamic-panel reconcile, a bridge's replays, settle-time resizes.
- A content comparison can't tell a replay from a click, because both change the grid identically. Origin can.

The flush still goes through `onLayoutChange`, so a bridge's reset-suppression guard still works for a dirty engine.

## Verification

- **Probe, committed engine, eager React mount, StrictMode, fresh host:** geometry in all six previously-red scenarios (`fx`, `fx-collapsed`, `fx-rail-collapsed`, `fx-rail-maximized`, `fx-closed`, `fx-docked-panel`) is **identical to main's render in every group**, rails included.
- **The carrier reproduces in jsdom** as a package test: construct at 981 → dispose → construct at 980 gives the blotter **387 vs 386** on the unfixed engine.
- **Mutation-checked:** against the original engine exactly the three new tests fail; the other 91 pass.
- `layout-dockview` 137/137 · React unit 474/474 · React contract coverage 1172/1172 · Solid unit 535/535 · Solid contract coverage 1139/1139 · typecheck 45/45 · biome + eslint clean.

## Tests that changed, and why

- **Instrumentation made explicit.** Tests that read a blob via dispose's old unconditional flush now say so through `persistArranged` / `touchContainer`.
- **Vacuous passes closed structurally.** The test tracker's `pins()` / `blob()` returned `[]` / `""` when nothing was saved, so "no pins" passed with no save at all. They now **throw**. That exposed three vacuous passes, one of which — *"leaves a static-only blob with no dynamicPanels exactly 
