# Default PDF attachments to non-embedded on upload

When dragging a PDF into the editor, it defaulted to the embedded/preview mode. PDFs should be inserted as plain file attachments unless the user explicitly enables the preview.

## Changes

- **`shared/editor/commands/insertFiles.ts`**: Changed `preview: upload.isPdf` → `preview: false` when creating the attachment node, so PDFs are inserted as regular file widgets by default. Added `preview` to the `attrs` option type so callers can override the default. Removed the now-unused `isPdf` field from the upload object.
- **`app/editor/menus/block.tsx`**: Added `preview: true` to the "Embed PDF" block menu item's `attrs`, so PDFs uploaded via the block menu are still shown as embedded viewers.
- **`shared/editor/nodes/Attachment.tsx`**: Updated `replaceAttachment` to preserve the existing node's `preview` state when replacing an attachment.

```ts
// Before
schema.nodes.attachment.create({
  ...
  preview: upload.isPdf,  // true for PDFs → embedded by default
})

// After
schema.nodes.attachment.create({
  ...
  preview: false,  // non-embedded by default; overridden to true by "Embed PDF" block menu
  ...options.attrs,
})
```

The `FileHelper.isPdf()` utility method is retained.

<!-- START COPILOT CODING AGENT TIPS -->
---

📍 Connect Copilot coding agent with [Jira](https://gh.io/cca-jira-docs), [Azure Boards](https://gh.io/cca-azure-boards-docs) or [Linear](https://gh.io/cca-linear-docs) to delegate work to Copilot in one click without leaving your project management tool.
