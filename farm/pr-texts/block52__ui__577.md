# Replace rake percentage free-text input with whole-number dropdown (1–10)

The chain rejects decimal rake percentages (`invalid uint32: 2.5`), but the free-text `<input type="number">` allowed any value, silently blocking table creation. Replaced with a `<select>` restricted to integers 1–10.

## Changes

- **`src/pages/TableAdminPage.tsx`** — swap `<input type="number" step="0.1">` for a `<select>` with options `1%`–`10%`; default remains `5`; updated helper text to reflect the new valid range

<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes #576
