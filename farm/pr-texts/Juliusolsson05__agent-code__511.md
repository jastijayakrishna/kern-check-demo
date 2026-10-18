# feat(renderer): live transcript window + memory instrumentation + raw-payload compaction

Closes #375.

The renderer's per-session runtime grew without bound on the live path: initial history loads 120 entries and older pages load 200, but every live jsonl burst appended forever (`[...baseEntries, ...appended]`), and several side structures (tool indices, seen-uuid sets, raw semantic/debug payload rings) never shrank. This PR bounds the live transcript window by count, makes what's trimmed reloadable, instruments every structure the investigation flagged, and stops retaining raw event payloads by default. Hibernation of background agents is deliberately out of scope (deferred by design).

## Part A — memory instrumentation

- New `performance/memoryInstrumentation.ts`, driven by a 30s interval in `useIpcSubscriptions` (separate from the 1 Hz ghost sweep — sweep cadence is a correctness knob, gauge cadence a cost knob).
- Per-session gauges (`renderer.session.memory.*`): entries count + byte estimate, semantic history/log byte estimates, feed-debug ring length, ghost map size, tool_use/tool_result index sizes, seen-uuid + trimmed-uuid set sizes.
- Global gauges: code-block registry size; Monaco model count via a probe registry (`lib/code/monacoModelProbe.ts`) registered from inside `getMonaco()` — instrumentation can never force the Monaco lazy chunk, and the workspace hook's module graph never imports `monaco-editor` (which the renderer vitest project cannot even resolve).
- Byte estimates sample ≤64 evenly-spaced items and extrapolate. Ingest-time accounting would tax the hot append path and need decrement bookkeeping at every trim/reload site; full stringify per tick is the exact workload being instrumented. A trend gauge only needs order-of-magnitude fidelity.

## Part B — the live entries window (the core)

New `session-runtime/liveEntryWindow.ts` + wiring in the jsonl burst handler:

- Trim fires when `entries.length > MAX_LIVE_ENTRIES` (2000, deliberately generous) down to `TRIM_TO_LIVE_ENTRIES` (1500) — hysteresis so the index rebuild + ledger recompute is paid ~once per 500 appends.

Trim-safety constraints (each one load-bearing):

1. **`totalEntries` is never decremented** — it is the on-disk denominator; `entries` was always documented as a window over it.
2. **Ownership bound**: the trim boundary stays strictly older than the oldest `semantic.history` turn's `startedAt`, `currentTurn.startedAt`, and every un-superseded ghost's `updatedAt`. Trimming a live turn's committed owner would defeat committed-ownership suppression and re-paint duplicates — the #165/#191/#344 regression class. Superseded ghosts don't protect (they're already scheduled for GC). Optimistic rows are never trimmed.
3. **uuid guard**: any uuid-less entry anywhere freezes the window. Uuid-less entries can't reload dedupe-safely through pagination, and the ledger's `entry:ingest-${index}` fallback ids (comment updated in `observations/committed.ts`) assume unshifted indices — a front-trim would re-key a retained uuid-less entry into an id previously owned by a different entry (the phantom-duplicate React-key class). In practice every mapped entry carries a uuid, so this is a freeze-don't-corrupt failsafe.
4. **Pagination reload**: all three ingest sites (live burst, initial history, older history) now stamp the mapper's `historyMarker` on each entry as a non-enumerable symbol rider — chosen over a parallel uuid→marker map because a rider dies with the entry (no new unbounded structure, no extra lifecycle plumbing) and is invisible to JSON.stringify (debug bundles, byte sampling). On trim, `historyOldestMarker` advances to the oldest retained entry's marker and `hasOlderHistory` flips true; if no retained marker exists the trim aborts rather than strand the region.
   **Asymmetric dedupe**: live ingest treats seen ∪ trimmed as already-seen (a resume bootstrapTail replay must not re-append old rows at the tail); the older-history path lets trimmed uuids back through, releasing them from the set as they reload. Trimmed-uuid bookkeeping fol
