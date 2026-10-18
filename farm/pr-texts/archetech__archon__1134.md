# fix(gatekeeper): Resolve the controller at the time an operation arrived

Closes #1131.

An asset operation's controller was resolved at `proof.created` — a value the
signer chooses. So a holder of a key that had since been rotated out could date
an operation before the rotation, select the document that still listed the
retired key, and go on modifying every asset the agent controls. Rotating after a
compromise did not close the window.

**Demonstrated before changing anything**, against a running gatekeeper:

```
old key, current created  → false     (rotation worked)
old key, backdated created → true     (same key, same operation, accepted)
```

It's the asset path only. An agent's own document is resolved at current, so the
retired key could not touch the agent — only everything it controls. And #1087
could not have fixed it: binding `created` into the signature stops a third
party moving it, but the attacker *holds* the key and signs over whatever
`created` they like.

## The fix

The controller is resolved at the time the operation **entered the network**,
which every caller already knows and none of which is `proof.created`:

| how it arrived | resolved at |
| --- | --- |
| `POST /did` | now |
| imported from a chain registry | the event's `time` — the block time |
| replayed from the store | the stored event's `time` |

One helper per port states the rule (`controllerDocument` /
`controller_document`), and each verification path calls it with the time it
has. The two inline resolutions that dug `created` out of the proof go with it.

## Why not something simpler

Each alternative was tried and fails for the same reason: the verifier needs
to know when the operation entered the network, and that fact is on the event,
not the operation.

- **Always resolve at now** breaks replay. An operation anchored before a
  rotation was authorized by the key current *then*; re-verifying it after the
  rotation has to reach that key.
- **Bound `created` only on direct submission** is bypassable: an attacker with
  a node anchors the backdated operation directly, and every other node imports
  it through a path the bound never touches.
- **Bound against the asset's own history** does nothing for assets untouched
  since the rotation, which is most of them.

## Known limit, stated in the spec

A DID registered on `hyperswarm` is never chain-anchored, so its events carry
the time the sending peer asserted, and there is no trusted clock to bound
against. That registry remains exposed by construction. Chain-registered DIDs
and every direct submission are closed.

## Verification

Both harnesses cover both halves — the refusal, and that an operation made
before a rotation still verifies on replay at its own time — and each was
mutation-checked in both directions: ignoring the time fails the replay test,
forcing a pre-rotation time fails the refusal test.

2956 JS tests, the full Rust suite, `tsc --noEmit`, eslint, clippy. All 523
pre-existing gatekeeper tests passed with no changes, which is the replay
non-regression across every import and sync flow already covered.

New spec section §5.8 states the rule and the limit.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01GYGMfX3foBcVqP7AQNXjWj

