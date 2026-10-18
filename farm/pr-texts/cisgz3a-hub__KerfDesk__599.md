# feat(ui): one design language for the operations rail (ADR-281)

Re-lands the rail styling from #588 (reverted by #594) with that review''s blockers fixed. Scope is honest: **rail styling only**.

## What #594 blocked, and what changed

| Blocker | Fix in this PR |
| --- | --- |
| A rail-only label-width rule leaked globally into nine non-rail dialogs | `.lf-field-label--sm` stays at its shared 90px. The rail''s 100px is now `.lf-pane-form .lf-field-label--sm` — scoped by construction, so no dialog using `kit/Field`''s default can move. |
| Governing export-extension documentation remained stale | No docs in this PR. `CONTRIBUTING.md`, `docs/**`, `src/platform/types.ts`, `MachineSettingsPanel*`, `export-execution-artifact`, `export-grbl-settings-backup` are all **excluded** — they were pre-existing branch work, not this change. |
| 38 files mixing UI, Advanced behavior, export runtime, and docs under a styling-only claim | 23 files, all rail styling + the ADR. The Advanced-toggle behavior is **not** here — it already landed independently on main in #571. |

## Change

- `tokens.css`: `.lf-pane-form` scope paints native buttons/inputs/selects with the chrome look; `.lf-section` disclosure chrome (hairline, rotating chevron, right-aligned badge); `.lf-subhead`; `.lf-hint`; `.lf-btn--sm`.
- New `kit/RailSection` (label / badge / **required** hint / open) adopted by probe, Manage bits, bit catalog, machine catalog, machine profiles, tiling, spoilboard, feeds calculator. The hint is required because the a11y hover-help contract scans for a literal `title`.
- Field grammar: 100px label column, 84px numeric inputs; X/Y pairs share one row (`Stock size (mm)`, `Stock origin (mm)`, `Park position (mm)`) with per-input aria-labels unchanged.
- Material & Bit groups as STOCK / SPINDLE / MOTION.

`SelectedShapeGeometryFields` gets **styling only** here — its `reconcileKey`/keyed-remount fix and the `RotatedFootprintNote` feature now on main are preserved untouched.

## Verification

- `tsc --noEmit` clean; eslint clean over `theme/kit/layers/machine`; `prettier --check src/ui` and `DECISIONS.md` clean; ADR gate green (ADR-281).
- `vitest run src/ui/machine src/ui/layers src/ui/a11y src/ui/theme`: **51 files / 266 tests pass**, including the narrow-rail select-shrink contract and the hover-help contract.
- Perceptual: before/after screenshots at the real 300px rail width in a dev server.
- NOT verified: full suite on this branch (CI will run it), hardware, E2E, dialog screenshots — though the scoped selector is exactly what keeps dialogs unchanged.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
