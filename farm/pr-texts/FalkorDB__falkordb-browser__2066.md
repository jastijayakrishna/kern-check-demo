# Improve UDF library panel expansion and function-to-code navigation

This change improves UDF browsing UX by making library expansion content-first and wiring function clicks directly to the corresponding location in the library source viewer. Expanded library context is now prioritized in the panel, and function discovery is actionable.

- **Library expansion behavior**
  - Track expansion at panel level so the most recently expanded library is treated as the active expanded section.
  - Give expanded library content a minimum vertical footprint (`>=40%`) so function lists are meaningfully browsable.
  - Load/select library source when expanding a library, so the right pane reflects the active library immediately.

- **Function click → editor navigation**
  - Convert function rows from static text to interactive controls.
  - Add `selectedUdfFunction` to UDF context state to carry function-intent from sidebar to editor view.
  - On function click, ensure the library is selected, then trigger navigation intent for that function.

- **Editor-side function location**
  - Capture Monaco editor instance and react to function selection intent.
  - Introduce a focused locator utility (`findFunctionLine`) to resolve function names to line numbers across common declaration forms:
    - `function name(...)`
    - `const name = (...) => ...`
    - `name: function (...) ...`
  - Center/reveal the resolved line in the main file viewer.

- **Navigation utility (new)**
  - Added a small dedicated helper plus tests for line resolution behavior:
    - `app/udf/functionNavigation.ts`
    - `app/udf/functionNavigation.test.ts`

```ts
const lineNumber = findFunctionLine(selectedUdf[5], selectedUdfFunction);
if (lineNumber) {
  editor.setPosition({ lineNumber, column: 1 });
  editor.revealLineInCenter(lineNumber);
}
```

<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes #2059
