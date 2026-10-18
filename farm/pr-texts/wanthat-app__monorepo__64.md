# feat: passkey autofill (conditional UI) + login rate limit (ADR-0022)

## Summary
- Conditional UI: on the auth page, if the device remembers the phone and the browser supports WebAuthn autofill (`browserSupportsWebAuthnAutofill()`), a conditional-mediation ceremony is primed on mount (`startAuthentication({ optionsJSON, useBrowserAutofill: true })`). The passkey surfaces itself in the phone field's autofill — the user taps the chip, Face ID runs, they're in — no button press first. The phone `<input>` carries `autocomplete="tel webauthn"` so the browser attaches passkeys to it.
- The explicit "Sign in with Face ID" button stays as the guaranteed fallback (browsers without autofill support, or a user who prefers it); tapping it runs a normal (non-conditional) ceremony, which SimpleWebAuthn 13 uses to auto-abort the pending conditional one.
- **iOS caveat:** a true auto-modal biometric prompt on page load is browser-forbidden without a user gesture. Conditional UI (the passkey surfacing in autofill) is the sanctioned closest-to-automatic path that works on iOS — this is the ADR-0022 "auto-on-load" spike realized within that constraint, not a new decision.
- Every non-success outcome of the conditional ceremony (no autofill support, user picks another method, cancel, abort from a new ceremony) is swallowed silently — no error UI, the remembered phone is never forgotten. It starts at most once per mount, only on the phone step.
- New per-phone rate limit on `POST /auth/passkey/login/options` (`withinPasskeyVelocity`, config keys `auth.passkeyMaxPerWindow` default 30 / `auth.passkeyWindowMinutes` default 60). This endpoint now fires on every auth-page load, so it runs on its own `"pk:"`-prefixed counter — deliberately generous and completely separate from the SMS-OTP velocity counter, so a member who signs in with Face ID often is never locked out.

## Test plan
- [x] `pnpm build && pnpm typecheck && pnpm test && pnpm lint && pnpm synth` all green
- [x] Unit tests: new config-default test (`@wanthat/contracts`), new 429 router test + velocity-cap wiring (`@wanthat/app-auth`)
- [ ] **On-device validation required** — conditional UI/autofill cannot be exercised in an automated browser (no real platform authenticator + user gesture). Verify manually on an iOS Safari device with an enrolled passkey: phone field should surface the passkey chip in autofill on page load; tapping it should complete Face ID sign-in. If iOS doesn't surface the chip for a username-hinted challenge on a given build/device, the explicit button still works — no regression either way.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01TjkamzCAy4WuLNzQwTiR7d
