# Fix support chat image attachments (blob URL → data URL)

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Fixes support chat attachment failures caused by `blob:` URLs being sent to the API, and fixes the UI so images actually appear in the conversation and clear from the input after send.

## Root cause

1. **API:** `PromptInput` stored attachments as `URL.createObjectURL()` blob URLs. `useChat` passes `FileUIPart[]` through unchanged, so the server received unusable `blob:` references.
2. **UI:** The support chat renderer only handled `text` / tool parts — not `file` parts — so sent images never appeared in the thread.
3. **UX:** Attachments were not cleared after submit, and the send button stayed disabled for image-only messages (`disabled={!input && !status}`).

## Changes

- **`convertFileUIPartsToDataURLs`**: Converts blob URLs to data URLs at submit time in `PromptInput`
- **Server guard**: `/api/ai/support` returns `400` if any file part still has a non-`data:` URL
- **Support UI**: Restrict attachments to `image/*` (screenshots)
- **Clear attachments** after successful submit in `PromptInput`
- **Render `file` parts** as images in the support conversation
- **`SupportPromptSubmit`**: Enable send when text or attachments are present
- **Files-only sends**: Use `sendMessage({ files })` without placeholder text

## Testing

- `bun run typecheck` passes
- Rebased onto latest `beta`

## Note

Can merge independently of #260 (search hardening). If both land, the support route will have both file URL validation and full Zod request validation.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-019f0a53-a520-7c6e-9e92-5c3089c8f7a0"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-019f0a53-a520-7c6e-9e92-5c3089c8f7a0"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
