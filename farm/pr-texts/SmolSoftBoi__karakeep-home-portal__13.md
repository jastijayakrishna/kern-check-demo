# [Chore] add jest-dom matchers

## Context
Need improved Testing Library assertions.

## Changes
- register `@testing-library/jest-dom` in Vitest setup
- verify DOM elements using `toBeInTheDocument` and `toHaveAttribute`

## Testing Done
- `yarn lint`
- `yarn test`


------
https://chatgpt.com/codex/tasks/task_e_68822eb53c108326a4463eb7d84475fd

## Summary by Sourcery

Add jest-dom matchers to Vitest setup and update tests to use improved DOM assertions

Enhancements:
- Register @testing-library/jest-dom in Vitest setup file

Tests:
- Refactor BookmarkList and Header tests to use toBeInTheDocument and toHaveAttribute matchers instead of manual attribute checks

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Tests**
  * Enhanced test assertions for bookmark links and header components to explicitly check for DOM presence and correct attributes.
  * Introduced a global test setup file to enable improved DOM matchers in tests.
  * Updated test configuration to automatically load the setup file before running tests.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
