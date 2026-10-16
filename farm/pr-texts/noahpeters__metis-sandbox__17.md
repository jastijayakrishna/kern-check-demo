# Move clamp into its own module

### Motivation
- The `sum` module contained a `clamp` helper that review feedback requested be extracted to improve separation of concerns and module organization.

### Description
- Add `clamp.mjs` exporting `clamp(value, minimum, maximum)` implemented with `Math.min(Math.max(value, minimum), maximum)`.
- Update `sum.test.mjs` to import `clamp` from `./clamp.mjs` and add focused tests for in-range, below-minimum, and above-maximum behaviors.
- Preserve existing `sum` and `multiply` implementations and their tests unchanged.

### Testing
- Ran `npm test` and all 7 tests passed.
- Ran `git diff --check` with no issues reported.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_b_6a94b8c4432c8322b9176b70e4b2c1af)

Metis-Task: noahpeters/metis-sandbox#13
