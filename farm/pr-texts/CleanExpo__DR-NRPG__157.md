# fix(auth): ownership scoping / IDOR on onboarding progress (DR-875)

## DR-875 — ownership scoping

**Offender fixed:** `app/api/onboarding/progress/[contractorId]` scoped contractors with `params.contractorId !== user.id` — but `Contractor.id ≠ User.id`. The check was doubly wrong: it blocked contractors from their **own** progress and never actually enforced ownership. Now it resolves the caller's `Contractor` via `Contractor.userId` and requires it to match the requested `contractorId` (ADMIN/SUPER_ADMIN exempt); `403` on mismatch.

**Audit result (the rest is already safe):**
- `app/api/contractor/[contractorId]` (GET/PATCH) already enforces `contractor.userId === user.id` (admin bypass) + field allowlisting.
- No contractor route trusts a client-supplied `contractorId` from body/query; private routes derive it from the session.

So this was the clearest remaining IDOR; the broader contractor surface already scopes by owner.

### Verification
`pnpm --filter nrpg-web type-check` → **0 errors** ✅. No DB change.

Phase 1 auth gates (DR-856).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
