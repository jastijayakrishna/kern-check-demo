# fix: suppress marquee long-press sampling

## Summary
- suppress canvas Sampling Session when touch long-press starts inside an active Marquee while Selection is active
- preserve outside-Marquee, no-Marquee, non-Selection, and non-touch sampling behavior
- mark issue 139 done and refresh task/platform tracking docs

## Tests
- bun run check
- bun run test -- src/lib/canvas/editor-session/tab-state.svelte.test.ts src/lib/canvas/canvas-interaction.svelte.test.ts
