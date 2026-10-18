# fix(app-router): preserve interception across middleware rewrites

## Summary

- preserve the internally matched source route when middleware hides dynamic segments from the browser URL
- distinguish browser-visible and middleware-matched target paths in interception proof metadata
- let navigation planning validate concrete dynamic route IDs without weakening stale-route safety
- strengthen the local Next.js parity fixture to start from the browser-visible rewritten URL

## Validation

- `vp test run tests/app-browser-interception-context.test.ts tests/app-page-render-identity.test.ts tests/navigation-planner.test.ts tests/app-rsc-route-matching.test.ts tests/app-browser-history-controller.test.ts` — 95 passed
- `CI=1 PLAYWRIGHT_PROJECT=app-router playwright test tests/e2e/app-router/interception-dynamic-segment-middleware.spec.ts --workers=1 --retries=0` — 4 passed
- targeted `vp check` on all changed files
- `vp run vinext#build`

The exact Next.js deploy-suite attempt stopped before deployment because the disposable worktree reuses a dependency symlink and `vp env` attempted to replace it non-interactively. No suite assertion was reached; CI should run the clean install/build path.

