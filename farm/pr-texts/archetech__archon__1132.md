# fix(gatekeeper): Authorize against the key the proof names

Closes #1130.

Both gatekeeper ports authorized an operation against `verificationMethod[0]`
whatever key the proof named, each carrying a `TBD` saying so. The key is now
selected by the DID URL in `proof.verificationMethod`.

## Why this is safe for everything anchored

Checked against the BTC-mainnet node's store rather than assumed, because a
change here that disagrees with history makes DIDs unresolvable:

| | |
| --- | --- |
| operations naming `#key-1` / `#key-2` / `#key-3` | 42,993 / 26 / 1 |
| absolute (`<did>#key-N`) vs relative (`#key-N`) | 41,408 / 1,612 |
| update or delete naming **their controller** | 11,442 |
| update or delete naming **their own DID** | 1,736 — and every one classifiable is an **agent**, the only DID type whose own document holds a key |

Rotation replaces the identity key **in place** (`keymaster.ts:2226`), keeping it
at index 0 under a new fragment, which is why the 27 operations naming `#key-2`
or `#key-3` verify today. So index 0 *is* the named key for the whole corpus, and
selecting by name reaches the same key — it just stops being an accident of how
rotation happens to work.

Six of the 1,736 could not be classified: their create operation is not in this
node's store.

## Refusal, not `Invalid operation`

A proof naming a method the document does not list now fails to verify. It
deliberately does not raise `InvalidOperationError`: `importEvent` treats that as
**DEFERRED**, so such an operation would be retried forever instead of rejected.
The same applies to a method carrying no `publicKeyJwk` — one existing test
asserted the old throw and now asserts the refusal.

## Both test harnesses were signing operations a keymaster never emits

`createUpdateOp` in TypeScript and `create_update_operation` in Rust named
`<targetDid>#key-1`, so an asset update named a key under the **asset's** DID —
a key that exists nowhere, since an asset document has no verification methods.
Real keymaster names the signing identity (`keymaster.ts:1382`).

Those fixtures only passed because selection ignored the name. Both harnesses now
name the signer, and the Rust helper takes it explicitly.

## Not in this PR

Enforcing `proofPurpose` against the relationship the key is listed under. That
is now *possible* — it was not, with no key lookup — but a DID that has been
updated resolves with a controller-authored document that may not grant
`capabilityInvocation` (#1129), so the rule needs deciding rather than assuming.

## Verification

2953 JS tests, 397 Python, the full Rust suite, `tsc --noEmit`, eslint, clippy.
Both ports test naming a listed key, a second key, an unlisted key, and a
relative reference against an absolute one. Mutation-checked: reverting to index
0 fails the unlisted-key and second-key cases.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01GYGMfX3foBcVqP7AQNXjWj

