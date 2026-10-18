# fix(schema): normalize Windows path separators in generated meta

## Summary
- Normalize `path.relative()` results with `.replaceAll("\\", "/")` for loader, section, and app block keys
- Normalize `filePath` in `toBase64()` calls for `@Props` definition keys (sections and apps)

On Windows, `path.relative()` returns backslash separators (e.g., `site/sections\Content\Faq.tsx`), which contaminates manifest block keys and base64-encoded schema definition keys. This causes the CMS sections editor to fail schema lookups, preventing sections from opening when clicked.

## Test plan
- [ ] Regenerate schema on Windows and verify manifest keys use forward slashes
- [ ] Verify `@Props` base64 definition keys match between `$ref` paths and `definitions` entries
- [ ] Confirm clicking sections in the CMS opens the section editor form

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated description by cubic. -->
---
## Summary by cubic
Normalize Windows path separators in generated schema/meta, single-decode decofile block keys, and correctly resolve props from mapped types. Fixes CMS editor lookups, wrong-file saves, and empty schemas for utility-type props.

- **Bug Fixes**
  - Force forward slashes in `path.relative(...)` and `file:///...` base64 keys for loader, section, and app blocks.
  - Build decofile keys with one `decodeURIComponent` via `singleDecodeBlockName` so studio `encodeURIComponent` round-trips to disk filenames.
  - Resolve `@Props` from mapped/utility types by falling back to `getDeclarations()[0]` and guarding AST node access.

<sup>Written for commit 772e120f1f2abdddf840d8757458bf7483b5f60e. Summary will update on new commits.</sup>

<a href="https://cubic.dev/pr/decocms/deco-start/pull/270?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="Review in cubic" src="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"></picture></a>

<!-- End of auto-generated description by cubic. -->


