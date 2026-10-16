# ♻️ Update category action button icons and fix alignment to left column

## Description

The Orphaned/Unmigrated button icons were non-associative, and all 3 buttons were full-width centered instead of aligned to the left content column.

- Replace Orphaned icon: `BiUser` → `PiPuzzlePiece` (🧩)
- Replace Unmigrated icon: `BiLinkExternal` → `BiPause` (⏸️)
- Move `<CategoryActionButtons />` inside `TinaHomepageWrapper` children so it renders within `layout-main-section` (left column only)

## Screenshot (optional)

**Before:** Buttons centered full-width below both columns with person/external-link icons
![before](https://github.com/user-attachments/assets/1cfa3cb0-db09-4b89-af3e-10521ea1caea)

**After (expected):** Buttons left-aligned under the category list column only
![after](https://github.com/user-attachments/assets/434a96d7-ae6f-4a47-b5ac-610bbd0d5552)
