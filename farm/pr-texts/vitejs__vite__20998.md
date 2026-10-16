# fix: handle query parameters for `/@vite/*` modules

- [x] Fixed issue in clientInjections.ts by using cleanUrl(id)
- [x] Added test case that imports `/@vite/env?foo` to verify the fix
- [x] Moved test to dev-only plugin per feedback
- [x] Built and linted successfully
- [x] CodeQL security check passed

## Issue Summary
The issue (#20997) is in `/packages/vite/src/node/plugins/clientInjections.ts`. When query parameters are appended to the env entry URL (e.g., `/@vite/env?token=xxx`), the strict equality check fails, causing `__DEFINES__` to not be replaced, resulting in a ReferenceError.

## Solution
- Import `cleanUrl` from `../../shared/utils`
- Use `cleanUrl(id)` to strip query parameters before comparing with `normalizedClientEntry` and `normalizedEnvEntry`
- Created a dev-only plugin in `playground/define/vite.config.js` that adds the test import during transformation
- The plugin uses `apply: 'serve'` to ensure it only runs in development mode

## Testing
The test imports `/@vite/env?foo` via a plugin that only applies during dev mode, ensuring the fix works correctly without affecting build behavior.

<!-- START COPILOT CODING AGENT SUFFIX -->



<details>

<summary>Original prompt</summary>

> Fix https://github.com/vitejs/vite/issues/20997 by using `cleanUrl(id)`. Add a test to https://github.com/vitejs/vite/tree/main/playground/define that imports `/@/vite/env?foo` and ensures that the error does not happen.


</details>



<!-- START COPILOT CODING AGENT TIPS -->
---

💬 We'd love your input! Share your thoughts on Copilot coding agent in our [2 minute survey](https://gh.io/copilot-coding-agent-survey).
