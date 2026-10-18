# Add Stripped Display (compact IME view) with UI, logic, and tests

### Motivation
- Provide a compact, IME-oriented "Stripped Display" mode suitable for embedding pages or console-driven demos that shows only the most relevant Vietnamese syllables and suppresses full UI controls.
- Ensure the compact view preserves copying of the full underlying buffer when allowed and visibly hides raw-mode and full Stripped Plover controls.
- Improve candidate presentation for IME embeddings by omitting candidate 1 when alternatives exist and by logging diff regions for debugging and host-side rendering.

### Description
- Introduces a runtime API `window.setStrippedDisplay({ copyAllowed?: boolean })` and a `strippedDisplay` state toggle in `src/main.ts` that drives UI class toggles and rendering behavior. 
- Implements compact rendering behavior changes in `updateDisplay` including candidate omission/offset, placeholder wave emoji for empty buffers, conditional candidate panel visibility, candidate diff region logging, and gated Ctrl+C copying based on `copyAllowed`.
- Adds `stripVisibleTextSegments` in `src/webCore.ts` to truncate non-Vietnamese runs and retain at most the nine rightmost piecemeal syllables, and integrates it into the visible-segment rendering path when stripped mode is enabled.
- Adds styling for the stripped display to `static/index.html`, includes a Puppeteer-based browser interaction test script `scripts/stripped-display-e2e.js`, registers the test in `package.json` as `test:stripped-display`, and extends `tests/webCore.test.ts` with unit tests for `stripVisibleTextSegments`.

### Testing
- Added unit tests for `stripVisibleTextSegments` in `tests/webCore.test.ts` that validate leftmost retained syllable selection and separator-abbreviation rules. 
- Added an automated browser interaction suite `scripts/stripped-display-e2e.js` that exercises empty-state behavior, nine-syllable truncation, separator abbreviation, whole-buffer copying semantics, raw-mode suppression, candidate diff rendering and Stripped Plover blanking, which is runnable via `npm run test:stripped-display`.
- No automated tests were executed as part of this rollout; the change includes the new tests and scripts for CI or local execution.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a5a2c56bdd4832ebb3968153aabcbfb)
