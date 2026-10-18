# fix(moves): recognize golden bar contract exhibits

## Summary
- fixes the golden-bar exhibit detector so required visual/table phrases from the deliverable contract are recognized when rendered as section titles plus SVGs/tables
- adds a regression test matching the live P0 pattern: value tree, stakeholder map, KPI scorecard, scope boundary, and proceed/hold/stop gate
- updates the Moves P0 release record with the live HTTP 422 golden-bar diagnosis

## Live context
After #3892 deployed to app.abarva.ai at revision mf0ae3083, the Meridian proof Move no longer hit the prior dv.created_at 500. P0 generation reached quality evaluation and returned HTTP 422 golden_bar_failed because the detector missed exhibits that were present as titled sections/tables.

## Validation
- npx jest src/lib/deliverables/__tests__/golden-bar.test.ts --runInBand
- npx eslint src/lib/deliverables/golden-bar.ts src/lib/deliverables/__tests__/golden-bar.test.ts
- npm run release:check -- --base origin/main --head HEAD
- npm run audit:control-plane-purity:check

Note: an ad hoc full npx tsc --noEmit attempt was stopped after ~19 minutes while still CPU-active/no output. The canonical GitHub Typecheck + reasoning-layer check should be used as the type gate for this PR.
