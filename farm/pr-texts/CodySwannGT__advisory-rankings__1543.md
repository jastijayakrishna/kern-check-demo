# feat(harper): CSRF origin checks, login throttling, security headers, write caps

## Summary

Security-hardening batch from the HarperDB best-practices review (findings M3/M4/M5/L1):

- **CSRF (M3)**: Harper hardcodes the session cookie to `SameSite=None; Secure` on HTTPS, removing the browser's cross-site protection. Every state-changing `post` (`Login`, `Logout`, `UserWatchlists`, `AdvisorRating`, `AdvisorCorrectionRequest`, `RegulatoryDiscrepancyReview`) now calls `requireSameOrigin()` — 403 when the browser-attested `Origin`/`Referer` host differs from the serving host. `Host`/`X-Forwarded-Host` aware for the Fabric edge proxy; header-less non-browser clients (curl, smoke, MCP) are allowed.
- **Login throttling (M4)**: per-worker in-memory failed-attempt lockout on `/Login` — 5 free attempts, then exponential 2s→15m windows returning 429. Best-effort per-thread brake (documented as such); front with edge rate-limiting for a hard guarantee.
- **Security headers (M5)**: the fastify static/shell layer emits `X-Content-Type-Options: nosniff` on every response and `CSP: frame-ancestors 'none'` + `X-Frame-Options: DENY` + HSTS + `Referrer-Policy` + `Permissions-Policy` on HTML documents. The ZAP baseline promotes those rules from WARN to FAIL so a regression breaks the build.
- **Abuse caps (L1)**: per-user limits on watchlists (50) and pending corrections (25), whose random ids were otherwise unbounded.

Runbook security section documents each control (CSRF posture, throttle semantics, header set, and the MQTT/WS broker-not-exposed posture).

## Verification

- `bun run build` / `typecheck` / `lint` clean
- `bun run test:cov`: 715 passed, 0 failed (new suites: `resource_request_origin`, `resource_login_throttle`; existing auth/watchlist/rating/correction suites still green under the new guards)

## Follow-ups (separate PRs, in flight)

- Full-scan `loadAll()` migration on profile/analytics endpoints
- RBAC role-map codification + CI drift check
- Lint-debt un-ratchet (`functional/type-declaration-immutability`, statement-order)

🤖 Generated with Claude Code
