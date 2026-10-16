# Improve error reporting for user-friendly CI/CD output

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Problem

When OpenCheck tests fail in CI/CD (e.g., due to `GraphRecursionError`), the output shows raw stack traces with no context about what went wrong or how to fix it. This makes debugging test failures unnecessarily difficult.

Example of the unfriendly output before this change:
```
GraphRecursionError: Recursion limit of 25 reached without hitting a stop condition...
    at _runLoop (/home/runner/.npm/_npx/.../node_modules/@langchain/langgraph/dist/pregel/index.js:1154:46)
```

## Changes

### 1. `src/agent/agent-factory.ts` — Catch and categorize runtime errors
- Wraps `agent.invoke()` in a try/catch that converts raw exceptions into structured, user-friendly `AgentExecutionResult` messages
- Categorizes common errors: recursion limit, rate limiting, authentication, network errors
- Each category includes an actionable suggestion (e.g., "Increase `recursionLimit` in your config")

### 2. `src/runner/test-runner.ts` — Graceful error handling per test
- Wraps `executeFn()` in a try/catch so that if one test crashes, the remaining tests still run
- Converts thrown errors into failed `TestResult` with error details

### 3. `src/output/reporter.ts` — Better error display
- Shows error details **inline** immediately when a test fails (not just in the summary)
- Multi-line errors are properly indented for readability
- Adds a **Troubleshooting tips** section at the end of failed runs with common fix suggestions

### 4. `src/cli.ts` — Safety net for unexpected errors
- Catches all errors (not just `ConfigLoadError`) with a formatted message and `process.exit(1)` instead of crashing with a raw stack trace

### 5. Bun-only rules and cleanup
- Removed accidentally committed `package-lock.json` (this project uses bun)
- Added `package-lock.json` to `.gitignore`
- Added `.cursorrules` and `CLAUDE.md` with bun-over-npm instructions to prevent this from recurring

### Example output after this change

```
  [FAIL] click each platform tab (ai, 67.3s)
         TEST_FAILED: Agent exceeded the recursion limit (25 steps) while executing this test.
           The test "click each platform tab..." required more steps than the configured limit allows.
           Suggestion: Increase 'recursionLimit' in your config (current: 25), or simplify the test case.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Test Results Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  ...

  Troubleshooting tips:
    • If a test hit the recursion limit, increase 'recursionLimit' in your config...
    • If a test failed with a network error, verify the target URL is reachable...
```

## Tests

All 110 tests pass, including new tests for:
- `GraphRecursionError` → friendly message conversion
- Rate limit and unexpected error handling
- TestRunner continuing after a test crash
- Inline error display in reporter
- Troubleshooting tips rendering
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-1a1c70eb-bb42-4962-862c-03257d902ff1"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-1a1c70eb-bb42-4962-862c-03257d902ff1"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
