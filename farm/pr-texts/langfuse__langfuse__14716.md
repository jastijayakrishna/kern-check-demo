# fix(trace): comfortable peek defaults, unify inner-split persistence (LFE-10601)

## TL;DR
The trace **peek** opened with worse defaults the bigger your screen — a very wide tree and a cramped info panel — and the tree/info ratio reset between tabs. This makes the peek open at a **comfortable, screen-aware default** (info wide, tree bounded, list still navigable) and **remembers your inner split in `localStorage`** like it already does the outer width. Scoped to the peek; the full-page trace view is untouched.

## Why
Two independent, separately-persisted resize systems stack in the peek:
1. **Outer width** — `0.5 × viewport`, so on a 2560px+ monitor the peek was ~1280px+ and kept growing.
2. **Inner tree ↔ info split** — a *share-based* 60% tree / 40% info, persisted in **per-tab `sessionStorage`**.

Because the tree was a *percentage of an already-large peek*, "bigger screen → bigger tree": at 2560px the tree was ~768px and info a cramped ~512px. And per-tab storage is why the split felt inconsistent between tabs and between people (one long-lived tab vs. many "open in new tab" tabs).

## What
- **Outer width — cap the default's px growth.** Default = `min(0.5·vw, PEEK_MAX_DEFAULT_WIDTH_PX)`, floored at the drag minimum. Normal laptops keep 50vw (zero change ≤ ~2800px); wide monitors stop ballooning so the underlying list stays navigable. User drags still go up to 90%.
- **Inner split (peek only) — anchor to comfort, give extra to info.** Give the info panel a comfortable target and hand the tree the remainder, clamped to a comfortable band, so extra width on a wide peek flows to the *content* (info), not the *index* (tree).
- **Unify persistence → `localStorage`.** The peek's inner split now persists cross-tab under a peek-scoped group id, matching the outer width. The full-page trace view keeps its own share-based, per-tab layout.

## Result (verified in-browser across widths)
| Viewport | Peek width | Tree | Info |
|---|---|---|---|
| 2560 | 1280 (50%) | **459** (was ~768) | **819** (was ~512) |
| 3440 | **1400** (capped, was 1720) | 460 | 940 |
| 1512 (laptop) | 756 (50%, unchanged) | 339 | 415 |
| 1280 | 640 | 278 (min-area) | 360 |
| 1100 | 550 | 260 (rail-min + horizontal scroll preserved) | 360 |

Dragging the inner split now survives reload and new tabs (localStorage). Small screens still collapse gracefully (260/360 mins + 40px rails + horizontal-scroll pin). Annotation mode is a separate `traceContext`, so none of the peek-scoped changes apply there.

<details>
<summary>Engineering detail</summary>

- **Why a computed percentage, not a px `defaultSize`.** react-resizable-panels resolves a px `defaultSize` to a percentage against whatever group width it measures *first* — on a peek that's a transient mid-open width, and the library then persists it. In practice the same laptop resolved to 316px one load and 394px the next. Percentages are width-independent, so the default is deterministic. `TraceLayoutDesktop` computes the split from the width the peek will actually open at (`resolveEffectiveWidthFraction() × innerWidth`) and passes it as the group `defaultLayout`.
- **Peek scoping.** `isPeekMode` (from `ViewPreferencesContext`) selects a peek group id (`trace-layout-peek-v1`) + `localStorage` + the computed default; everything else keeps `trace-layout-v2` + `sessionStorage` + 60/40. The full-page trace view would otherwise get a ~2000px-wide info panel on a 4K monitor.
- **Untouched:** the collapse rails, the both-panels-min horizontal-scroll pin (LFE-10550), the annotation-mode collapse + save-suppression.
- **Tests:** `peekPanelStore.clienttest.ts` covers the viewport-aware capped default (normal / wide / ultra-wide / saved-preference-wins). Split behavior verified in-browser at the five widths above + drag-persistence across reload.

**Design calls made (open to change):** persistence is **global** (consistent with every existing trace preference — `showGraph`, `logViewMode`, … — which are all global `localStorage`); **view-mode memory (timeline vs tree) deferred** to keep this scoped to the
