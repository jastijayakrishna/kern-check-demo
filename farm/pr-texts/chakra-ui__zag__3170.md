# fix: handle numeric number input set value

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
Closes #3169

## 📝 Description

Fix number input `api.setValue` when `formatOptions` is defined.

## ⛳️ Current behavior (updates)

Calling `api.setValue` with a number could pass the numeric value into the localized number parser, which expects a string and can throw.

## 🚀 New behavior

Numeric `setValue` arguments are treated as raw numbers before formatting, while string values continue through the localized parser.

## 💣 Is this a breaking change (Yes/No):

No

## 📝 Additional Information

Added a patch changeset for `@zag-js/number-input`.

Verified with:

- `pnpm exec vitest packages/machines/number-input/tests --run`
- `pnpm --filter @zag-js/number-input typecheck`
- `pnpm --filter @zag-js/number-input lint`
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-76f02046-7c42-45a8-944d-d2d3b60249eb"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-76f02046-7c42-45a8-944d-d2d3b60249eb"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
