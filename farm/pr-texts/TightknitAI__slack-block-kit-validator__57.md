# Add response-only metadata fields to image elements and blocks

## Summary

This PR adds support for Slack's response-only metadata fields on image elements and image blocks. These fields (`image_width`, `image_height`, `image_bytes`, `fallback`, and `is_animated`) are echoed back by Slack in retrieved messages but are ignored on send. By accepting these fields in the schema and types, real Slack payloads will now validate correctly without requiring manual field stripping.

Fixes validation errors when processing actual Slack API responses containing image metadata.

## Type of change

- [ ] Bug fix (non-breaking change that fixes an issue)
- [x] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing behavior to change)
- [x] Schema update (changes to `src/slack-block-kit.schema.json`)
- [ ] Docs / chore (no runtime change)

## Changes

- Added `fallback`, `image_width`, `image_height`, and `image_bytes` fields to `ImageElement` type and schema
- Added `fallback`, `image_width`, `image_height`, `image_bytes`, and `is_animated` fields to `ImageBlock` type and schema
- Updated JSDoc comments to clarify these are response-only metadata fields that are ignored on send
- Added test cases validating acceptance of response-only metadata with correct types
- Added test case validating rejection of response-only metadata with incorrect types

## Testing

- [x] `pnpm test` passes (added test cases in `test/blocks.test.ts` and `test/block-elements.test.ts`)
- [x] `pnpm typecheck` passes
- [x] `pnpm lint` passes
- [x] `pnpm validate-schema` passes
- [x] Added tests covering the new fields with both valid and invalid types

## Schema changes

- [x] Verified against the [Slack Block Kit reference](https://api.slack.com/reference/block-kit)
- [x] Backwards compatible (existing valid payloads still validate; new fields are optional)
- [ ] N/A - not a breaking change

## Checklist

- [x] Commit messages follow [Conventional Commits](https://www.conventionalcommits.org/)
- [ ] N/A - no public API changes to README
- [x] No secrets, tokens, or sample tenant data committed

https://claude.ai/code/session_01LLEAj62CAeFofbDXsgsbxz
