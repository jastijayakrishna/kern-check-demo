# Faster mirror-based checkouts: packed-refs ref copy, pull-ref purge, commit-graph, single-attempt sync

## Summary

For `fetch-depth: 0` checkouts we populate the workspace's refs from the already-synced local mirror. Today that is `git fetch <mirrorPath> '+refs/heads/*:refs/remotes/origin/*' '+refs/tags/*:refs/tags/*'`, which runs the full fetch machinery — advertisement of the mirror's entire ref set (~60k for large repos including retained `refs/pull/*`), the `mark_complete` walk that parses every local ref tip out of the cold Ceph-backed pack, and a connectivity check. On a large repo this is the dominant checkout tail cost at peak: the same command takes ~2s warm and 3–4 minutes cold/contended on a large production repo (~18.7k live heads+tags), while the mirror sync itself took ~6s.

This replaces it with a direct ref copy in `copyRefsFromMirror`, with layered fallbacks (direct copy → previous local `git fetch` → existing network fetch):

- Fresh workspace (no `packed-refs` file and nothing under `refs/remotes/origin/*` or `refs/tags/*` — the normal checkout path): write the workspace `.git/packed-refs` file directly from the mirror's `for-each-ref` output via `buildPackedRefsContent` (heads → `refs/remotes/origin/*` per `mapMirrorRefToWorkspace`, tags as-is, byte-sorted, `# pack-refs with: sorted` header). Zero object access — the only mirror reads are its own ref listing.
- Reused workspace: reconcile with `git update-ref --stdin` via `buildRefCopyInstructions` — `delete` for stale workspace refs (equivalent to `--prune`), `update` only for refs whose sha differs (equivalent to `+` force refspecs, but skipping unchanged refs because `update-ref` verifies the object of every ref it writes), then `pack-refs --all`. Symbolic refs (`refs/remotes/origin/HEAD`) are detected via `%(symref)` and never deleted or rewritten — `update-ref` would dereference a delete through the symref and remove the branch behind it.

The copy only runs when its invariants provably hold; otherwise it returns false and the local-fetch fallback (which moves objects as well as refs) runs:

- `.git` must be a real directory (no gitfile worktrees);
- `objects/info/alternates` must contain an entry for this mirror's `objects` directory — the copied refs are bare name→sha pairs, so without the alternate every one of them would dangle;
- `extensions.refstorage` must be unset or `files` — a reftable repository ignores a written `packed-refs` file entirely.

Why packed-refs instead of `update-ref` for everything: `update-ref` validates every written ref's object through mmap'd pack pages, so on a cold mirror it costs the same as the fetch. Cold-cache benchmark (20k-ref mirror on a loop device, dropped caches, readahead off), byte-identical resulting ref sets:

| approach | wall time | block read IOs | read volume |
|---|---|---|---|
| local `git fetch` (current) | 2.2s | 10,533 | 41 MiB |
| `update-ref --stdin` all refs | 2.7s | 10,388 | 40 MiB |
| direct packed-refs write | 0.045s | 339 | 1 MiB |

On Ceph at ≥1ms effective read latency this removes ~10k serialized round trips per job — the 1–4 minute "Fetching the repository" tail observed at peak.

Semantics notes:
- Peel lines/traits are intentionally omitted from the generated packed-refs (peeling every annotated tag costs one cold object read per tag); git peels lazily on use instead.
- `FETCH_HEAD` is not written by the direct copy, and a successful copy deletes any stale `FETCH_HEAD` left by an earlier checkout in a reused workspace. The deliberate semantic is "absent, never stale": nothing in the action or runner reads `FETCH_HEAD` after checkout. When the caller's verification of the requested ref/commit fails, the targeted network fetch runs as before (and writes its own).
- Git's connectivity verification of every tip is skipped. This is sound because the copy is gated on a verified alternate to the mirror whose own sync fetch ran that connectivity check over these exact refs; any failure still falls back to the old local fetch.

## Purging legacy refs/pull/*

Second commit: mirrors no longer carry `refs/pull/*` at all (`purgePullRefs`).

- Since the mirror-first sync, pull refs are never synchronized (a job needing one fetches it directly into its workspace), but mirrors still carry every pull ref they ever accumulated — on one large production mirror ~40k of ~60k total refs are dead `refs/pull/*`. Every one of them is walked by git's `mark_complete_local_refs` inside every sync fetch: in a verbose production run the delta fetch of just 3 changed refs spent 3.27s in `mark_complete_local_refs` + 1.56s in `consume_refs`, dominated by these dead refs.
- `syncMirrorFromRemote` now deletes all `refs/pull/*` (one `update-ref --stdin` transaction — ref database only, no object access) before the changed-ref fetch, so the same job's fetch already walks the smaller set. The purge counts as a mirror change so the sticky disk is committed even when branches/tags were already current; after the first purge it is a no-op.
- `ensureMirror` also purges right after the initial `clone --mirror`, so new mirrors start without pull refs (the clone still downloads them; the now-unreachable objects go away at the next mirror gc).

## Keeping the mirror commit-graph current

Third commit: the mirror always has an up-to-date commit-graph.

- Reading commit-graphs is default-on in git, but writing only happens during a real gc. Our maintenance is `gc --auto`, which is a no-op below thresholds (~6700 loose objects / 50 packs), and neither `clone --mirror` nor `fetch` writes one by default — so a mirror has no commit-graph from hydration until the first threshold-tripping gc, and it goes stale between gcs. The commits git parses inside every sync fetch (`mark_complete_local_refs`, negotiation walks) are then scattered cold pack reads instead of lookups in one compact mmap'd file.
- `ensureMirror` now runs `commit-graph write --reachable` after the initial clone, and the sync fetch passes `-c fetch.writeCommitGraph=true` (incremental split chain, cost proportional to the commits just fetched). Both verified against git 2.34 (runner version); the graph is a pure cache, so a failed write is a non-fatal warning.

## Tolerating refs deleted mid-sync

Fourth commit (moved here from #46): a ref deleted on the remote between `ls-remote` and the batched `fetch --stdin` makes git abort the whole fetch with `couldn't find remote ref` (the failure happens at advertisement matching, before any transfer). `parseMissingRemoteRefs` extracts the vanished refs from stderr, they are pruned from the refspec list and the batch is re-run immediately (up to `MAX_VANISHED_REF_RETRIES = 5` rounds, no backoff — the ref is gone, waiting won't help); vanished refs still present locally are deleted alongside other remotely-deleted refs, and the sync + sticky-disk commit proceed. Observed in production as ~0.2% of syncs on a busy repo aborting on their ephemeral `trunk-temp/pr-*` merge-queue branches.

## Single-attempt sync with one total deadline

Fifth commit: sync failure is soft (the workspace is populated from the mirror's last good state plus a targeted fetch of the job's own ref, and the next job's sync picks up the refs), so burning checkout time on retries is a bad trade. Previously a struggling sync could spend up to 3 × 120s fetch attempts plus backoff inside the checkout step — at peak, timed-out syncs were a visible part of the p99 checkout tail. Now `ls-remote` and the sync fetch run exactly once (`retryHelper` removed; the vanished-ref re-runs above are not time-based retries).

`syncMirrorFromRemote` establishes a single deadline at entry: `ls-remote` and every fetch invocation (including vanished-ref reruns) receive `timeout <remaining>` drawn from that shared budget, so the sync's worst case is 120s total regardless of how many subprocesses run.

## Robustness follow-ups (review feedback)

- `purgePullRefs` never fails its caller — a purge error can't discard a completed hydration clone.
- `fetch.writeCommitGraph=true` is only passed when the mirror already has a commit-graph, keeping the sync-fetch write incremental; mirrors without one get their initial graph off the critical path (after the initial clone, or in the post step), under a timeout, non-fatally.
- The generated packed-refs file is written to a temp file and renamed into place, so a failed write can't leave a truncated file behind.
- `copyRefsFromMirror` gating (alternates, ref backend, real `.git` directory), symbolic-ref preservation, stale-`FETCH_HEAD` removal, and the single total sync deadline described above.

## Testing

- Unit tests for `mapMirrorRefToWorkspace`, `buildRefCopyInstructions` (prune, changed-only updates, symref preservation, non-branch/tag refs, empty inputs), `buildPackedRefsContent`, and `parseMissingRemoteRefs`; full suite passes (143 tests).
- New real-git suite `__test__/mirror-ref-copy-git.test.ts`: fresh workspace (exact refs, connectivity via `fsck` + `rev-list --objects --all`, lazy annotated-tag peel, no `FETCH_HEAD`), reused workspace (reconcile changed/pruned refs, `origin/HEAD` survives `remote set-head`, stale `FETCH_HEAD` removed), missing/foreign alternates and reftable each refuse the copy and succeed through the local-fetch fallback.
- Real `fetch-depth: 0` integration coverage in the Blacksmith CI workflow: fresh checkout verified for exact ref parity against `ls-remote`, tag peeling and connectivity; reused checkout pre-seeded with `origin/HEAD`, a stale remote-tracking ref, and a stale `FETCH_HEAD`, verified afterward.
- Cold-cache block-IO benchmark above; not yet benchmarked on a Blacksmith runner — pending an A/B run on a comparable repo (large ref count, cold sticky disk).


Link to Devin session: https://app.devin.ai/sessions/a3b42ef15226438faf3f9cdde9662918
Open in Devin Desktop: https://app.devin.ai/desktop/session/a3b42ef15226438faf3f9cdde9662918?variant=devin
Requested by: @piob-io

<!-- codesmith:footer:staging -->
---
<a href="https://staging.blacksmith.sh/useblacksmith/codesmith/checkout/pr/47"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v2.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-light-v2.svg"><img alt="View with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v2.svg"></picture></a> <a href="https://stagingbackend.blacksmith.sh/track/enable-autofix?expires=1790460229&installation_model_id=8&pr_number=47&repository=useblacksmith%2Fcheckout&return_to=https%3A%2F%2Fgithub.com%2Fuseblacksmith%2Fcheckout%2Fpull%2F47&signature=9dab27ae3abe2681dbd8964ea894a0dd0b3b88a42a7924b86e12b74eec42ac1e"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-light.svg"><img alt="Autofix with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"></picture></a>
<sup>Need help on this PR? Tag <code>@codesmith-bot</code> with what you need. Autofix is disabled. (Staging)</sup>

<!-- codesmith:autofix:disabled -->
<!-- /codesmith:footer:staging -->

<!-- codesmith:footer -->
---
<a href="https://app.blacksmith.sh/useblacksmith/codesmith/checkout/pr/47"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v2.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-light-v2.svg"><img alt="View with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v2.svg"></picture></a> <a href="https://backend.blacksmith.sh/track/enable-autofix?expires=1790460233&installation_model_id=2&pr_number=47&repository=useblacksmith%2Fcheckout&return_to=https%3A%2F%2Fgithub.com%2Fuseblacksmith%2Fcheckout%2Fpull%2F47&signature=affd2087c4a8e32c8978689bc76e908a8787f8e3804e38ca54958fb8b296779f"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-light.svg"><img alt="Autofix with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"></picture></a>
<sup>Need help on this PR? Tag <code>@codesmith-bot</code> with what you need. Autofix is disabled.</sup>

<!-- codesmith:autofix:disabled -->
<!-- /codesmith:footer -->
