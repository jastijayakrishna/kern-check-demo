# fix(swimlanes): preserve source order for disconnected nodes

## Root cause

In the default lane-aware layering (`assignLayers_LaneAwareCompact`), every node in a lane gets its own layer, and the node that comes first in the topological order gets the first free layer. Both topological sorts (`topoSortIfAcyclic` for TB, `topoSortByGenerationIfAcyclic` for LR) start from `sortedZeroInDegreeNodes`, which sorts by ID. Nothing constrains nodes without edges after that, so a lane of unconnected nodes comes out in alphabetical order:

```mermaid
swimlane-beta
  subgraph s1
    Sunday
    Monday
  end
```

drew Monday above Sunday.

## Fix

`sortedZeroInDegreeNodes` still sorts by ID, but the slots taken by nodes that have no edges (and aren't groups) are refilled in source order. Connected nodes keep their positions.

I also tried breaking every topological tie by source order. That moved 6 of the 27 swimlane layout fixtures: in `issue-7802-*` and `12/13-disagree-exits-*`, the unconnected `id1` jumped from the bottom of lane X1 to its second row and added a layer. So this PR only changes the order of unconnected nodes.

| develop | this PR |
| --- | --- |
| ![before](https://raw.githubusercontent.com/SwastikTripathi/mermaid/pr-assets/8366/before.png) | ![after](https://raw.githubusercontent.com/SwastikTripathi/mermaid/pr-assets/8366/after.png) |

## Verification

- `__tests__/sourceOrder.spec.ts` parses swimlane source with `Diagram.fromText` and runs `runSwimlaneLayoutCore` with fixed node sizes. It covers the issue's diagram, five nodes in one lane (TB and LR), and unconnected nodes in two lanes. All four tests fail on develop and pass here.
- I dumped every node position for the 27 swimlane DDLT fixtures that have sizes, on develop and on this branch. They're identical.
- Rendered both diagrams above in headless Chrome with a local `build:mermaid` of develop and of this branch. develop puts Monday at `translate(0, 22.5)` and Sunday at `translate(0, 117.5)`. This branch swaps them.
- `vitest run` (331 files, 6700 tests) passes. `tsc --noEmit`, ESLint, Prettier and cspell are clean on the changed files.

Fixes #8355

🤖 Generated with [Claude Code](https://claude.com/claude-code)


<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary
- Preserve source order for unconnected, non-group nodes in swimlane layouts. Connected nodes keep their existing positions.
- Update both swimlane topological-sort helpers to use the graph when selecting zero-in-degree nodes.
- Add regression tests for multiple lane directions and node counts, plus two example diagrams and a patch changeset.

## Testing
Test results are not independently verified. The supplied PR objectives report that the regression tests and project checks pass.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
