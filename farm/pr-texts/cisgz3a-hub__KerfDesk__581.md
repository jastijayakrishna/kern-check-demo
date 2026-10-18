# fix(cnc): re-land the thin-detail V-carve stage with the #575 coverage corrections (ADR-279 Amendment)

Re-lands the ADR-279 thin-detail V-carve stage (#572, reverted by #575), folding in the #577 refinements and correcting every finding from the revert review. See the ADR-279 Amendment in DECISIONS.md for the full response; summary:

1. **Depth-clamp coverage (the headline defect)** - ring pitch is now `min(Detail, 2*maxDepth*tan(theta/2))`, fine pitch `min(0.05, same)`, so clamped footprints always overlap. The reviewer's exact probe (2x2 mm, 90 deg bit, Detail 0.5, max depth 0.05) is a pinned perceptual regression test: it measured **13.8 % coverage before the fix and >= 85 % after**, and proves nothing cuts deeper than the clamp.
2. **Tapering-tail residual** - fixed by the exact-residual computation (from #577's `fix(cnc): report sub-pitch tails attached to rescued slivers`), folded in here.
3. **Difference precision** - explicit `DIFFERENCE_PRECISION_DECIMALS = 3` passed to clipper (default was 2).
4. **Byte-identity overclaim** - corrected in the ADR amendment: sharp-corner wedge passes change wide sharp-cornered outputs by design; only wedge-free wide artwork is byte-identical.
5. **Emitter revision** - bumped to `adr-279-vcarve-thin-detail-v2` (with its pinning test).

Also included from #577 (which this PR supersedes): sliver-major detail ordering, the exact residual above, and the layer-panel thin-detail note.

## Verification

- 119 test files / 739 tests across `src/core/cnc`, `design-carve`, `relief`, `ui/layers`, `io/gcode`, geometry and the advisory suite: all pass (two 5 s-timeout flakes under a fully contended parallel run pass solo; the new grid-computing probe now carries the sibling suites' 60 s allowance).
- `pnpm typecheck`, scoped ESLint, Prettier, and the ADR number gate (227 decisions + 2 amendments) all green.
- NOT verified: physical cutting; the junction under-cut blend remains a documented limitation with its sim-prerequisite plan.

Snapshot change acknowledged: `vcarve-thin-perceptual.test.ts.snap` returns with this re-land (new file restored from #572; byte-identical to the reviewed one). The single-square `vcarve-perceptual.test.ts.snap` is untouched.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
