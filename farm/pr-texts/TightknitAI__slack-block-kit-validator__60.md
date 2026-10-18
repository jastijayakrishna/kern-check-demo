# Add validation for single plan block per message

## Summary

Adds a new helper function `checkSinglePlanBlock` to validate that Block Kit payloads contain at most one `plan` block per message. Slack rejects payloads with multiple plan blocks with an `invalid_blocks` error, so this validation catches the issue early.

Closes the gap in validation coverage for the `plan` block type, similar to the existing `checkSingleTableBlock` helper.

## Type of change

- [x] New feature (non-breaking change that adds functionality)
- [ ] Bug fix (non-breaking change that fixes an issue)
- [ ] Breaking change (fix or feature that would cause existing behavior to change)
- [ ] Schema update (changes to `src/slack-block-kit.schema.json`)
- [ ] Docs / chore (no runtime change)

## Changes

- Added `checkSinglePlanBlock` helper function that validates at most one `plan` block exists in a payload
- Integrated the helper into `validateBlockKit` to run alongside other cross-payload validation rules
- Exported the helper from `src/helpers.ts` for public API access
- Added comprehensive unit tests covering zero, one, and multiple plan block scenarios
- Added integration tests to `validateBlockKit.test.ts` verifying the validation is applied
- Added a demo preset (`two-plans`) showcasing the invalid case
- Updated README.md to document the new helper function

## Testing

- [x] `pnpm test` passes — added unit tests in `test/check-single-plan-block.test.ts` and integration tests in `test/validate-block-kit.test.ts`
- [x] `pnpm typecheck` passes
- [x] `pnpm lint` passes
- [x] Added tests covering: no plan blocks, single plan block (valid), multiple plan blocks (invalid), and empty arrays

## Checklist

- [x] Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/)
- [x] Public API changes reflected in `README.md` (added `checkSinglePlanBlock` to helper functions table)
- [x] No secrets, tokens, or sample tenant data committed

https://claude.ai/code/session_01PVtufDFDAZfKgt4bC9RxY6
