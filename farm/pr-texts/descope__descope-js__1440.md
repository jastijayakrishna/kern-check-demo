# fix(nextjs-sdk): read session cookie from request in getSession

## Problem

`getSession(req)` returns `undefined` in Pages Router API routes when the `Authorization` header is missing, even when a valid `DS` session cookie is present (customer report)

The cookie fallback used `cookies()` from `next/headers`, which only works in App Router request scope. In a Pages Router API route it throws, the error is swallowed (debug-level log only), and `undefined` is returned - the request cookie is never read

## Fix

- `getSession(req)` reads the session cookie directly from `req.cookies` (respecting `sessionCookieName` config) instead of `next/headers`
- `getSessionFromAuthorizationOrCookie` now takes the resolved cookie JWT value; each entry point supplies it from the right source (`next/headers` for App Router `session()`, `req.cookies` for Pages Router `getSession()`)

## Tests

- `getSession` cookie tests now go through `req.cookies`
- Regression test: `next/headers` `cookies()` throwing (Pages Router) while the request cookie is present
- Custom `sessionCookieName` test

🤖 Generated with [Claude Code](https://claude.com/claude-code)
