# fix(auth-sso): clear cookie before sending 500 on SSO login failure

## Problem

Every SSO login attempt while the SSO upstream is unavailable crashes an entire ECS task. The error path of `login` in `auth-sso.controller.ts` chains `.clearCookie()` after `.json()`, so the cookie write runs after the response has been sent and throws `ERR_HTTP_HEADERS_SENT`. The throw happens inside the neverthrow `mapErr` callback, so it escapes as an unhandled rejection and Node 22 terminates the process.

This is the root cause of the 2026-10-16 prod incident: three tasks died at 02:38 and 02:43 UTC during a transient SSO discovery outage, each preceded by exactly one `GET /api/v3/auth/sso/login 500`, producing the ALB connect/5XX alarms and the ECS crash monitor warn ([alert thread](https://opengovproducts.slack.com/archives/CLJPA6NDN/p1792118729211939)).

## Solution

Reorder the chain so `.clearCookie()` runs before `.json()` sends the response.

Adds a controller spec covering both paths of `login`. The regression test asserts clearCookie-before-json via jest `invocationCallOrder` — a `headersSent`-aware throwing mock would mirror Express more literally, but the `typesafe/no-throw-sync-func` lint rule forbids throwing in sync mock implementations, and the ordering assertion catches the same regression. Verified the test fails against the pre-fix controller.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
