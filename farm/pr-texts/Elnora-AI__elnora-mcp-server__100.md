# feat: consume platform refresh tokens for 30-day MCP sessions (ELN-513)

## Summary

- **Store platform refresh tokens** — `exchangeAuthorizationCode` now reads `refresh_token` from the platform's token exchange response and persists it in the `TokenRecord`
- **Auto-refresh expired platform tokens** — `verifyAccessToken` attempts `grant_type=refresh_token` against the platform before revoking, transparently extending sessions from 1 hour to 30 days
- **Security hardening** — sanitize Axios errors in logs to prevent `client_secret`/`refresh_token` leakage; add sensitive keys to log redaction set
- **Deduplicate refresh logic** — extract `attemptRefreshOrRevoke()` helper used by both `valid:false` and `401` code paths

Fixes ELN-513

> **Depends on**: Backend PR Elnora-AI/elnora-platform#676 (merged) which adds `grant_type=refresh_token` support to `/oauth/token`. Deploy backend first, then this PR.

## Test plan

- [x] TypeScript compiles clean (`tsc --noEmit`)
- [x] 111/111 unit tests pass (5 new: refresh on valid:false, refresh on 401, refresh failure → revoke, cached validation after refresh, getPlatformToken returns refreshed token)
- [x] Security audit: Axios error sanitization, log redaction, no credential leakage
- [ ] Deploy backend with refresh token support first
- [ ] Deploy this PR, authenticate, wait >1 hour, verify session survives

🤖 Generated with [Claude Code](https://claude.com/claude-code)
