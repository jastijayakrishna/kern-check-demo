# fix: Update FilePickerOptions onFilesPicked type

# Context
This PR addresses an inaccuracy in the `FilePickerOptions` interface where the `onFilesPicked` callback parameter type did not match the actual data structure received at runtime. Users reported that the callback receives an object with a `files` property, rather than a direct array of `File` objects.

## Why
To ensure type safety and provide an accurate API definition for developers, the `onFilesPicked` callback's parameter type has been updated to correctly reflect that it receives an object `{ files: File[] }`. This prevents type mismatches and eliminates the need for user-side workarounds.

## What
- Corrected the `onFilesPicked` callback parameter type in `src/types.ts` and `src/filePicker.ts` from `(data: File[]) => void` to `(data: { files: File[] }) => void`.
- Updated the `README.md` documentation, including code examples and the parameter description, to reflect the correct callback signature.

## Checklist

Use the checklist below as a guide to ensure your PR is ready for review

- [x] 📝 PR has description (comment /describe to generate a description via the PR agent)
- [x] 🧪 PR includes tests (Existing tests were run and passed)
- [ ] 🪵 PR includes logs
- [ ] 📸 PR includes screenshots demonstrating the impact (eg: UI screenshots, stack diffs, perf improvements etc.)
- [x] 📜 Docs have been updated where relevant (README.md)

---
[Slack Thread](https://stackonehq.slack.com/archives/C08HKKH68V8/p1756924027717739?thread_ts=1756924027.717739&cid=C08HKKH68V8)

<a href="https://cursor.com/background-agent?bcId=bc-86d67ed3-1217-4b0f-a567-cb264d4f4481">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-cursor-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-cursor-light.svg">
    <img alt="Open in Cursor" src="https://cursor.com/open-in-cursor.svg">
  </picture>
</a>
<a href="https://cursor.com/agents?id=bc-86d67ed3-1217-4b0f-a567-cb264d4f4481">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-web-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-web-light.svg">
    <img alt="Open in Web" src="https://cursor.com/open-in-web.svg">
  </picture>
</a>


    
<!-- This is an auto-generated description by cubic. -->
---

## Summary by cubic
Fixes the FilePickerOptions.onFilesPicked type to match runtime. The callback now receives { files: File[] } instead of File[]; docs updated to reflect this.

- **Migration**
  - Update callbacks to onFilesPicked: (data) => { /* use data.files */ }.
  - No runtime behavior changes; this aligns types with existing behavior.

<!-- End of auto-generated description by cubic. -->
