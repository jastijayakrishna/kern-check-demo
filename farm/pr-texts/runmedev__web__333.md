# Fix comment range navigation and highlights

## Summary

- Navigate range-comment threads to the exact rendered Markdown text instead of only the owning cell.
- Preserve notebook scroll position when opening a rendered-text comment draft.
- Keep unresolved comment ranges visibly highlighted, with stronger active styling and an accessible range count.
- Map Unicode projection offsets back to precise DOM ranges while retaining cell-level fallback for outdated anchors.
- Center the exact DOM range inside the notebook viewport, retain a whole-cell fallback when mapping is unavailable, and clear active styling whenever the comments panel closes.

## Validation

- `pnpm -C app exec vitest run src/lib/markdown/renderedMarkdownProjection.test.ts src/components/Actions/MarkdownCell.test.tsx src/components/NotebookCommentsPanel.test.tsx src/components/Actions/Actions.test.tsx` — 107 tests passed.
- `pnpm -C app exec vitest run` — 847 tests passed across 88 files.
- `runme run build test` — passed.
- Local Drive-backed CUJ: selecting the thread moved its exact range from 6306.5–6325.5 px outside an 806 px viewport to 704.5–723.5 px; opening a draft kept `scrollTop` at 5602; after the native selection collapsed, the persistent highlight remained visible.

Validation notebook: [20260820_0601_comments_ux_fix_validation.ipynb](https://runme.gateway.unified-0.internal.api.openai.org/?doc=https%3A%2F%2Fdrive.google.com%2Ffile%2Fd%2F1dMlZOI4VIHLUNN0jRzXCx7_HQGZH72Cc%2Fview)

