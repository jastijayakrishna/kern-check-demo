# fix(db): lazy-resolve GUC context in Prisma middleware for RSC pages

## Summary

Resolves #1611 — 112 server-component pages under `app/admin` + `app/(portal)` query Prisma with anonymous GUC credentials because RSC renders run outside the root layout's `gucContextStorage.run()` AsyncLocalStorage scope.

**Fix (Option A from the issue):** when `getGucContext()` returns `null` in the Prisma middleware, lazily call `resolveAuthGucContext()` via a dynamic import. Since that function uses React's `cache()`, it is one Supabase + one DB round-trip per request, shared across all RSC queries. Outside a React request (cron, build), `getUser()` returns `null` and falls through to `ANONYMOUS_GUC_CONTEXT` — identical to the current behavior.

The `$transaction` override gets the same treatment: RSC code calling `prisma.$transaction()` now also gets proper GUC setup inside the transaction.

**Dynamic import** avoids the circular dependency: `lib/auth/server.ts` imports `prisma` from `lib/db/prisma.ts`, so a static import would cycle at module init time.

**No behavior change for:**
- API routes (already wrapped in `withApiGuc` — explicit ALS context is set, lazy path never fires)
- Cron routes (explicit `withSystemGuc` context)
- Anonymous/unauthenticated RSC renders (lazy-resolved context degrades to `ANONYMOUS_GUC_CONTEXT`, same as before)

## Test plan
- [ ] Admin pages still load and show correct data after login
- [ ] Portal pages (member dashboard, etc.) still load correctly
- [ ] Unauthenticated access to public pages still works
- [ ] No new `[prisma:guc]` console errors in dev
- [ ] `resolveAuthGucContext()` is not called more than once per request (React cache deduplicated)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
