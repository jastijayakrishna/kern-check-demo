# feat: Fase 4 — auth-sdk WebOxyProvider on SessionClient (cross-domain session sync, web-RP half)

Completes the client cutover for the cross-domain session-sync redesign. `@oxyhq/auth` `WebOxyProvider` fully retires `AuthManager` and drives the server-authoritative `SessionClient` (`@oxyhq/core`), so web-RP apps (console, mention.earth) join the same central device-session as the Expo apps (services, already live).

**Reconciled onto main** preserving #459 sign-out gates, #462 localStorage fail-safe (`getLocalStorageWeb`), #473 core ^5.

- `@oxyhq/core`: shared SessionClient integration layer (host adapter + projection + factory), reused by services + auth-sdk (no duplication).
- `WebOxyProvider`: cold-boot token ladder + `addCurrentAccount→start→syncFromClient` handoff; mutations→SessionClient; socket owned by SessionClient (`useSessionSocket` deleted); `accounts`/`activeAuthuser` derived from device state; **token refresh** = reactive (silent-iframe/FedCM re-mint) + proactive (exp−60s) — NOT `bootstrap` (would deadlock the bearer-gated route). AuthManager fully retired.
- console `playground.tsx`: `authManager`→`oxyServices.httpService.refreshAccessToken`.

Verified: auth-sdk **95/95**, core session tests green, tsc + `auth:build` + `oxy-console build` clean. Deploys console (+ rebuilds accounts/inbox via core filter — services behavior unchanged, additive core). Cross-app verification (accounts↔console) follows the merge; mention.earth needs a separate `@oxyhq/auth` publish + bump.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
