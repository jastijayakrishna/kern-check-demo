# feat: Fase 4 redeploy — auth-sdk WebOxyProvider on SessionClient, FedCM removed from client auth (fixes console sign-in loop)

## Summary

This reapplies the reverted Fase 4 cross-domain session sync work (#490 was reverted in #491) with two additional fixes cherry-picked on top, and fixes the root cause of why #490 had to be reverted in the first place.

- **Reapplies #490** (revert-of-revert of `ec6bb4be`) — the verified Fase 4 file-overlay: `WebOxyProvider` (`@oxyhq/auth`) rebuilt on `SessionClient` for cross-domain session sync, preserving prior work from #459 / #462 / #473.
- **+ `b124d3dc`** — `useDeviceAccounts` (`@oxyhq/services`) now sources device accounts from `SessionClient` instead of `oxy_rt` `refreshAllSessions`, so `ProfileMenu` correctly lists all switchable device accounts.
- **+ `4fb25427`** — FedCM removed from the client auth path entirely. FedCM is a Chrome-only API; it's taken out of cold-boot, refresh, and UI. The `/auth/silent` iframe + `/sso` top-level bounce + password + device-flow sign-in paths are kept and now carry cross-browser cold boot on their own.

### Root cause of the #491 revert (now fixed)

Console's `AuthGuard` was re-invoking `signIn()` in a loop because `WebOxyProvider.signIn` set `isLoading(false)` **after** initiating the redirect. Each repeated `window.location.assign()` call aborted the in-flight navigation, so the guard observed `isLoading === false` + still-unauthenticated and fired `signIn()` again — a ~200ms loop that never let the redirect complete.

Fix: the loading state now stays set after redirect initiation, and a `signingInRef` mutex prevents re-entrant `signIn()` calls while a redirect is in flight. Covered by a new regression test: `packages/auth-sdk/__tests__/WebOxyProvider.signInLoop.test.tsx`.

## Verification (run in isolated worktree before this PR)

- `@oxyhq/core` tests: 764/764 passing
- `@oxyhq/services` tests: 245/245 passing
- `@oxyhq/auth` (auth-sdk) tests: 93/93 passing
- `tsc --noEmit` clean across core / auth-sdk / services (0 errors × 3)
- All builds green, including `oxy-console` (Vite) and `accounts` (Expo export)
- `bun install --frozen-lockfile` passes (lockfile gate)

No `packages/api` changes in this diff — no backend/ECS deploy expected from this PR; Cloudflare Pages deploys (accounts / console / inbox) are expected to trigger on merge.

## Test plan

- [ ] CI green (core/services/auth-sdk/api test jobs + build jobs)
- [ ] `WebOxyProvider.signInLoop.test.tsx` passes and demonstrates the fix
- [ ] Post-merge: confirm no sign-in redirect loop on console (`console.oxy.so`)
- [ ] Post-merge: confirm cross-domain session sync still restores sessions on Safari/Firefox (no FedCM) via `/auth/silent` + `/sso` bounce

🤖 Generated with [Claude Code](https://claude.com/claude-code)
