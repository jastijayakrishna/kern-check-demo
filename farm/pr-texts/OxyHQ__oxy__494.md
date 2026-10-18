# fix: session restore self-heal + unified switchable accounts (ProfileMenu lists linked accounts) + SDK-only sign-in screen

## Summary

Three fixes on top of the Fase 4 redeploy (#492), root-caused live on accounts.oxy.so:

1. **fix(services): self-heal web stored-session restore** — the cold-boot guard required BOTH the stored active-session id AND the legacy `activeAuthuser` marker. `writeActiveAuthuser` was deleted in the SessionClient cutover, so **every fresh web sign-in lost its session on reload** (observed: zero API calls during cold boot); and a server-side revocation that removed only the active-id key stranded surviving valid sessions. New guard bails only when there is nothing to restore; when the active id is missing/invalid, the first validated surviving session is elected provisional active — the SessionClient handoff reconciles the true active from the server.

2. **feat(services): unified switchable-accounts hook** — `useSwitchableAccounts` = device set ∪ linked account graph (`GET /accounts`: owned orgs + shared-with-you), deduped. ProfileMenu / AccountMenu / AccountSwitcherView all list device + linked accounts and route EVERY selection through `switchToAccount(accountId)` (on-device → plain switch, first-time → mint + register; one uniform path). Applied as a **verified-content overlay** from `impl/session-sync-p1` (the diff was not self-contained against main's older ProfileMenu; the overlaid ProfileMenu carries its NativeWind unification + restored dual-edge anchor for ProfileButton `placement:'auto'`). AccountMenu retained — inbox/MailboxDrawer consumes it.

3. **refactor(accounts): sign-in screen delegates to the SDK** — thin branded shell with a single "Sign in with Oxy" button opening the SDK SignInModal; app-local password form + 2FA step removed (they live in the SDK flow).

## Verification (on THIS branch)
- services: 46 suites / 250 tests green; `tsc --noEmit` 0; `bun run services:build` success
- accounts: tsc = pre-existing NW5 baseline only; expo export verified on identical content

🤖 Generated with [Claude Code](https://claude.com/claude-code)
