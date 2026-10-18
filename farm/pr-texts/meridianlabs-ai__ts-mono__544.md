# Consolidate Scout score value rendering

## Summary

- add Scout's fixed-preview `expandable={false}` behavior and array-compatible `className` support to the shared transcript `ScoreValue`
- migrate both Scout consumers to `@tsmono/inspect-components/transcript`
- delete Scout's duplicate `ScoreValue` implementation
- cover default expandable and fixed non-expandable object-score behavior with shared component tests

## Why

Scout and `@tsmono/inspect-components` carried near-identical `ScoreValue` implementations. Scout's copy had evolved two small API additions, so shared behavior changes could drift between the apps.

## Validation

- `pnpm -C packages/inspect-components test` — 918 passed, 2 skipped
- `pnpm -C packages/inspect-components lint`
- `pnpm -C packages/inspect-components typecheck`
- `pnpm -C apps/scout test` — 210 passed
- `pnpm -C apps/scout lint`
- `pnpm -C apps/scout typecheck`
- `pnpm -C apps/scout build:app`

## Manual QA

Tested a local Scout Vite page using the real shared `ScoreValue` and Scout `ScoreColumn` under Scout's theme and component providers:

- simple score rendered inline as `pass`
- expandable object score initially showed 2 of 5 rows and a `3 more...` control
- clicking `3 more...` showed all 5 rows and a `less...` control; clicking `less...` restored the 2-row preview
- Scout's non-expandable score column showed exactly 3 of 5 rows plus `All scores (5)`, with no internal more/less toggle
- no browser console errors occurred during the QA page checks

The temporary QA harness was removed before committing.
