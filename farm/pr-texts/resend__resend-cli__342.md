# feat: add message_id to sent email get/list output

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Add `message_id` to sent email CLI output, matching the API and Node SDK.

## Changes

- **`resend emails get`**: `message_id` in help text example and interactive `Message-ID:` line
- **`resend emails list`**: `message_id` in help text example
- **Test**: `message_id` in get command mock/assertion
- **Skills**: `message_id` in `emails get` / `emails list` output examples (so agents parsing `--json` know the field exists)

No webhook or receiving code changes — those already pass through `message_id` from the API.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-adf426f4-650c-4b12-a769-03f62d8f92f9"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-adf426f4-650c-4b12-a769-03f62d8f92f9"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Add `message_id` (RFC 5322 Message-ID) to sent email CLI output for parity with the API and the `resend` Node SDK. Helps correlate sent emails with provider logs.

- **New Features**
  - `resend emails get`: prints Message-ID in interactive output; help JSON includes `message_id`.
  - `resend emails list`: help JSON includes `message_id`.

- **Refactors**
  - Documented `message_id` in `skills/resend-cli` examples and bumped skill version to `2.3.1`.
  - Scope remains `message_id`-only; no webhook or receiving changes.

<sup>Written for commit 3529a62bf5447c4469ba9548e3966e2ea34cea45. Summary will update on new commits.</sup>

<a href="https://cubic.dev/pr/resend/resend-cli/pull/342?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="Review in cubic" src="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"></picture></a>

<!-- End of auto-generated description by cubic. -->
