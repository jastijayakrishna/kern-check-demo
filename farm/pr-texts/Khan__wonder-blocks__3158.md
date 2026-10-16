# Fix useCachedEffect refetching with unmemoized onResultChanged

## Summary

Issue: FEI-8109

Fixed `useCachedEffect` entering an endless refetch loop when an unmemoized `onResultChanged` callback is passed with the `CacheAndNetwork` or `NetworkOnly` fetch policies.

## Changes

- **Use `useLatestRef` for `onResultChanged`**: The callback is now tracked via a latest-value ref so its identity no longer invalidates the memoized fetch function. This prevents cancellation and restart of inflight requests when the callback's identity changes between renders.
- **Remove `onResultChanged` from dependency array**: Since the callback is accessed via ref, it's no longer needed in the memo's dependencies, preventing unnecessary fetch restarts.
- **Preserve callback invocation semantics**: The most recently supplied `onResultChanged` callback is still invoked when a result arrives, maintaining the expected behavior for callers who update the callback between renders.

## Implementation Details

The fix uses `useLatestRef` from `@khanacademy/wonder-blocks-core` to maintain a reference to the latest `onResultChanged` callback without affecting the memoized fetch function's dependencies. This allows the fetch logic to invoke the current callback while preventing identity changes from triggering fetch cancellation and restart cycles.

Added test coverage to verify:
- Inflight fetches are not restarted when callback identity changes
- The most recently supplied callback is invoked with results
- Previously supplied callbacks are not invoked after being replaced

Includes a patch changeset for `@khanacademy/wonder-blocks-data`.

https://claude.ai/code/session_01Firs1rBtyAXz4LJKGB1wbZ
