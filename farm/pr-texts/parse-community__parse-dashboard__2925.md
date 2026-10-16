# feat: Add hyperlink support in Views table

## Summary
- handle `Link` objects when calculating column widths
- display link values as `<a>` elements in Views

## Testing
- `npm run lint`
- `npm test` *(fails: dashboard e2e › can keep mount path on redirect)*

------
https://chatgpt.com/codex/tasks/task_e_687ae204a51c832d93b1723d6a625462

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Added support for displaying `Link` data types as clickable links in data tables.
  * Links open in a new tab and handle both relative and absolute URLs for improved navigation.

* **Enhancements**
  * Improved display of `Link` values by showing user-friendly text instead of raw objects.

* **Documentation**
  * Updated README to explain rendering of `Link` and `Pointer` types in view tables, including examples for relative and absolute URLs.
  * Added guidance on sanitizing data to prevent XSS vulnerabilities.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
