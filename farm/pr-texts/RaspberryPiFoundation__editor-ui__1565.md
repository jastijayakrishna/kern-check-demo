# fix: stop instructions preview lingering above edit/view tabs

> 🤖 Generated with AI (Claude Code)
> 👨‍💻 Reviewed and steered by @maxelkins

## Summary

- Educators saw a stray rendered copy of the instructions above the Edit/View tabs.
- On refresh the panel renders read-only instructions (injected via `innerHTML`) before the teacher role resolves, then swaps to the editable tabs.
- React reused the same `<div>` for both branches, leaving the injected markup stranded above the tabs.
- Keying the two branch divs forces a remount so the stale content is removed.

Fixes RaspberryPiFoundation/digital-editor-issues#1650

## Changes

- Add distinct `key` props to the read-only and editable-tabs branch divs so React remounts instead of reusing the node.
- Add a regression test covering the `instructionsEditable` false → true transition.

## Note on fix

- This is a minimal fix, it gives the two renders distinct identity without disturbing the Prism/scratchblocks pipeline that relies on imperative `innerHTML`.
- It does treat a symptom of a deeper problem: read-only (Projects site instructions) and editable instructions (Code Classroom) share one component, one `stepContent` ref, and one imperative `innerHTML` effect in the same JSX slot. That combination is what let React reuse the node.
- In the future though we may want two different components that are used in the instruction panel - `ReadOnlyInstructions` / `EditableInstructions`.

## Screenshots

_To be added._
