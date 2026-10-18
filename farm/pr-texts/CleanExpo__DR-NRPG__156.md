# feat(auth): centralized RBAC gate for /api/admin + /dashboard/admin (DR-874)

## DR-874 — admin RBAC

**Centralized gate (new):** edge middleware now blocks `/api/admin/*` and `/dashboard/admin/*` unless the NextAuth JWT's `userType` is `ADMIN`/`SUPER_ADMIN` — API → `403`, pages → redirect to `/login`. Ensures no admin route can be accidentally left ungated.

**Authoritative checks (already present):** route handlers use `authenticateRequest` + `requireRole()` (fresh DB userType), and `app/api/admin/contractor-verification/action` already requires ADMIN/SUPER_ADMIN and writes an actor audit row via `logContractorVerification`. The middleware is defense-in-depth on top of these.

### Reviewer note
The middleware gate reads `userType` from the JWT via `getToken`. Please confirm the NextAuth `jwt` callback populates `token.userType` (it does in `lib/auth`) so legitimate admins aren't 403'd — the route-level `requireRole` (fresh DB read) remains the source of truth regardless.

### Verification
`pnpm --filter nrpg-web type-check` → **0 errors** ✅. No DB change.

Phase 1 auth gates (DR-856).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
