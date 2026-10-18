# fix(app-blocks): allow buzz:read:self in dev-mint + surface un-grantable dev-preview consent

## Summary

Fixes two related App Blocks **dev-tunnel consent** issues reported by an app author. Dev-tunnel / mod-gated (dark) — no change to the prod approved-app consent path.

## Issue A (server — the real fix): `buzz:read:self` missing from the dev-mint allowlists

`dev-scoped-mint.service.ts` defines three scope allowlists the mint clamp filters against. `buzz:read:self` was in **none** of them, so in the dev-tunnel the clamp stripped it before consent — the block's `REQUEST_CONSENT` resolved an empty `missingScopes`, and the app's "Allow ledger access" button looked dead.

**Fix:** add `buzz:read:self` to **`DEV_TOKEN_SCOPE_ALLOWLIST`** (bearer dev-token) and **`TUNNEL_HOST_MINT_SCOPE_ALLOWLIST`** (cookie dev-tunnel host-mint) only.

Why it's safe:
- **Self-bound to the dev's OWN ledger.** The dev-mint signs the token with the authenticated dev's `userId` as subject, and the buzz-read bridge (`authorizeBlockBuzzRead`) derives `userId` off `claims.sub` — never body input — then re-checks `assertViewerIsAppDeveloper`. So the scope reads only the dev's own balance/ledger/earnings, no third-party financial data, no consent round-trip needed.
- **Pure read.** All `buzz:read:self` handlers require `TokenScope.BuzzRead`; no money moves. The money-OUT scope `social:tip:self` (`TokenScope.SocialTip`) stays **excluded everywhere**.
- **Consistent** with the dev allowlists already granting `ai:write:budgeted` (real Buzz *spend*) and `collections:read:private` — forbidding a dev from *reading* their own balance while permitting *spending* it is incoherent.

**Deliberately withheld** from the mod-review sandbox allowlist (`REVIEW_MINT_SCOPE_ALLOWLIST`, unchanged): a mod previewing *someone else's* unapproved app must not leak the mod's own balance.

## Issue B (client — defensive UX): un-grantable `REQUEST_CONSENT` dropped silently

`PageBlockHost` previously no-op'd whenever the grantable set was empty, so a request for a permission that was clamped/withheld at mint (un-grantable in this preview) vanished silently — the app looked broken.

Now it distinguishes, deterministically:
- **Benign** — every requested scope is already granted (a block re-requesting a held scope) → keep the silent no-op.
- **Un-grantable** — a requested scope is neither currently granted nor addable via consent (`missingScopes`) → surface a "permission isn't available in this preview" toast.

The distinction uses the block's advisory `scopes` hint **only to decide whether to inform the user** — never to widen the grant (still bounded server-side to `missingScopes`). `reviewMode` stays silent. The decision logic is extracted to a pure, unit-tested helper (`resolveUngrantableConsentScopes`).

## Tests

- `dev-scoped-mint.service.test.ts`: `buzz:read:self` ∈ both dev allowlists, ∉ mod-review sandbox; `social:tip:self` ∉ all; a dev-tunnel manifest requesting `buzz:read:self` keeps the scope through the clamp; the sandbox strips it.
- `dev-token.test.ts`: R1 escalation-defense tests updated — `buzz:read:self` now legitimately survives the bearer path; money/write/unknown scopes still stripped.
- `pageBlockHostLogic.test.ts`: full coverage of the un-grantable/benign/grantable/no-hint cases for the new helper.
- `PageBlockHost.browser.test.tsx`: un-grantable request toasts (no dialog); benign no-op neither toasts nor dialogs; `reviewMode` stays silent.

All targeted unit + browser tests pass (129 unit + 25 browser).

🤖 Generated with [Claude Code](https://claude.com/claude-code)

