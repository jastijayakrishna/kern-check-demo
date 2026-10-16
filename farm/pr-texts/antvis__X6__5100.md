# fix(model): traverse descendants in depth-first order

### 📝 Description

Make the default `Cell.getDescendants()` traversal visit each child's subtree before the next sibling. The current implementation appends every immediate child first, then appends their descendants, despite the API documenting depth-first order.

For `parent -> [first, second]`, `first -> [child, sibling]`, and `child -> [grandchild]`, the expected order is `[first, child, grandchild, sibling, second]`.

### 💡 Motivation and Context

Build the result separately and append one child together with its descendants. The explicit breadth-first and shallow branches are unchanged. Add regressions for the default order, BFS, `deep: false`, leaf cells and unchanged parent/child relationships.

This corrects the documented default ordering. Deep clone/subgraph consumers may observe the corrected list order; membership is unchanged. Existing PR #5039 concerns removal of orphan children and changes a different method.

### 🧩 Types of changes

- [x] Bug fix
- [x] Test Case

### 🔍 Validation

- Before the fix, defect reproduction on original production code: **the new DFS regression failed as expected, 17 other tests passed**; the BFS/shallow controls passed.
- `vitest run __tests__/model __tests__/plugin/selection.spec.ts`: **323 passed**.
- Root `tsc --noEmit --pretty false` and `git diff --check`: passed.
- Full-suite recheck at this exact PR head: **3035 passed, 0 failed** across 202 test files; TypeScript passed again. Unchanged upstream under the same environment: **3032 passed, 0 failed**.
- These full rechecks register the real Windows Arial font as the test process's `sans-serif` using `@napi-rs/canvas`. The original unspecified-font failure was a font-width assumption in the unchanged `Dom.breakText` test (174.21px text versus a 200px wrap threshold). Arial measures it as 248.09px. No production source, test assertions or system font settings were changed for this environment control.

Codex assisted with audit, reproduction, implementation and local validation. Ready for maintainer review.
