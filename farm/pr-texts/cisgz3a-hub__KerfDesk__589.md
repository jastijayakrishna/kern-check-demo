# fix(cnc): re-land the thin-detail stage with the junction blend and the #584 corrections (ADR-280)

Third landing of the thin-detail V-carve stage: restores the #584-reverted #581, adds the **junction blend** (ADR-280 Amendment 2), and answers **every #584 finding** (ADR-280 Amendment 3). The decision renumbered ADR-279 → **ADR-280** because #578 claimed 279 while this was off main.

## The #584 findings, answered

1. **Coverage floor** — ring pitch floors at 0.002 mm (two Clipper quanta, distinct insets guaranteed). The 1° / 0.05 mm case cannot silently cap any more: it sets the new `passLimited` flag.
2. **Honest budgets** — `buildOffsetLadder` now reports `capped` (budget exhausted with interior remaining, previously indistinguishable from completion). Coarse-capped, fine-capped and floor-degraded all surface through the generalized layer-named `pass-limit` Job Review advisory — informs, never refuses (rule 7).
3. **Pitch bound corrected further** — the strengthened probe caught that even the corrected law left ~4 % interior stripes along mitered diagonals (spacing grows ×√2–×2 at corners); the pitch is now **one clamp-footprint radius**, `min(Detail, maxDepth·tan(θ/2))`.
4. **Probe strengthened** — the #575 probe now excludes only the sub-footprint edge band and requires **≥ 99 % interior coverage outright** (stripes fail it), clamp bound unchanged; plus the exact 1° regression test and the advisory-suite pin.

## The junction blend (Amendment 2)

Detail rings are now `path3d` passes whose vertices carry `z = −min(distToSourceBoundary/tan(θ/2), maxDepth)` — the analytic groove law — with adaptive segment subdivision (0.02 mm Z tolerance) so junction crossings gain vertices at the depth knee while straight sides stay two vertices. The under-cut seams at stroke-width transitions (the dark notches in the maintainer's "Safe" screenshot) are gone: the Drive-tail perceptual window now starts **0.05 mm from the junction cut-line** (previously excluded δ + 0.5 mm) and holds the same ≤ 0.15 mm bound — it measured 0.225 mm before the blend. Ramp-configured layers keep constant pitch-depth detail rings (the ADR-278 planner is one-depth-per-ring by design). Prerequisite #586 (vertex-exact simulator) is already on main and is the measuring instrument here.

## Verification

- 103 test files / 618 tests green across `src/core/cnc`, `sim`, `geometry`, `io/gcode`, and the advisory + panel-note suites; `pnpm typecheck`, ESLint and repo-wide Prettier clean; ADR gate green (228 decisions + 4 amendments).
- Failing-first at every step: the junction window (0.225 mm red → green), the 1° probe (silent → `passLimited`), the capped ladder, the diagonal-stripe interior assertion (95.95 % red → ≥ 99 %).
- `EMITTER_REVISION` = `adr-280-vcarve-junction-blend-v3` (output shaping changed).
- NOT verified: physical cutting; ramp-configured layers intentionally retain the pre-blend seam; the 3D viewer still shades path3d by endpoint span.

Snapshot change acknowledged: detail rings emit G1 XYZ moves and test titles renumbered to ADR-280, so the thin-stroke perceptual snapshot regenerated.

🤖 Generated with [Claude Code](https://claude.com/claude-code)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Improved V-carve support for thin strokes, narrow gaps, corner details, and hairline artwork.
  * Added adaptive carving depths and improved detail coverage while respecting configured depth limits.
  * Preserved carving order across regions for more consistent toolpaths.
  * Added in-app advisories for uncarvable thin details, geometry issues, and carving limits.

* **Bug Fixes**
  * Improved handling and reporting of offset and polygon-processing failures.
  * Clarified warnings when detail or pass limits prevent complete carving.

* **Documentation**
  * Added design documentation for thin-detail V-carving behavior and known hardware considerations.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
