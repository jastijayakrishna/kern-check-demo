# fix(vscode): handle paths with illegal chars in error diagnostics

Fix `UriError: Scheme contains illegal characters` by always constructing file URIs with `Uri.file(...)` in `vscode-error-diagnostics`.

The previous implementation used `Uri.parse(...)` on raw file paths, which could interpret parts of a Windows path (e.g., `C:`) as an invalid URI scheme, leading to crashes when handling error diagnostics. This change ensures file paths are correctly treated as file URIs.

---
<p><a href="https://cursor.com/agents/bc-9eee9004-45a1-4977-9e63-0635686e6acd"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-9eee9004-45a1-4977-9e63-0635686e6acd"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</p>
