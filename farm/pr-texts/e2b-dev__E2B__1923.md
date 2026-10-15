# fix(js-sdk): treat WatchHandle.stop() as a clean watch end

## Summary

Squashed version of community PR https://github.com/e2b-dev/E2B/pull/1912 by @harshitgavita-07. Fixes #1895.

`WatchHandle.stop()` aborts the watch stream. The abort surfaced as a Connect cancellation, which was mapped to `TimeoutError` and passed to `onExit`, so every user-initiated stop looked like a request timeout. The handle now records the stop, and a stream error that arrives after it ends the watch cleanly:

```ts
async stop() {
  this.stopped = true
  this.handleStop()
}

private async *iterateEvents() {
  try { for await (const event of this.events) ... }
  catch (err) {
    if (this.stopped) return
    throw await handleRpcErrorWithHealthCheck(err, this.checkHealth)
  }
}
```

The suppression covers only the stream iterator, so `onEvent` rejections still reach `onExit`, including ones raised after `stop()`. After `stop()`, `onExit` is called asynchronously with no argument, which matches what async Python `AsyncWatchHandle.stop()` passes (#1480). This is now documented in the JSDoc on `stop()` and `WatchOpts.onExit`.

Tests in `packages/js-sdk/tests/sandbox/files/watchHandle.test.ts` cover three cases:
- a clean exit after `stop()`
- stream errors when the watch was not stopped
- an `onEvent` error thrown after `stop()`

Includes an `e2b` patch changeset.

Not covered: aborting through `opts.signal` still reports a `TimeoutError`. That behaviour predates this PR and is left for a follow-up.

Link to Devin session: https://app.devin.ai/sessions/410788c120d144ed87242ce3b1eb22f7
Open in Devin Desktop: https://app.devin.ai/desktop/session/410788c120d144ed87242ce3b1eb22f7?variant=devin
<!-- devin-review-badge-begin -->

---

<a href="https://app.devin.ai/review/e2b-dev/e2b/pull/1923" target="_blank"><picture><source media="(prefers-color-scheme: dark)" srcset="https://static.devin.ai/assets/gh-devin-review-dark.svg?v=4"><img src="https://static.devin.ai/assets/gh-devin-review-light.svg?v=4" alt="Devin Review"></picture></a>
<!-- devin-review-badge-end -->
