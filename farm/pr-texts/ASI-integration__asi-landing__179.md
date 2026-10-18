# Authenticate multi-repository baseline SHA lookup

## What changed

- use the optional server-side `GITHUB_TOKEN` for allowlisted baseline SHA requests
- keep unauthenticated public-repository compatibility when the token is absent
- add focused regression coverage for landing and `asi-os-runtime`, token placement, malformed SHAs, and GitHub non-OK responses

## Root cause

`resolveAllowlistedBaselineSha()` called GitHub's commit endpoint without the authorization header already used by the other owner-console GitHub control-center calls. Fine-grained PAT access to `asi-os-runtime` therefore was not applied to baseline resolution.

## Safety and compatibility

- repository and branch still come exclusively from the server allowlist
- token is sent only in the `Authorization` header and is never placed in the URL or error payload
- timeout, `cache: no-store`, exact 40-character SHA validation, and fail-closed errors are unchanged
- no production data, database, DNS, payments, messages, merge, or deploy

## Validation

- `npx.cmd vitest run src/lib/development/__tests__/baseline-sha.test.ts` — 5 passed
- `npx.cmd vitest run src/lib/development/__tests__/task-service.test.ts` — 31 passed
- `npm.cmd run typecheck` — passed
- `npx.cmd eslint src/lib/development/baseline-sha.ts src/lib/development/__tests__/baseline-sha.test.ts` — passed
- `git diff --check` — passed

## Rollback

Revert commit `f2e27d852bb41b6da6c23eac3fb2e787741105e2`; no data cleanup is required.
