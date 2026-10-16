# feat: surface message_id in email tools

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Surface `message_id` from the Resend API in email tool outputs:

- `get-email` — show Message ID in details
- `list-emails` — include Message ID in each summary line
- `list-received-emails` — include Message ID in each summary line

(`get-received-email` already included it.)

## Test plan

- [x] `pnpm run lint`
- [x] `pnpm test`
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-335d32de-d9ac-4fe0-aa87-3dd168de8609"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-335d32de-d9ac-4fe0-aa87-3dd168de8609"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
