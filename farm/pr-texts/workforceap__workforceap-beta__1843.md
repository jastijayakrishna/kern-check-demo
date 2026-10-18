# fix(guc): wrap coursera b4b admin routes and onet/search with withApiGuc

## Summary

Admin routes calling `isAdmin`/`requireAdmin`/`isSuperAdmin`/`isAdminInOrg` from `lib/auth/roles` (which queries Prisma) but missing `withApiGuc` per-request DB GUC context:

- `app/api/admin/coursera/b4b-bindings-suggestions/route.ts` — calls `isSuperAdmin`, `isAdminInOrg`, `getActorOrganizationId`
- `app/api/admin/coursera/b4b-programs/route.ts` — calls `isAdmin`
- `app/api/admin/coursera/self-test/route.ts` — calls `isAdmin` (via local `requireAdmin` wrapper)
- `app/api/admin/onet/search/route.ts` — calls `requireAdmin`

Part of Track A — Tenant Isolation Hardening GUC sweep.

## Test plan
- [ ] `/admin/coursera` page loads and B4B binding suggestions display
- [ ] B4B programs list renders for admin
- [ ] Coursera self-test runs to completion
- [ ] O*NET occupation search returns results in admin

🤖 Generated with [Claude Code](https://claude.com/claude-code)
