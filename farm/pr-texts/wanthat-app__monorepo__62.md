# feat: passkey (Face ID) login — remembered phone, no re-prompt (ADR-0022 Flow B)

## Summary

Implements the missing login half of ADR-0022 Flow B: "visit → biometric → in" for a returning device, with OTP as the always-available fallback for a fresh device.

- **Contracts** (`packages/contracts`): `PasskeyLoginOptionsBody/Response`, `PasskeyLoginVerifyBody/Response`.
- **Cognito wrapper** (`services/app-auth`): `startPasskeyAuth`/`respondPasskeyAuth` drive Cognito `USER_AUTH` with `PREFERRED_CHALLENGE: WEB_AUTHN`.
- **Router** (`services/app-auth`): `POST /auth/passkey/login/options` and `/verify` — public, enumeration-safe (unknown phone and "no passkey enrolled" both collapse to `passkey_unavailable`). Verify hands off the *same* signed ticket as `/auth/verify`, so `/auth/session` (app-core) resolves the member exactly like the OTP path.
- **Infra** (`infra/lib/api-stack.ts`): the two login routes are explicit static routes with **no authorizer** (user isn't signed in yet) and take precedence over the JWT-authorizer-protected `/auth/passkey/{proxy+}` enrolment route.
- **SPA** (`apps/web`): the phone (Cognito username) is remembered in `localStorage` on every successful sign-in (`apps/web/src/lib/device.ts`) and replayed silently for passkey login (`apps/web/src/lib/passkey.ts#loginWithPasskey`). `AuthPage` shows a device-matched biometric CTA ("Sign in with Face ID"/"Touch ID"/"Windows Hello") above the phone form when a phone is remembered, with "use a different number" to forget it. OTP is always visible as the fallback.

**RP-ID / origin note:** same origin as enrolment (`dev.wanthat.app`), so the WebAuthn RP-ID already fixed on the pool matches — no Managed Login (hosted-UI) redirect is needed for this flow.

**Managed Login (Flow C):** left in place (`managed-login.ts`, `CallbackPage`) but no longer linked from the customer sign-in flow — it's currently non-functional (its origin, the Cognito domain, can't consume a passkey bound to the site RP-ID) and needs a custom auth domain to fix, which is a separate future slice/ADR. A fresh device without a remembered phone falls back to OTP, which always works.

## Test plan

- [x] `pnpm build && pnpm typecheck && pnpm test && pnpm lint && pnpm synth` all green
- [x] `infra/cdk.out/wanthat-dev-api.template.json`: confirmed `POST /auth/passkey/login/options` and `/verify` have `AuthorizationType: NONE` (no authorizer); `POST /auth/passkey/{proxy+}` still has `AuthorizationType: JWT`
- [ ] On-device manual validation (Face ID / Touch ID / Windows Hello) — automated browsers have no platform authenticator, so this needs a real device against a deployed dev stack

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01TjkamzCAy4WuLNzQwTiR7d
