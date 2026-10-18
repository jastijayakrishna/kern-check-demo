# fix(admin): scope growth page MemberEvent queries to actor's org

## Summary
- Three data-loader functions on `/admin/growth` (`loadSignupsByUtmSource`, `loadApplyAttemptsLast24h`, `loadLoginCountLast24h`) queried `MemberEvent` without an org filter — an admin from Org A could see Org B's UTM signup and login telemetry
- Added `user: { organizationId: orgId }` filter to all three queries
- Wrapped loader calls in `withAuthGuc()` to satisfy RSC GUC context (same pattern as `app/admin/page.tsx:43`)
- Resolves **TODO-007** (cross-org scope issue on growth analytics page)

## Test plan
- [ ] Log in as an Org-A admin, visit `/admin/growth` — should only show events for Org-A members
- [ ] Log in as a super_admin — should see all events (orgId scoped to their own org; super_admins have their own org context)
- [ ] Typecheck passes (`npx tsc --noEmit`)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
