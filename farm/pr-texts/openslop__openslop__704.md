# perf: nightly performance optimizations 2026-09-01

A source node has no edges and never changes once built, so serializing it is a property of the node. Every dependent was recomputing it instead.

## What was wrong

`nodeIdentity` resolved a source dependency by re-serializing it from scratch:

```ts
return isSourceNode(node)
  ? serializeInputs(nodeInputs(node, results))
  : resultIdentity(results.getElementSnapshot(node.id).result);
```

`serializeInputs` sorts both records with `localeCompare` and `JSON.stringify`s the result. `needsGeneration` calls `nodeInputs`, which calls `nodeIdentity` once per dependency, so every staleness check paid for that on each of the element's source deps — art style, aspect ratio, reference images, voice.

That check is not on a cold path. Per queue notification, and again on every render that reads the queue store, the editor runs roughly five evaluations per element:

| Caller | Sweeps |
| --- | --- |
| `useGenerate` on each element card (`staleReason`) | 1 × per element |
| `SceneGenerateButton` (`pending`, `stale`) | 2 × per element |
| `EditorToolbar` via `useGenerateAll` (`pending`, `stale`) | 2 × per element |

The project-level source nodes are the same four objects for every element in the project, re-sorted and re-stringified each time.

## What changed

`sourceNode()` — the only constructor for source nodes — serializes once and stores the result on the node. `nodeIdentity` reads it back. The type says what was already true in the doc comment: a source node's identity is its inputs, settled when it is built.

## Measurements

Warm (best of 12 rounds), 200 elements with four source dependencies each:

| | before | after |
| --- | --- | --- |
| 5 × 200 `needsGeneration` | 8.3 ms | 3.0 ms |
| 200 × `staleReason` | 1.7 ms | 0.6 ms |
| 4 × 200 `sourceNode()` | 0.05 ms | 0.8 ms |

Construction pays 0.7 ms more per full graph rebuild; evaluation saves 6.4 ms per sweep. A full sweep goes from ~10 ms to ~4.4 ms — from a dropped frame to a fraction of one, on a path that re-runs on every queue tick during a Generate All run and on every keystroke via `useGenerateAll`.

No behavior change: all 1513 tests pass untouched, including `graph.test.ts` and `staleReason.test.ts`.

## Open PR overlap check

Open PRs considered: #701 (BYOK connectors and a third-party gateway) and #703 (nightly maintainability 2026-09-01). This PR touches only `lib/generation/graph.ts`, which neither of them modifies. #701 edits `lib/generation/scriptEdit.ts` and several `lib/generation/__tests__/*` files; its only change to `graph.test.ts` is an unrelated one-line fixture edit, so there is no conflict.

## Skipped

- **`MotionLayer` subscribing to `useCurrentFrame()` when the effect is `none`** (the default). Real, but it is a single-component re-render suppression — the shape closed as trivial on #284.
- **Collapsing `useGenerateScope`'s `pending` and `stale` into one sweep.** `stale` is a strict subset of `pending`, so the second sweep is redundant, but `useSyncExternalStore` needs a referentially stable snapshot and returning both counts as one object needs `useSyncExternalStoreWithSelector` machinery in `createStoreContext`. Not worth the seam change for the remaining half.
- **`isEqual(nodeInputs(...), resultInputs)` in `needsGeneration`.** Now the dominant cost, but replacing the lodash deep compare with a hand-rolled walk trades a clear library call for custom code.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
