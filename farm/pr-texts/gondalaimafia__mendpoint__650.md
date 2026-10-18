# closure: make the successor live proof satisfiable (authority rotation)

Makes the successor activation live proof satisfiable. Activation previously required a proof that could not be produced: the successor's check contexts are not required until branch protection is switched, so its first run can never be a required check on the activation head itself. #619 had to be merged by an owner-authorised operator bypass because of it.

## What the rule now requires

**On `pull_request`** (the merge gate), activation is proven by an **open sibling** pull request whose head ran the staged bytes successfully:

- the sibling's App check-run and controller commit status must both be present on the sibling head, both App-bound, and both link to the **same** workflow run;
- that run must be the successor workflow path, not the predecessor's, and its own conclusion must be `success`;
- the run must have started **after the staging window opened**, bounded by the staging provenance (below), with an unparseable `created_at` rejected rather than admitted.

**On `push`** (after the activation merges), the pull_request-time proofs are deliberately **not** re-performed on the merged head. They were enforced proposal-side at pull_request time and are re-verified by `closure:check` on main. The observation records this as `skipped` rather than `observed`, so it cannot be read as a positive verification that never happened.

## Staging provenance bounds the window

The success-path window starts at the staging rotation's `issuedAt`. That is now resolved by `main()` from the trusted on-disk main policy plus the rotation ledger, so it is available on **every** trigger — the pull_request merge gate, the schedule sweep, and the push fan-out — not only on the `current_pull_request` scope where the proposal observation is plumbed. When the proposal observation also carries provenance, the two must **agree**. Absent provenance fails closed with `AUTHORITY_SUCCESSOR_STAGING_PROVENANCE_REQUIRED` rather than running on an unbounded window.

## Coverage bound, stated explicitly

Only **open** siblings are enumerated, from the open-PR set already fetched, so no extra installation API calls are made. A sibling that merged or closed between its success run and the activation is not counted. In practice the window is dense — D1 produced eight sibling runs in 44 minutes — and a missing proof **fails closed**, so the bound narrows what can prove activation, never what can pass.

## Sibling bytes are bound, not assumed

A sibling success run only counts if the successor workflow file **at that sibling's base revision** hashes to the staged digest. The file content is read back through the contents API and compared, so a sibling that ran an earlier version of the bytes, or whose staged workflow file is absent at its base, is rejected.

## Path validation before any request

Because the workflow path is used to build that contents-API request, a path carrying traversal segments is rejected **before any request is issued** (`AUTHORITY_SUCCESSOR_WORKFLOW_PATH_INVALID`), rather than relying on later equality checks. Percent-encoding does not neutralise traversal and is handled.

## Release-train record restored for #461

This rotation also restores **#461** as a merged static release-train record. #461's own rotation removed its static record because `CURRENT_PR_BOOTSTRAP_DUPLICATE` forbids being both the bootstrap and a static record. It has since merged, so `main` satisfies `PR_NOT_IN_RELEASE_TRAIN` for the `ME-GTM-003` row **only while 461 remains the bootstrap** — and any rotation regenerating the bootstrap strands it. A rotation is the only vehicle that can carry the record, since an ordinary data pull request cannot add it while 461 is still the bootstrap.

Every mutable value is read live from the GitHub API; the field set, order, `owner` shape (`branch_prefix`, which `production-closure-matrix.ts` requires of every static record) and `review` shape follow the records #639 refreshed.

## Receipt

```
rotationId            rotation-2026
