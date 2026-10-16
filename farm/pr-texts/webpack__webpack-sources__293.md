# fix: keep scope bindings through CachedSource replays and cached data

**Summary**

Follow-up to #275, now rebased onto `main`. This PR includes what was #294.

`scopes` broke as soon as a `CachedSource` was composed a second time, which is how webpack uses its modules:

```js
const module = new CachedSource(new OriginalSource(code, "lib.js", bindings));
new ConcatSource(module, "\n").map({ columns: true, scopes: true }).scopes; // "BCAAA,…"
new ConcatSource(module, "\n").map({ columns: true, scopes: true }).scopes; // before: undefined
```

Three problems, one commit each:
1. **Replay dropped the bindings.** `CachedSource.streamChunks` replays a cached entry through `streamChunksOfSourceMap`, and a map only keeps the encoded `scopes` string, not the bindings its sources declared. Fix: while a `scopes` request fills an entry, record the bindings by source index, and pass them to `onSource` on replay. An entry filled without streaming (`map()`, `sourceAndMap()`) never saw them, so a `scopes` request streams the original once to record them.
2. **The persistent cache dropped them.** `getCachedData()` didn't carry the recorded data, so a source restored from webpack's persistent cache needed its original to report bindings, and one restored without an original couldn't. Fix: include the data in the buffered map entries. Nothing is added unless a `scopes` request was made, so other cached data is unchanged.
3. **Replayed maps weren't byte-identical.** Found by the new tests. The cached map also holds the names its own `scopes` field appended. `streamChunksOfSourceMap` reports all of a map's names, so the parent's `names` came out in a different order than on a fresh build. The bindings were the same, but the map bytes differed between a cold build and a cached one, which changes content hashes. Fix: record how many names the stream itself reported, and replay with only those.

The recorded data is `BufferEntry.scopes = { bindings, names }`. Requests without the `scopes` option take the same code path as before.

**What kind of change does this PR introduce?**

fix

**Did you add tests for your changes?**

Yes, in `test/scopes.js`.

A matrix of webpack-shaped compositions:
- concatenated modules;
- a module without bindings between two with them;
- prefixed modules;
- a replaced module;
- a cached chunk of cached modules;
- a cached module bundling two sources, whose source indices are remapped in the bundle.

Each composition is checked for `map` and `sourceAndMap`, with and without `columns`:
- **Correct:** the field equals the one `util.scopes.addScopesToSourceMap` decodes from a map built without caching or the option.
- **Replay:** repeated builds on the same cached modules emit byte-identical maps, without streaming any module again.
- **Restore:** a build from `CachedSource`s restored from `getCachedData()` emits the same maps. It's checked directly and after a `v8.serialize` round-trip, with originals that throw if they're used.
- **Cleared caches:** after `clearCache()` the field is built again correctly.

Plus single cases:
- a `map()`-filled entry records its bindings with one re-stream;
- a restored module whose data holds no bindings streams its original once;
- data from requests without the option gains nothing.

The tests catch both earlier states: against #275 alone, 19 fail; with only the first two fixes, 9 fail (the names order). The full suite passes: 89,968 tests under `node --test` on Node.js 22, and under Jest on Node.js 20, 16 and 10.

**Does this PR introduce a breaking change?**

No. Cached data gains an optional `scopes` field on entries, and only after a `scopes` request.

**If relevant, what needs to be documented once your changes are merged or what have you already documented in this PR?**

Nothing.

**Use of AI**

Claude Code found these while reviewing #275 and wrote the fixes and tests.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ThsbPWvW5vnYWEaFs2Q22F

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Bug Fixes**
  * Cached source-map requests now preserve scope bindings and reported map names when reused or restored from serialized cache data.
  * When cached data lacks scope information, the source is streamed to collect it before replay, helping ensure scope results remain accurate.
  * Scope information is retained across repeated map requests and cached compositions, including when cache data is cleared and restored.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
