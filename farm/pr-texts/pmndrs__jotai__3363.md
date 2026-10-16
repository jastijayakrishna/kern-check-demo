# fix(unwrap): prevent infinite microtask loop on rejected source recompute

`unwrap` could spin indefinitely when a rejected source atom recomputed (e.g. an observable error causing a sync throw after a pending promise rejection). The `catch {}` guarding `prev = get(promiseAndValueAtom)` always reset `prev` to `undefined` after a rejection, so `promise !== prev?.p` was perpetually `true`, re-attaching `.then` handlers and calling `triggerRefresh()` in a tight microtask loop that starved the event loop.

## Related Bug Reports or Discussions

#3362 

## Summary

- **Root cause**: `promiseAndValueAtom` threw cached errors directly, making `prev` always `undefined` on the next read, which re-attached promise handlers on every cycle
- **Fix**: Store rejections as `{ p: promise, e: error }` state instead of throwing from the internal atom. The `prev.p === promise` guard short-circuits subsequent reads for the same rejected promise, preventing handler re-attachment. The error is rethrown only from the public atom — observable behavior is unchanged and the #3162 recovery fix is preserved
- **Test**: Added regression test reproducing the exact loop scenario (mounted subscriber + sync throw after pending rejection)

## Check List

- [ ] `pnpm run fix` for formatting and linting code and docs
