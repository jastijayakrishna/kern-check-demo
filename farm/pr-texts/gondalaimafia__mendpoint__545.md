# Event-source the current-PR bootstrap to de-serialize the closure queue

## Summary

Every PR had to **edit** `docs/PRODUCTION_CLOSURE_MATRIX.json` to re-author its own `releaseTrain.currentPullRequestBootstrap`, so every PR conflicted with every other on that one file and only one could merge per matrix generation.

This does **not** stop PRs from shipping a bootstrap: `requireCurrentPullRequestBootstrap: true` still holds, so every PR carries a structurally valid block. The change is that a PR may now **inherit the block unchanged** from main (stale, describing whatever merged last) instead of re-authoring it. An unchanged inherited block does not conflict, which removes the serialization; the pull request under judgement is resolved from provider facts instead of from that block.

- **github-authority**: resolves the current PR from the workflow event (`pull_request`) or the single PR the pushed commit merged (`push`; new `listPullRequestsForCommit`, fail-closed on zero-or-many). The rotation attestation demand is driven by the rotation `production-closure-proposal-authority` actually validated (the trusted, head-bound proposal observation) when that determination ran, and by the **number-bound** matrix declaration when it did not (the sweep) — never by a raw self-declared bootstrap number, and never silently collapsed to "no rotation". The owner is derived from the live `release-owner:*` label, bound by time to the latest mutation (labeled or unlabeled) of any such label so a stale exact-head approval cannot be promoted by mutating labels. A live requirement-mapping cross-check keyed on the event PR keeps the matrix from crediting the current PR with a requirement its body does not declare.
- **matrix**: `currentPullRequestBootstrap` optional in the type; still required and shape-validated in production.
- **proposal-authority**: the self-removal exemption keeps #539's `bootstrapChanged` rule and prefers the CI-attested `MENDPOINT_CLOSURE_PR_NUMBER` when present; the env var is optional at the entrypoint, so the pinned workflow is not edited and this lands as a pure `runtime` rotation.

Rotations keep the author-time bootstrap since `authorityRotation` carries reviewed intent that cannot be reconstructed from live PR metadata.

## Known residual (accepted for this PR, documented)

**What:** On the `*/30` scheduled sweep (and `push`/`workflow_dispatch`), a rotation whose matrix bootstrap declares the `authorityRotation` under a pull request number that is **not** the pull request being evaluated ("foreign-numbered declaration") does not have its exact-head rotation **attestation** demanded by `github-authority`. Its `boundMatrixBootstrap` is undefined (the declaration names another PR), so `expectedRotation` is undefined and no attestation is required on that path.

**Exact conditions required to reach it:** (1) the sweep trigger, where `observationScope` is `full_release_train` and the proposal rotation determination is not plumbed into `github-authority`; **and** (2) an `authorityRotation` declared under a foreign PR number; **and** (3) a plain (non-attesting) trusted approval on the exact head. On the reactive `pull_request_target` path this same declaration is rejected with `AUTHORITY_ROTATION_FOREIGN_DECLARATION` and the missing attestation is demanded.

**Bounded — it is not an unvalidated protected-file change.** `production-closure-proposal-authority` runs on **every** trigger including the sweep (it has no trigger/scope branching), and **both** merge-gating contexts (the dedicated App check and the controller status) are published only when `PROPOSAL_OUTCOME == success`. So the rotation's ledger receipt, base/proposed policy digests, protected-file digests, surface-drift, and bootstrap-to-receipt binding are all validated on the sweep and gate the merge. The only control the sweep cannot demand for a foreign-numbered declaration is the exact-head review that explicitly attests the `rotationId` plus both policy digests. A self-named rotation on the sweep **is** attestation-gated (number-
