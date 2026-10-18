# fix(battle): sync latest stage UI and dungeon runtime fixes

## What changed

- Applied the pending Battle UI fixes on top of the latest `master`.
- Widened combat camera framing without changing gameplay hitboxes.
- Reset the dungeon battle runtime/UI reference so dead monster sprites do not persist across stages.
- Reduced the stage objective HUD footprint.
- Preserved the corrected Survival/Chase/Time Attack objective clock and objective HUD behavior.
- Updated the Adventure catalog regression expectation to match the latest `master` config where stage 1-8 is `mini-boss`.

## Validation

- TypeScript frontend: passed
- Oxlint: passed
- Tests: 108 files / 910 tests passed
- Production build: passed
- Bundle-size check: passed

The local environment does not have Deno installed, so the Supabase Edge Function typecheck could not run locally; GitHub Actions should perform that check on this PR.

No Backend/Supabase source changes were introduced by this PR, and `master` was not modified directly.
