# test: add kernel utility coverage

## Summary
- add regression tests for editor kernel utilities and event registration
- cover system detection helpers across node, browser, and server contexts
- scope vitest coverage to core runtime modules and enforce 80% thresholds

## Testing
- npm run test:coverage
- npm run type-check

------
https://chatgpt.com/codex/tasks/task_e_68eb60c45688832a9ff376e7c42063dc

## Summary by Sourcery

Add comprehensive regression tests for editor-kernel utility functions, system detection helpers, and event registration, and enforce coverage thresholds on core modules

CI:
- Configure Vitest coverage reporter (text, json-summary, lcov), include core runtime modules, exclude tests, plugins, demos, and enforce minimum coverage (lines 80%, statements 80%, functions 80%, branches 70%)

Tests:
- Add utils.test.ts covering DOM constants, service ID generation, no-op, editor state creation, assertions, DOM-to-lexical mappings, node order comparison, and kernel retrieval
- Add sys.test.ts to cover system detection helpers across Node, browser, and server contexts
- Add event.test.ts to verify event registration utilities
