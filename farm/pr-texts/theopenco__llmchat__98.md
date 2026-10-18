# feat(widget): persist visitor identity in localStorage (skip the form on reload/return)

## Why

`name`/`email`/`identified` were plain React state (reset on reload), so the IdentifyForm re-triggered even though the visitor already entered their details — and the server already had them (the model never re-asks; this was purely the client form gate). This adds a client-side prefill so a returning/reloading visitor skips the form. **The server conversation row stays authoritative** — this is convenience only.

## Design

- **localStorage, per-project key** `llmchat_identity_<projectKey>`, value `{ name, email, savedAt }`.
  - *localStorage* (not sessionStorage) → a **returning** visitor (new tab / after a close) is remembered.
  - *per-project key* (not global) → identity is PII, so a multi-widget origin can't bleed one project's visitor into another's form. (The anonymous `clientId` keeps its sessionStorage + global key — divergence documented in `lib.ts`.)
- **30-day TTL** → bounds stale data + the shared-device window. `getStoredIdentity` is tolerant (missing / malformed / expired / empty-name → `null` → form shows) and **never throws** (private-mode / quota safe). Name + email trimmed on store.
- **Read on mount** (next to `setClientId`) → prefill + `setIdentified(true)` to skip the form. **Write on submit** → `setStoredIdentity` (the form already blocks an empty name).

## Embed architecture (confirmed, as requested)

`mount.tsx` uses `document.currentScript` + `host.attachShadow` → the widget runs as a **same-origin script in the customer's page**. So this identity PII lands in the **customer's origin localStorage** (shared with their other scripts) — which is exactly why the **per-project key** matters. (The `/embed` route is the separate cross-origin-iframe option; it'd isolate to our origin.) This doesn't change the localStorage decision, just records where the PII lives.

## Preserved / not touched

- **Zero bug-1 interaction** (confirmed): `findOrCreateConversation` returns an existing row without overwriting name/email, and the model identity reads `conv.name`/`conv.email` (set at creation) — so the prefilled chat-body values can't change what the model sees on an existing conversation.
- IdentifyForm fields + **email-optional** unchanged; overwrite semantics unchanged; escalation/resolve/holding untouched.
- **Empty-name guard** ties to #93: a stored empty name never skips into a "Hi !" greeting.

## Verification

- **Widget 112 tests pass.** New: round-trip, TTL expiry + cleanup, malformed/missing/empty-name → null, **per-project keying**, trim, and mount-hydration (skips form + personalizes the greeting; **still shows the form** when storage is empty / expired / a different project).
- Bundle 900.83 kB (helpers only, no bloat). Adversarial review (correctness/security + scope/tests) → **ship**, zero blocking; I folded in the two worthwhile nits (trim-on-store, stale-entry cleanup).
- `vitest.setup.ts` now clears web storage between tests — necessary because form-submit now persists identity (fixed two pre-existing escalated/resolved tests that re-submit the form under the same projectKey).

## Known tradeoff (the explicit decision, documented in code)

On a shared/kiosk device, the 30-day localStorage entry means a new visitor in a fresh tab gets a new conversation **prefilled** with the prior visitor's name/email. The TTL bounds it; a shorter TTL or a "not you?" reset link could tighten it further (out of scope here).

Deploy: widget change — if the preview's `kind: nextjs` builder flakes, known transient, re-trigger once.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
