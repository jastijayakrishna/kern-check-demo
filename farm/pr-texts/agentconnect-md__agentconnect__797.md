# feat(cp): surface session-access refresh-behind failures

Phase 4 of `docs/designs/session-access-cold-visit.md` (§5 last bullet, §8) — follow-up to #792, item 4 of #775. Observability only; no behavior changes.

## The gap

The session-access snapshot cache serves stale entries while refreshing behind the request; `noDeleteOnFetchRejection` deliberately keeps the previous entry serving when that background refresh fails, so a provider blip never empties the answer. But the failure was visible nowhere: the served snapshot still carried its recorded `degraded: false`, nothing was logged, no counter moved. A refresh pipeline broken for minutes looked identical to a healthy one — which #775 called out as the precondition for ever discussing a longer stale window.

## What this adds

- **A structured warn per rejected refresh-behind sweep**, stable message `session access refresh-behind failed — still serving the previous snapshot`, carrying the org id and a cause classification. The cause follows the `slack-session-access.ts` discipline — a CAUSE, never a TARGET: the error's `code` or class name, never its message, so no scope/channel/workspace identifier can ride into the log.
- **The event doubles as the counter.** It fires only for the background class: a cold blocking sweep's failure already surfaces to its caller as an error (unchanged), so counting this message counts exactly the previously invisible failures. Log-based counting is the established precedent on this surface (the Slack degraded-resolve warn, the doorbell per-pull log — design §5); an OTel counter can follow if that proves insufficient.
- **A staleness stamp on the entry**: `refreshFailedAt` is set on the snapshot the failure leaves serving; a refresh that lands replaces the entry, which clears it.

Deliberately untouched: the `REFRESH_BEHIND` options — in particular `allowStaleOnFetchRejection` stays absent, so a caller past the ceiling coalescing onto an in-flight refresh still observes its failure — plus `SNAPSHOT_FRESH_MS` / `SNAPSHOT_MAX_STALE_MS`, fail-closed behavior, and every DTO/UI surface.

## Natural follow-up (not in this PR)

`refreshFailedAt` is recorded but not surfaced. Folding it into `accessSyncDegraded` (or an `accessIssue`) on responses served from a stale-and-failing snapshot is a behavior change: every list/detail/usage consumer would start showing the degraded banner during provider outages that today serve quietly. It would take reading the stamp in the snapshot hand-out path plus a product decision on those banner semantics.

## Tests

Three additions to the existing FakeClock harness in `session-access.test.ts`:
- a refresh-behind rejection emits exactly one warn (org + cause payload asserted exactly, message excluded) and the entry keeps serving the recorded answer, now stamped;
- a subsequent successful refresh clears the stamp, asserted via the replacing entry's fresh answer;
- a cold blocking-sweep failure propagates to the caller as today and emits nothing.

## Verification

- `pnpm --filter @agentconnect.md/control-plane typecheck` — exit 0
- `test:unit` — 1398 passed (138 files)
- `test:int` — 1059 passed (74 files, Testcontainers Postgres), exit code captured explicitly: 0
- `eslint` and `prettier --check` on the touched files — clean

🤖 Generated with [Claude Code](https://claude.com/claude-code)
