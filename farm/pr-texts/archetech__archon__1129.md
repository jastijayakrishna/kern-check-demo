# fix: Name the relationship an operation actually exercises

A DID operation claimed `proofPurpose: "authentication"`, which in DID Core means
the signer is proving they **are** the subject. An operation does something else:
it exercises control over a DID document. The relationship for that is
`capabilityInvocation`.

## What the specification says

[DID Core 1.0 §5.3.4](https://www.w3.org/TR/did-core/#capability-invocation):

> The `capabilityInvocation` verification relationship is used to specify a
> verification method that might be used by the DID subject to invoke a
> cryptographic capability, **such as the authorization to update the DID
> Document.**

That last clause is the specification's own example of the relationship, and it
is what a DID operation does. For contrast,
[§5.3.1](https://www.w3.org/TR/did-core/#authentication) and
[§5.3.2](https://www.w3.org/TR/did-core/#assertion):

> The `authentication` verification relationship is used to specify how the DID
> subject is expected to be authenticated, for purposes such as **logging into a
> website or engaging in any sort of challenge-response protocol.**

> The `assertionMethod` verification relationship is used to specify how the DID
> subject is expected to express claims, such as for the purposes of **issuing a
> Verifiable Credential.**

An operation is neither a login nor a claim.

**Scope, stated honestly:** no standard *requires* this. DID Core defines what
the relationships mean; it does not specify DID operations at all, and leaves
method behaviour to the method — "DID methods and applications are expected to
define this themselves". So this is `did:cid` choosing the relationship whose
defined meaning matches, not conformance to a clause. The fit is exact for update
and delete, and by extension for create, where the specification's phrase is
"update the DID Document" and no document yet exists.

**Why the document had to change too.**
[VC Data Integrity](https://www.w3.org/TR/vc-data-integrity/#proofs) calls
`proofPurpose` "a safeguard to prevent the proof from being misused by being
applied to a purpose other than the one that was intended", and §2.6 gives the
check as ensuring "the verification method is expressed under a verification
relationship that is acceptable given the proof's purpose". A purpose no
relationship grants cannot be checked, so generated agent documents list
`#key-1` under `capabilityInvocation` as well. Archon's credential path already
enforces exactly this rule (`authorizedForPurpose`).

The accepted set keeps `authentication` and `assertionMethod`. Both were accepted
before this, so an operation carrying either may already be anchored, and every
node replays its own history on restart. The BTC-mainnet node's 43,020 anchored
operations all claim `authentication` — but one node's store is not the network's
history, and the cost of being wrong is a DID that stops resolving permanently
against a saving of one string in a list.

## It was never decided

`authentication` was written in **#20**, the commit that introduced W3C-shaped
proofs, as a literal with no discussion in the message, the diff, or the scheme
doc it updated in the same change. `capabilityInvocation` appears once in the
whole history, and only as a value being *rejected* for credentials.

That is the same commit that chose `EcdsaSecp256k1Signature2019`, and the same
kind of error: a W3C shape taken by appearance rather than read against the
specification. #1127 corrected the type and left the purpose, which is the more
embarrassing half — the new proof builder in both ports is code written during
that PR, and it re-made the choice rather than inheriting it.

It survived because nothing consults it. Both gatekeepers check the string is one
of the accepted values and then authorize against `verificationMethod[0]`
regardless. "Nothing reads this" is the condition under which a wrong value
lasts, not evidence that it is right.

## What changed

- Both gatekeeper ports accept `capabilityInvocation`, and go on accepting
  `authentica
