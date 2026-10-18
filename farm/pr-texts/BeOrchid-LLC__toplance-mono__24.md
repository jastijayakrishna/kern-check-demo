# Guard against deploying a Clerk dev instance to a real host

## Summary
- Root cause of the staging `session_exists` login loop: staging was built with a `pk_test_`/`sk_test_` Clerk dev key pair, which runs cookieless (`url_based_session_syncing`) — the browser holds a session the server can never read as a cookie, so `proxy.ts` and clerk-js permanently disagree.
- Adds `src/instrumentation.ts` + `src/lib/env/verify-clerk-instance.ts`: at server startup, refuses to boot if `CLERK_SECRET_KEY` is `sk_test_` and `APP_URL` resolves to a non-local host. Turns this into a loud deploy-time failure instead of a login loop discovered in the field.
- Fixes `toplance.ca` → `staging.toplance.ca` in the README's Clerk instance setup steps (the doc named the wrong host).
- Corrects a comment in `auth-form.tsx` that implied the `window.location.assign` + Clerk handshake always closes the session gap — it only does on a `sk_live_` instance, which sets a real first-party cookie.

This does not fix the staging instance itself — that requires a new Clerk application, live keys wired through Coolify, and a rebuild, all outside this repo.

## Test plan
- [x] `npm run typecheck` — clean
- [x] `npx vitest run` — 687/687 passing, including 6 new cases in `src/lib/env/verify-clerk-instance.test.ts`
- [x] Manually booted a throwaway dev server with `CLERK_SECRET_KEY=sk_test_… APP_URL=https://staging.toplance.ca` and confirmed it refuses to become ready with the expected error
- [x] Manually booted normally against `.env.local` and confirmed no behavior change (guard is a no-op)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01D6sviXri3zJ7JFp55bbYeh
