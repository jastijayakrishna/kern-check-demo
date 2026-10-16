# fix: linting errors

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

`biome check .` reported three `lint/suspicious/useAwait` warnings in `src/adapter.ts` for async methods that never await:

- `initialize`
- `fetchThread`
- `fetchMessages`

This removes the `async` modifier from those methods and returns resolved promises instead, keeping the `Promise` return signatures unchanged for the Chat SDK.

Since `initialize` now throws synchronously when the API key is missing (identical behavior for callers that await it), the corresponding test was updated to expect a synchronous throw instead of a rejection.

## Verification

- `pnpm lint`: 0 warnings
- `pnpm typecheck`: clean
- `pnpm test`: 96/96 passing
<!-- CURSOR_AGENT_PR_BODY_END -->

[Slack Thread](https://resend.slack.com/archives/C0AG3A0TP7W/p1786389403535059?thread_ts=1786389403.535059&cid=C0AG3A0TP7W)

<div><a href="https://cursor.com/agents/bc-b5855e7e-3b52-5e26-94ab-ff4fb0bee7d2?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-b5855e7e-3b52-5e26-94ab-ff4fb0bee7d2&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
