# fix(core): backfill resource id on hydrated messages

Fixes #18559.

This updates MastraDB message hydration so `resourceId` is filled from `memoryInfo` independently from `threadId`. Previously, messages that already had a `threadId` skipped the `resourceId` backfill.

I added a focused regression test for a restored message that already has `threadId` but is missing `resourceId`.

Checks run:
- pnpm --filter ./packages/core test src/agent/message-list/conversion/input-converter.test.ts
- pnpm --filter ./packages/core test src/agent/message-list/conversion/input-converter.test.ts src/agent/message-list/tests/message-list.test.ts
- pnpm --filter ./packages/core check
- git diff --check

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## ELI5
When MastraDB restores a saved message, it should be able to remember which “resource box” it belongs to. This PR fixes hydration so that even if the message already has its “thread/conversation ID,” it will still fill in the missing “resource ID” from `memoryInfo`.

## What changed
- Fixed `hydrateMastraDBMessageFields` so `resourceId` is backfilled independently of whether `threadId` is missing.
- Kept any existing `threadId` intact while hydrating missing `resourceId` from `context.memoryInfo?.resourceId`.
- Added a regression test for a restored message that already has `threadId` but lacks `resourceId`, asserting that `resourceId` is restored and that unnecessary ID/createdAt generation is not triggered.
- Added a changeset entry for a patch release to `@mastra/core`.

## Notes
- This targets restored DB message conversion so resource-scoped memory/history association is preserved.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
