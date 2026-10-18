# Add FAB upload button and improve dev upload UI in ProtestVideoGallery

### Motivation

- Improve developer-only upload UX so devs can easily add original, uncompressed videos from their phone. 
- Provide a persistent, accessible shortcut to open the file picker from anywhere on the page for faster uploads.

### Description

- Import `FaPlus` and replace the inline upload CTA with a clearer plus-focused control and updated instructional copy in `ProtestVideoGallery.jsx`. 
- Update the developer upload button to show a circular `FaPlus` icon, change labels to `Tap + to add videos`, and clarify that uploaded files retain original quality. 
- Add a fixed floating action button (FAB) that uses `fileInputRef` and is only rendered when `isDev` is true to trigger the file picker; the FAB includes an `aria-label` and disabled styling tied to `isUploading`. 
- Preserve existing drag-and-drop, file input, and upload flow, while adjusting styles and copy for clarity.

### Testing

- No automated tests were run as part of this change.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a5a632821988329aa92ab96b793f65e)
