# Add privacy-oriented stripped web display mode

### Motivation
- Provide an embeddable, privacy-oriented presentation that reveals only a compact view of the buffer when desired, for use cases that should not expose full text content to the embedding page or observers.
- Ensure embedding clients can opt in to limited copy behavior and that Stripped Plover integration and candidate UI are handled safely under the privacy mode.

### Description
- Add `renderStrippedDisplayText(text, limit = 9)` to `src/webCore.ts` to emit only the rightmost nine Vietnamese syllables, preserve short non-Vietnamese tokens, and replace longer non-Vietnamese segments with an ellipsis.
- Add an embedding API `window.setStrippedDisplay({ copyAllowed?: boolean })` and integrate stripped-mode rendering and candidate selection behavior in `src/main.ts`, including skipping the redundant top candidate and preventing the raw-text escape hatch while stripped mode is active.
- Enforce stripped-mode UI adjustments via CSS in `static/index.html` to hide Plower controls and show the blank yellow active-Plover state, and document the new API and behavior in `README_WEB.md`.
- Add unit tests for `renderStrippedDisplayText` in `tests/webCore.test.ts` and adjust copy handling so `Ctrl+C` respects `copyAllowed` and returns the intended buffer in stripped mode.

### Testing
- Ran unit tests with `npm test -- --runInBand`, all test suites passed (5 suites, 73 tests).
- Built the frontend with `npm run build`, which completed successfully and produced `static/script.js`.
- Ran `git diff --check` (no style errors reported) and attempted a Puppeteer screenshot, but Chromium could not start in this environment due to a missing system library (`libatk-1.0.so.0`), so no screenshot was produced.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a5a218c371c832ea42d6a2a249888a5)
