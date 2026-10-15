# fix: block localhost and loopback addresses in SSRF protection

## Summary
- Adds `127.0.0.1`, `::1`, and `0.0.0.0` to the `BLOCKED_HOSTNAMES` list alongside `localhost` for defense-in-depth SSRF protection
- Previously these addresses were only caught by IP range checks; now they are also blocked at the hostname level, ensuring consistent "Blocked hostname" errors
- Adds corresponding test coverage for the new blocked hostnames

Closes #28616

## Test plan
- [x] `TZ=UTC yarn vitest run packages/lib/ssrfProtection.test.ts` -- all 59 tests pass (4 new)
- [ ] Verify no regressions in webhook URL validation
- [ ] Verify self-hosted environments still allow private IPs for internal webhooks

🤖 Generated with [Claude Code](https://claude.com/claude-code)
