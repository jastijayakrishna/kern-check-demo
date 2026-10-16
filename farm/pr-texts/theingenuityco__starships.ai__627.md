# feat: File upload URL issue

Fix type guards to correctly handle multimodal content in LLM messages.

Previously, messages with `ContentBlock[]` (e.g., for images and PDFs) were silently dropped due to strict type guards expecting only string content, preventing agents from receiving file URLs.

---
<a href="https://cursor.com/background-agent?bcId=bc-794f2a78-c0d9-4ea8-a7a1-b781af31a54a"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-cursor-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-cursor-light.svg"><img alt="Open in Cursor" src="https://cursor.com/open-in-cursor.svg"></picture></a>&nbsp;<a href="https://cursor.com/agents?id=bc-794f2a78-c0d9-4ea8-a7a1-b781af31a54a"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-web-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-web-light.svg"><img alt="Open in Web" src="https://cursor.com/open-in-web.svg"></picture></a>
