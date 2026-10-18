# perf(properties): parallelise page queries and fix the filter drawer

**Depends on: none**

## Two defects
1. **11 top-level sequential calls, 7 fully independent** (getUser, memberships, counties, states, lists, tags, `listUsers`) → batched into one `Promise.all`. **11 legs → 3.**
2. **`applyFilters()` awaited inside a loop** over active filter blocks, so *every active filter block added another serial round trip*. This is the leading suspect for the filter-drawer slowness operators report.

Also replaced the unread-inbound and open-task ID fan-outs with relationship joins, removing two of the three unbounded full-table queries that were materialising ID lists into the outer `WHERE` clause.

## Known gap — acceptance is incomplete
The **engagement mixed-bucket fallback still materialises an unbounded ID list.** Two of three unbounded blocks are fixed; this one is not. Flagged rather than hidden — a follow-up is required before this cluster can be called done.

## Measurement
Synthetic, at an assumed 50ms/RTT: page 353ms → 51ms, multi-block filters 203ms → 51ms. **That is arithmetic on round-trip counts, not production latency.** No performance win is claimed from it; the preview-vs-preview benchmark runs in the verify phase.

## Verification
- `npm run typecheck` — clean
- `npm test` — 1535 tests across 135 files pass

## Provenance
Code by Codex against a measured work order; committed, verified and opened by Claude (Codex sandbox has no network access).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
