# Fix Owner Console launchable degraded acceptance

## What changed

- align the Owner Console acceptance readiness gate with the existing launch contract
- allow schema-valid `degraded` readiness when `canLaunch` is true and every component is explicitly non-blocking
- keep blocked, contradictory, or malformed component evidence fail-closed
- document recoverable checkout drift as a launchable acceptance precondition

## Why

Issue #132 confirmed that clean Runtime checkouts with recoverable baseline drift are intentionally launchable because baseline recovery runs immediately before execution. The acceptance harness incorrectly required exact `overallState === "ready"` and blocked that supported path.

## Validation

- `npm.cmd exec -- vitest run src/app/api/dashboard/development/__tests__/routes.test.ts -t "owner console autonomous acceptance command"` — 9 passed, 28 skipped
- `npm.cmd exec -- eslint scripts/owner-console-runtime-acceptance.mjs src/app/api/dashboard/development/__tests__/routes.test.ts` — PASS
- `npm.cmd run typecheck` — PASS
- `node --check scripts/owner-console-runtime-acceptance.mjs` — PASS
- `git diff --check` and staged diff check — PASS

## Safety and rollback

- no live E2E was run
- no merge, deploy, production configuration, Runtime VM, secrets, data, DNS, or repository settings were changed
- one-draft-PR/one-proof-file, no-merge, no-deploy, and secret-safety behavior is unchanged
- rollback: revert this commit to restore the exact-ready-only acceptance gate

Closes no issue; contributes the narrow acceptance-harness repair requested in #132.

