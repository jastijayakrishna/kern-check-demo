# fix: generate valid faker schema mocks

Fixes #3747

## Summary
- cast top-level enum schema factories to their own enum array type
- alias schema factory imports when they collide with a per-tag MSW aggregate
- cover the combined tags-split, MSW, faker schemas, and enum configuration end to end

## Validation
- bun run vitest run packages/core/src/writers/split-tags-mode.test.ts packages/core/src/writers/tags-mode.test.ts packages/core/src/writers/mock-outputs.test.ts packages/mock/src/faker/index.test.ts packages/mock/src/faker/getters/scalar.test.ts packages/orval/src/generate-spec.test.ts
- bun run typecheck
- bun run lint
- bun run format:check

This pull request was prepared and submitted by OpenAI Codex acting as an AI agent through the contributor account.

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Fixed enum faker generation to produce correct TypeScript casts for top-level schemas.
  * Prevented naming collisions in generated MSW mocks by assigning safe aliases to conflicting schema factories.

* **Tests**
  * Added coverage for enum-based faker generation.
  * Added regression tests for tagged MSW generation, including schema factory aliasing and mock output.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
