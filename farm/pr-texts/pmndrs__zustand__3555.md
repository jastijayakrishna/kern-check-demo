# fix(persist): clearStorage() should invalidate concurrent async rehydration

With async storage, `clearStorage()` can race with a pending `rehydrate()`: the item is removed, but the older async read completes afterward and writes the cleared value back into state.

`rehydrate()` already uses `hydrationVersion` to discard stale concurrent hydrations — `clearStorage()` simply wasn't advancing that counter.

## Summary

- **`src/middleware/persist.ts`**: Increment `hydrationVersion` at the start of `clearStorage()`. Any in-flight `rehydrate()` then fails the existing `currentVersion !== hydrationVersion` staleness checks and exits without applying state.

- **`tests/persistAsync.test.tsx`**: Five new tests covering:
  - Stale async `getItem` result discarded after `clearStorage()`
  - Stale async `migrate` result discarded after `clearStorage()`
  - Hydration still invalidated when `removeItem` throws
  - `clearStorage()` after a completed hydration does not reset live state
  - `onRehydrateStorage`/`onFinishHydration` callbacks suppressed for stale hydration; subsequent `rehydrate()` works correctly

Close #3554
