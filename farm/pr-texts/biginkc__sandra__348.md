# perf(metrics): collapse the outbound SMS metrics fan-out — 50.4% of all database time

**Depends on: none**

## The defect
`getOutboundSmsMetrics()` fires 12–13 unscoped `count: 'exact'` queries per call. `getQueueStats()` calls it with **zero scope arguments**, and `use-queue-stats.ts` polls it **every 30 seconds** whenever the Messages cockpit is open — across both Inbox and Outbox tabs.

Measured against production over the 38.7 days since `stats_reset`:

| Metric | Value |
|---|---|
| Share of **all** database time | **50.4%** (44.5M of 88.3M ms) |
| Sequential scans on `messages` | 414,318 |
| Tuples read | 20.59 billion |
| Profile | fast query called constantly — 210–325ms mean, ~14,500 invocations |
| Role | `authenticated` — a browser tab, not a background job |

This was invisible to static search for three investigation rounds because the repo checkout being read was 138 commits behind production.

## The fix
One `outbound_sms_metrics()` RPC using filtered aggregates over a single scan. Read-only prototype: **40.5ms vs ~3,058ms per current invocation (~75×)**.

## Choices made, and why
- **Polling stays at 30s.** Widening to 5 minutes is a one-line change recovering ~90% — but it costs operators up to five minutes of queue staleness. The collapse recovers ~98.7% with *no product-behaviour change*. Strictly better on both axes.
- **No index.** Confirmed with `enable_seqscan=off` that none can help: `channel='sms'` matches 100% of rows, `direction` is 2-valued. Also `max_parallel_workers_per_gather = 1`, so the current 12 concurrent counts contend rather than parallelise.
- **No cache.** Deferred deliberately — it only addresses N-concurrent-operator load, which isn't demonstrated.

## Security
`SECURITY INVOKER`, so RLS continues to enforce tenancy — chosen over `SECURITY DEFINER` specifically to make cross-tenant leakage structurally impossible rather than checked.
- `search_path` pinned to `public, pg_temp`
- EXECUTE revoked from `public`, `anon`, **and `service_role`** (service_role bypasses RLS and would reopen the hole)
- Granted only to `authenticated`
- Every aggregate scoped through the org predicate, not a single membership gate

## Parity
Chicago day boundaries preserved (`OPERATOR_TIME_ZONE` — a UTC boundary would silently shift daily totals), plus per-status counts, schedule min/max, and error handling. Parity assertions and RPC call-count coverage added.

## Verification
- `npm run typecheck` — clean
- `npm test` — 1534 tests across 135 files pass
- **No performance win is claimed yet.** The 75× figure is a read-only prototype measurement, not this code. The preview-vs-preview benchmark under the interleaved A/B protocol runs in the verify phase.

## Provenance
Code written by Codex against a measured work order; committed, verified and opened by Claude because the Codex sandbox has no network access.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
