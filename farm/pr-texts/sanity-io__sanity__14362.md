# fix(form): constrain pte annotation reference picker width and results height

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
### Description

SAPP-3617 / #12975 stopped annotation edit popovers collapsing to auto width by falling through to the popover default. That default was container index 2 (~960px), which overshoots the PTE column (~640px) and, because the nested reference autocomplete is constrained to the popover’s own scroll box, leaves only about one result row of height.

Fixes [SAPP-4329](https://linear.app/sanity/issue/SAPP-4329/studio-pte-reference-picker-annotation-excessively-wide-and-vertically).

Why this shape:
- Changing only the width still leaves the autocomplete clipped to the popover header+field leftover space.
- Using the document pane for every nested popover would re-break portaled dialogs (`referenceHidden`). The insert-menu overflow exception (`EditDialogOuterBoundaryContext`) is the existing pattern: outer pane when it contains the input, otherwise `document.documentElement`.

What changed: default annotation popover width is now container index 1, and reference autocomplete results inside edit dialogs/popovers use that overflow exception.

### What to review

- `PopoverModal.tsx` / `ObjectEditModal.tsx` — popover default width 1 (~640px), matching the PTE column and dialog default. Explicit `options.modal.width` is unchanged.
- `useReferenceAutocompletePopoverBoundary.ts` — edit-dialog overflow exception. Same-dataset, GDR, and cross-dataset autocompletes share this hook.
- Confirm we did not reintroduce the SAPP-3617 auto-width collapse (unspecified width still resolves to a real container width, not `[]`).

### Testing

- Unit tests in `ReferenceAutocomplete.test.tsx` for the edit-dialog boundary cases (outer contains input; portaled popover; no outer boundary). `pnpm vitest run --project=sanity` on those files: 17 passed.
- Existing `_getModalOption` tests still cover the SAPP-3617 unspecified-width case (`[1]`, not `[]`).
- Desktop verification in test studio on a `ptReference` annotation (measured popover width 906px → 648px; visible autocomplete rows 1 → 6).

Before (popover ~906px, one result row):

[Before: annotation popover about 906 pixels wide](https://cursor.com/agents/bc-2458251d-1ebd-445d-88ba-5e92dba20675/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fbefore_annotation_popover_too_wide.webp)
[Before: autocomplete shows one result row](https://cursor.com/agents/bc-2458251d-1ebd-445d-88ba-5e92dba20675/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fbefore_annotation_autocomplete_one_row.webp)

After (popover ~648px, six result rows):

[After: annotation popover matches the PTE column width](https://cursor.com/agents/bc-2458251d-1ebd-445d-88ba-5e92dba20675/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fafter_annotation_popover_column_width.webp)
[After: autocomplete shows six author results](https://cursor.com/agents/bc-2458251d-1ebd-445d-88ba-5e92dba20675/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fafter_annotation_autocomplete_six_rows.webp)

[after_pte_annotation_reference_picker_layout-2.mp4](https://cursor.com/agents/bc-2458251d-1ebd-445d-88ba-5e92dba20675/artifacts?path=%2Fopt%2Fcursor%2Fartifacts%2Fafter_pte_annotation_reference_picker_layout-2.mp4)

### Notes for release

Portable Text annotation edit popovers that contain a reference field now use the same ~640px width as the PTE column, and the reference search results list can show several documents at once instead of a single cramped row.

---

<sub>To show artifacts inline, <a href="https://cursor.com/dashboard/cloud-agents#team-pull-requests">enable</a> in settings.</sub>
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-2458251d-1ebd-445d-88ba-5e92dba20675?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-2458251d-1ebd-445d-88ba-5e92dba20675&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
