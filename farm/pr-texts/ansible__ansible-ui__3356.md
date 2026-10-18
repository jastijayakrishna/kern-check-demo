# Batch WebSocket-triggered job fetches with id__in

## Summary

Batch WebSocket-triggered fetch actions in `JobsList.tsx` into a single `GET /unified_jobs/?id__in=<ids>` request instead of firing one request per job. Uses a 500ms debounce window to collect job IDs, with an immediate flush at 50 IDs to keep URLs safe. Falls back to `throttledRefresh()` on batch fetch failure.

### Performance Test

Ran `launch_stress_test.sh` against both `devel` and this branch with 3G network throttling. Network recorded for 5 minutes via HAR capture.

| Metric | Before (devel) | After (batched) | Improvement |
|---|---|---|---|
| Job fetch requests | 45 individual | 2 batched | **96% fewer** |
| Total `unified_jobs` GETs | 70 | 27 | **61% fewer** |
| p95 fetch latency | 9,776 ms | 3,537 ms | **64% faster** |
| Mean fetch latency | 7,448 ms | 2,909 ms | **61% faster** |
| Wall-clock to fetch all jobs | 24.8 s | 5.6 s | **77% faster** |
| List refresh p95 | 2,522 ms | 2,096 ms | **17% faster** |

## Type of Change

- [ ] Bug fix
- [x] Enhancement
- [ ] Tests
- [ ] Documentation
- [ ] Other (please specify)

## Risk Analysis - REQUIRED

- [ ] **High** — Broad platform impact (e.g., SWR config, shared framework components, authentication, routing, API wrappers, build/bundler config). Changes affect multiple workspaces or could cause widespread regressions.
- [ ] **Medium** — Scoped but cross-cutting (e.g., shared utility functions, changes to multiple pages within one workspace, component library updates, test infrastructure). Limited blast radius but touches common code paths.
- [x] **Low** — Narrowly scoped (e.g., single page fix, styling tweak, documentation, test-only changes, copy/string updates). Minimal risk of unintended side effects.

## Dependencies

None. The `id__in` filter is standard Django REST Framework and already supported by the AWX API.

## Testing

### Ephemeral E2E Tests

Once PR is ready and preliminary checks pass, trigger tests by posting a comment `/run-playwright` on this PR.

### Manual Testing

1. Launch 10+ jobs simultaneously
2. Open browser Network tab, filter by `id__in`
3. Confirm batched requests appear instead of individual `id=N` requests
4. Confirm all jobs appear in the list in real time

### Screenshots

N/A — no visual changes.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
