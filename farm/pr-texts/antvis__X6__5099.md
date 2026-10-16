# fix(common): preserve caller-owned array paths

### 📝 Description

`ObjectExt.getByPath()` consumes a caller-provided array with `shift()`, and `setByPath()` removes its last element with `pop()`. Reusing the same path can therefore return `undefined` or write to a different property. `Store.getByPath()` exposes the same read-side effect.

Copy array paths before consuming them, matching `unsetByPath()` and the existing Store write path. String paths and delimiter behavior are unchanged. Add regressions for repeated reads/writes, missing properties and the public Store API.

### 💡 Motivation and Context

For `const path = ['attr', 'fill']`, reading `{ attr: { fill: 'red' } }` twice should return `'red'` twice and leave `path` intact. Before this change, the first read empties the array and the second returns `undefined`.

No matching existing PR was found for `getByPath` / `setByPath` during the scoped duplicate search.

### 🧩 Types of changes

- [x] Bug fix
- [x] Test Case

### 🔍 Validation

- Before the fix, defect reproduction on original production code: **the 4 new regression tests failed as expected, 35 existing tests passed**.
- `vitest run __tests__/common/object __tests__/model/store.spec.ts`: **41 passed**.
- Root `tsc --noEmit --pretty false` and `git diff --check`: passed.
- Full-suite recheck at this exact PR head: **3036 passed, 0 failed** across 202 test files; TypeScript passed again. Unchanged upstream under the same environment: **3032 passed, 0 failed**.
- These full rechecks register the real Windows Arial font as the test process's `sans-serif` using `@napi-rs/canvas`. The original unspecified-font run had one `Dom.breakText` assertion failure: this machine measured the string as 174.21px, below the test's 200px wrap threshold; Arial measures it as 248.09px. No production source, test assertions or system font settings were changed for this environment control.
- The optional changed-file Biome lint also reports existing diagnostics, including the unchanged implicit-any `let ret`; a clean repository-wide lint/full-suite run is not claimed.

Codex assisted with audit, reproduction, implementation and local validation. Ready for maintainer review.
