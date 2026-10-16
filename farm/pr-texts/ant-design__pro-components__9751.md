# feat(form): export layout APIs and document form grid surface

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

ProForm layout/shell API cleanup (#9751): tree-shaking, `createProFormField` / `useProFormFieldShell`, removed `warpField`, Form.Item pick/omit helpers.

**Breaking:** `warpField` removed — use `createProFormField` (**recommend major semver**).

## Types API review (dedicated pass)

### Already done before this review
- `ProFormInstance` from `BaseForm/typing` in Dependency + SchemaForm runtime files
- `ProFormItemProps` single source in `FormItem/typing.ts`
- Form entry exports `pickProFormItemProps` / `omitProFormItemProps` / `proFormItemPropKeys`
- `ProFormGridConfig`, `CommonFormProps`, `BaseFormProps`, `ProFormRef`, etc. on form entry

### This review — changes
- **Form entry:** explicit re-exports for `ExtendsProps`, `ProFormItemCreateConfig`, `ProFormFieldRemoteProps`, `FieldProps`, and full Schema helper types (`FormSchema`, `FormFieldType`, `ItemType`, `ProFormPropsType`, shell `UseProFormFieldShellOptions`, …)
- **BaseForm types:** `ProFormInstance` / `ProFormRef` / `SyncToUrl` from `BaseForm/typing`; `CommonFormProps` / `BaseFormProps` from `BaseForm/BaseForm` (clearer than `BaseForm` barrel)
- **Tighten:** `proFormFieldKey?: React.Key`; `ProFormFieldItemProps.children?: React.ReactNode`
- **Docs:** `docs/internal/form-types-api.md` + link from `form-architecture.md`
- **Fixture:** `scripts/fixtures/published-types/pro-form-shell-types.tsx`

### Follow-ups (not in PR)
- Extract `CommonFormProps` / `BaseFormProps` to a types-only module (reduce type↔runtime coupling)
- Replace Schema `getFieldProps` / `getFormItemProps` / `label: any` with stricter generics
- Dedupe `secondary` between `ExtendsProps` and `ProFormFieldItemProps`
- Remove deprecated `FiledContextProps` alias (major)

## Tree-shaking

`ProFormText` ~47KB / 9 form modules — `checkFormTreeShaking.mjs` passes.

## Verdict

Ready for maintainer review — confirm **major** for `warpField` removal.

> Submitted by Cursor
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-607b3d71-9430-5cea-9bbd-12da738bd913?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-607b3d71-9430-5cea-9bbd-12da738bd913&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
