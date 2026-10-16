# Standardize tool responses, add tab targeting, confirmations, redaction, and tests

### Motivation

- Provide a single, versioned tool response envelope and builders to make tool outputs deterministic and backward-compatible (`protocolVersion: 2` and legacy `success` boolean). 
- Enable deterministic tab targeting via stable session-scoped IDs and allow tools to operate on explicit `tabId`s or a deterministic active-tab strategy. 
- Require explicit confirmations for policy-gated actions and ensure confirmations are one-time, TTL-bound, and in-memory only. 
- Make audit logs safe by redacting form values, cookies/headers/storage values and URLs with obvious tokens. 
- Add a deterministic, hermetic test harness (Playwright-backed) and CI steps to validate behavior automatically.

### Description

- Added a standard response helper and types in `src/lib/response.ts` and migrated tools to use `ok()` / `fail()` builders while preserving top-level `success` for one-release compatibility. 
- Introduced `src/browser/tabRegistry.ts` and exported it from `src/browser/index.ts` to maintain stable `tabId -> Page` mapping, active-tab selection (prioritizes focused page, then last-focused, then first non-extension), `listTabs()` and `getId()` helpers. 
- Extended tool schemas to accept optional `tabId` and `confirmationId`; updated all page/action tools in `src/mcp/tools.ts` to resolve pages via the new registry and to use the `ok`/`fail` response envelope. 
- Reworked confirmation flow: replaced old pending-action model with `src/policy/confirmations.ts` that stores pending confirmations in-memory (one-time use, TTL), added `confirm_action` (`confirmAction`) and `deny_action` (`denyAction`) tools, and made tools return `NEEDS_CONFIRMATION` errors with `{ confirmationId, actionSummary }` when policy requires confirmation. 
- Hardened audit logging to redact sensitive data via new `src/policy/redaction.ts` and plumbed it into `src/policy/audit.ts` to ensure cookies/headers/form values and token query params are redacted before writing logs. 
- Added tests: `src/tests/audit-redaction.test.ts` (unit tests for redaction) and `src/tests/browser-integration.test.ts` (Playwright integration covering `list_tabs`, `fill_input`, `click`, `screenshot`, policy-block -> `NEEDS_CONFIRMATION` -> `confirm_action` -> action proceeds). 
- Updated `src/mcp/server.ts` to advertise `list_tabs`, optional `tabId`/`confirmationId` inputs, and to expose `deny_action`; changed error serialization to use the new response envelope. 
- Updated `src/test-connection.ts` to exercise `list_tabs` and the active-tab strategy. 
- Updated `package.json` scripts (`test` and `test:milestone1`) to build before running tests, and extended CI (`.github/workflows/ci.yml`) to run tests and install Playwright Chromium with deps in the test job. 
- Updated README to document the `protocolVersion`/`success` contract, `list_tabs`/`tabId` usage, and confirmation flow usage.

### Testing

- Ran `pnpm run test` (builds then runs Node tests): unit tests for redaction and policy tooling passed; overall test runner recorded 9 passes and 1 failing integration test. 
- The failing test is the Playwright integration (`src/tests/browser-integration.test.ts`) which failed locally because Playwright browser binaries were not installed in this environment (error suggests running `pnpm exec playwright install`); CI job includes `pnpm exec playwright install --with-deps chromium` to ensure the integration test runs successfully in CI. 
- Type checking and build were exercised as part of the `test` script (`pnpm run build`) during the run and errors were addressed in this change set prior to adding tests.

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_696bd5c966808333a856f13d90b346b6)
