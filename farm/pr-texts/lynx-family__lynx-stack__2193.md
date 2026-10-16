# fix: Normalize x-input number filtering

`x-input` number handling now keeps the inner input as text with `inputmode="decimal"` while filtering invalid characters internally. This supports values like `1.2` and strips invalid input like `1.2a` without setting the `input-filter` attribute.

## Changes Made

- Apply internal numeric filtering for `type="number"` without setting `input-filter`.
- Keep the inner input type as `text` and preserve `inputmode="decimal"`.
- Added a dedicated fixture for `attribute-type-number-inner-input-type`.
- Updated the numeric input test to validate `1.2a` filters to `1.2`.
- Added a patch changeset for `@lynx-js/web-elements`.

## Testing

- Not run (not requested in this update).

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
