# feat(batch): support tags and scheduledAt in batch email options

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

The batch API now supports `tags` and `scheduled_at`. This PR updates the SDK types and tests to reflect that.

## Changes

- **`CreateBatchEmailOptions`**: Removed `scheduledAt` from the `Omit` list so batch emails can be scheduled. `tags` was already available via `CreateEmailOptions`.
- **Tests**: Added coverage for `tags` and `scheduledAt` serialization in batch requests, and extended the template email test to include tags.
- **Changelog**: Added a Tegami changelog entry for a minor version bump.

## Notes

Runtime serialization already worked through `parseEmailToApiOptions` — only the types and test coverage were out of date. Attachments remain unsupported in batch.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-a6f158bf-309a-4915-b0e3-2d7573d0fcd5"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-a6f158bf-309a-4915-b0e3-2d7573d0fcd5"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Add `scheduledAt` and `tags` support to batch emails, enabling scheduled, tagged batch sends. Adds a Tegami changelog entry for a minor `resend` release; attachments remain unsupported.

- New Features
  - `CreateBatchEmailOptions` now includes `scheduledAt`.
  - Added tests for `tags` and `scheduledAt` serialization, including a template email case with tags.

<sup>Written for commit 883fe81c2bf17b8bc13b3bd4712c7188fc0f4633. Summary will update on new commits.</sup>

<a href="https://cubic.dev/pr/resend/resend-node/pull/1022?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="Review in cubic" src="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"></picture></a>

<!-- End of auto-generated description by cubic. -->
