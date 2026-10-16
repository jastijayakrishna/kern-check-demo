# feat(js): add `ignoreBrowserExtensionErrors` option

- [x] Understand codebase structure
- [x] Add `ignoreBrowserExtensionErrors` to `BrowserConfig` type in `packages/core/src/types.ts`
- [x] Add default value (`false`) in the browser client constructor
- [x] Add browser extension filter logic into the single built-in `beforeNotify` handler (before `__incrementErrorsCount`), so ignored extension errors don't count against `maxErrors`
- [x] Add tests for the new feature (8 test cases including regression for maxErrors interaction)
- [x] All tests pass (54 browser tests, 132 core tests)
- [x] Reverted unintended `packages/js/package-lock.json` changes
