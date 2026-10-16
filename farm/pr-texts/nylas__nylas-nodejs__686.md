# feat(folders): Updated Folders.find method to support optional queryParams.

<!-- Add information about your PR here -->
Fixes #685

This PR enhances the `Folders.find` method to support optional `queryParams`.

**Why this change?**
The existing `Folders.find` method did not accept `queryParams`, unlike other resource `find` methods (e.g., `Messages.find`, `Events.find`). This update aligns `Folders.find` with the SDK's consistent pattern, making it more robust and ready for future API extensions that might introduce query parameters for fetching folders.

**Changes include:**
- Added `FindFolderQueryParams` interface.
- Updated `FindFolderParams` to include an optional `queryParams` property.
- Modified `Folders.find` to accept and pass `queryParams` to the base `_find` method.
- Added a new test case to verify `find` with `queryParams`.

# License
I confirm that this contribution is made under the terms of the MIT license and that I have the authority necessary to make this contribution on behalf of its copyright owner.

---
<a href="https://cursor.com/background-agent?bcId=bc-295625f1-9db4-4cea-be8e-8cca60980dfb"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-cursor-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-cursor-light.svg"><img alt="Open in Cursor" src="https://cursor.com/open-in-cursor.svg"></picture></a>&nbsp;<a href="https://cursor.com/agents?id=bc-295625f1-9db4-4cea-be8e-8cca60980dfb"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-web-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-web-light.svg"><img alt="Open in Web" src="https://cursor.com/open-in-web.svg"></picture></a>
