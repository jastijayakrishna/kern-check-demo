# Defer Android inference render when model is ready; passthrough Ctrl/Alt/Meta hardware keys

### Motivation
- Avoid flashing raw V7 in the WebUI when Android hardware-key inference is synchronous and the native model is already `ready` so the UI should wait for the native result instead of briefly showing raw text. 
- Ensure OS-level modifier keys (Ctrl/Alt/Meta) are not consumed by the V7 engine and instead are passed through to the OS/hardware input handling.

### Description
- In `src/main.ts`, modify `runInference()` to conditionally skip the immediate `updateDisplay()` when running under the Android IME and the model state is `ready` by adding `shouldDeferAndroidInferenceRender()`; this defers flashing raw V7 until the native result arrives. 
- Add helper functions `shouldDeferAndroidInferenceRender()` and `hasOsPassthroughModifier()` and use the latter in `document` key event handlers to ignore events that include `Ctrl`, `Alt`, or `Meta`. 
- Update Android IME (`ime-android/app/src/main/java/.../V7ImeService.java`) so `dispatchHardwareKeyEvent` returns `false` (not routed to WebView/V7) when `Ctrl`, `Alt`, or `Meta` are pressed. 
- Extend the Android IME end-to-end script (`scripts/android-ime-e2e.js`) with cases that validate modifier passthrough and that ensure when the model is `ready` the WebUI does not render raw V7 while a native inference result is pending. 
- Small test/auxiliary edits to support assertions in the E2E script and to keep preexisting behavior when the model is `loading` or `error`.

### Testing
- Unit test suite: ran `npm run build && npx jest --runInBand` and all unit tests passed (`5` suites, `72` tests passed). 
- Build: `vite build` succeeded during test runs. 
- Android IME E2E: `npm run test:android-ime` could not complete in this environment because Puppeteer/Chrome failed to launch due to a missing system library (`libatk-1.0.so.0`), so the browser-driven E2E could not be executed here. 
- Lint/format: attempted to run `npx prettier` on changed JS/TS files (JS/TS files formatted); Java file skipped by Prettier parser which was noted but does not affect runtime tests.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a5cc8496954832e82ccb7f6208f47c0)
