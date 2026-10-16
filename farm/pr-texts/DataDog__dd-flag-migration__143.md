# feat: add configurable tag sync to migrations

## Motivation

Re-migrating existing flags replaced all Datadog tags with source tags, removing tags configured directly in Datadog. Users need control over whether existing tags are preserved or overwritten.

## Changes

- Prompts interactive LaunchDarkly and Eppo migrations to choose:
  - **Merge:** Add source tags while preserving existing Datadog tags.
  - **Overwrite:** Replace Datadog tags with source tags.
- Adds LaunchDarkly `team:*` tags only for teams successfully matched to Datadog teams.
- Keeps overwrite behavior as the non-interactive default for backward compatibility.
- Updates migration guidance and unit tests.

## Test instructions

1. Run `yarn migrate`.
2. Select LaunchDarkly or Eppo and choose a flag already in Datadog.
3. Choose **Merge** and verify:
   - Existing Datadog tags remain.
   - Source tags are added.
   - For LaunchDarkly, only matched teams produce `team:*` tags.
4. Repeat using **Overwrite** and verify Datadog-only tags are removed.
5. Run:
   ```sh
   yarn typecheck
   yarn lint:fix
   yarn test
   ```
   All 972 tests should pass.

## Checklist

- [ ] Updated documentation (README)
- [ ] Tested locally with `yarn migrate` or `yarn evaluate`
- [x] Added or updated unit tests for this change
