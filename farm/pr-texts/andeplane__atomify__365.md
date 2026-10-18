# Full TypeScript audit: FILES_REPORT.md + fix every identified bug

## Summary

Audited all 91 `.ts`/`.tsx` files in `src/` (17,784 lines), scoring each on code quality, bugs, test coverage, and pattern adherence. The full per-file writeup is in `FILES_REPORT.md`. Every problem marked 🔴 ("fixed in this PR") in that report is fixed here, in atomic commits — nothing marked 🟡 (deferred, needs a design decision) or ⚪ (nit) was touched.

Highlights:
- **Real bugs**: `addParticleStyle` silently turning `particleStyles` from an array into a plain object; `run()`/`newSimulation()` crashing with an unhandled TypeError when a simulation's input script doesn't match any file; a Rules-of-Hooks violation in `ColorModifierSettings` that can unmount the tree; a leaked self-perpetuating `setTimeout` poll loop in `AutoStartSimulation`; a Dygraph instance leak in `Figure`; `window.onkeydown` clobbering; idle simulations mislabeled "Minimization"; a broken survey form in `RunInCloud` (5 fields sharing one form name, defaults that don't match the displayed UI).
- **Duplication removed**: the three sync-modifier classes (~90% copy-pasted data1D logic) now share one helper; `SimulationSummaryExpanded` (476 lines, 90% identical to `SimulationSummaryContent`) is now a 19-line wrapper, which also restores a "show simulation box" row it had silently lost to drift.
- **A test that couldn't fail**: `app.test.ts`'s embedded-mode test rebuilt its expectation inline instead of exercising `app.ts`; now uses `vi.resetModules()`/`vi.doMock()` to actually run the module's init code (verified by temporarily inverting the logic under test and confirming it now fails).

## Test plan
- [x] `tsc --noEmit` clean
- [x] `vitest run` — 406/406 passing (26 test files), including updated tests for the array/object bug and the modifier refactor
- [x] `npm run build` succeeds
- [x] Verified the previously-tautological `app.test.ts` test actually fails when the logic it tests is broken

🤖 Generated with [Claude Code](https://claude.com/claude-code)
