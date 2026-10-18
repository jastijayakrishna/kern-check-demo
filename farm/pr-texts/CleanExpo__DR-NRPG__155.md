# feat(auth): per-request account-status enforcement (DR-873)

## DR-873 — block/suspend takes effect within one request

`authenticateRequest` already re-reads the user from the DB on every request (so `userType` is always current), but it **never checked `isActive`/`isBlocked`** — a user blocked or deactivated after login kept authenticating until their JWT/session expired.

Adds an account-status gate in **both** auth paths (cookie session + bearer token): a freshly-read user with `isActive === false` or `isBlocked === true` gets `403 Account is suspended or inactive`. Because the read is per-request, block/suspend/role changes now apply immediately.

### Verification
`pnpm --filter nrpg-web type-check` → **0 errors** ✅. No DB change. (High blast radius: this middleware backs ~250 routes — change is additive, returns the same shape on success.)

Phase 1 auth gates (DR-856).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
