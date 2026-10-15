# fix(cursor): reject getDriverCursor after initialization errors

**Summary**

Fixes #16561.

`getDriverCursor()` currently waits forever when called after a pre-find hook has failed: the stored initialization error is ignored and the `cursor` event will never arrive. Reject with the stored `_error` before registering the event wait.

The existing driver-cursor fast path and pending-initialization behavior are preserved. This adds only a constant-time check when no driver cursor is available, with no timers, extra listeners, or database operations. Skipped middleware behavior is outside this change.

**Examples**

The regression tests use a real rejecting pre-find hook and call `getDriverCursor()` both before and after its error event. On unchanged master, the early call rejects correctly and the late call times out. Both reject with the original error after this fix.

Validation on Node.js 22.17.1 / MongoDB 8.2.3:

- Query-cursor and aggregation suites: **136 passing**.
- ESLint on the changed source and test: passed.
- `git diff --check`: passed.
- Broader `eachAsync` helper tests: 9 passing, 1 timeout. The same `gh-8235` test times out on the unchanged checkout; its source and helper are identical to master. That test runs 1,001 sequential zero-delay timers under a 10-second limit on this Windows host. No test timeout or unrelated implementation was changed.

Developed with AI assistance; the reproduction, patch, and tests were checked against current master.
