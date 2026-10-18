# Use shared LoadingBar in Inspect

## Summary

- replace all four Inspect `ActivityBar` consumers with `@tsmono/react`'s shared `LoadingBar`
- delete Inspect's duplicate component and stylesheet
- remove the shared component's incorrect fixed `aria-valuenow="25"` so its animated state is exposed as indeterminate progress
- add unit coverage for animated and idle states and update the existing loading-state end-to-end test terminology

The removed determinate `progress` API had no consumers in the repository.

## Validation

- `pnpm --filter @tsmono/react test` — 221 tests passed
- `pnpm --filter @tsmono/react lint`
- `pnpm --filter @tsmono/react typecheck`
- `pnpm --filter @meridianlabs/log-viewer test` — 1,141 tests passed
- `pnpm --filter @meridianlabs/log-viewer lint`
- `pnpm --filter @meridianlabs/log-viewer typecheck`
- `pnpm --filter @meridianlabs/log-viewer build`
- `pnpm --filter @meridianlabs/log-viewer e2e -- error-state.spec.ts` — the package runner executed all 102 Inspect Playwright tests; all passed

## Manual browser QA

Tested the Inspect app in the in-app browser at 1280×720 against delayed and immediate local API responses.

- confirmed the active bar stays full-width and 1px tall beneath the navbar
- confirmed the animated segment remains 5% wide, blue (`rgb(59, 130, 246)`), and uses the same 2-second left-to-right animation
- confirmed `aria-valuenow` is absent during indeterminate loading
- confirmed the animated child disappears after loading completes, with no layout shift

