# Move system prompt to websocket message

Move `systemPrompt` from URL query parameters to a post-connect websocket message to prevent URL size limits.

The previous implementation could lead to `session_settings` becoming too large for URL query parameters, particularly when a `systemPrompt` was included. This change aligns `systemPrompt` handling with `builtinTools` and `tools`, which are already sent via a post-connect websocket message.

---
<a href="https://cursor.com/background-agent?bcId=bc-cd7fe1b4-2247-499b-980b-42d7bb1ef335"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-cursor-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-cursor-light.svg"><img alt="Open in Cursor" src="https://cursor.com/open-in-cursor.svg"></picture></a>&nbsp;<a href="https://cursor.com/agents?id=bc-cd7fe1b4-2247-499b-980b-42d7bb1ef335"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-web-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-web-light.svg"><img alt="Open in Web" src="https://cursor.com/open-in-web.svg"></picture></a>
