# Python compilation path delay

Set Python program state to `COMPILING` during initial file download to match C compilation behavior and fix #414 .

Previously, when a Python program was run for the first time, the UI immediately showed "Stop" while Python runtime files were downloading, leading to a confusing user experience. This change ensures the UI displays a "Loading Python..." message and the button reflects a `COMPILING` state until the Python environment is ready.

This can be verified using network throttling in the browser's developer tools.

---
<a href="https://cursor.com/background-agent?bcId=bc-87bce499-40e6-42c1-a8e2-71d03d432b0b"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-cursor-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-cursor-light.svg"><img alt="Open in Cursor" src="https://cursor.com/open-in-cursor.svg"></picture></a>&nbsp;<a href="https://cursor.com/agents?id=bc-87bce499-40e6-42c1-a8e2-71d03d432b0b"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-web-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-web-light.svg"><img alt="Open in Web" src="https://cursor.com/open-in-web.svg"></picture></a>
