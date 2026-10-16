# Restore five runtime permissions to the normal roles tab

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
# PR

The roles page was grouping five permissions under the deprecated tab even though runtime guards still enforce them. This change moves those permissions back to the normal Permissions tab, grouped by their existing business modules.

## What changed

Removed these codes from the frontend `DEPRECATED_ROLE_PERMISSIONS` list:

- `KNOWLEDGEBASE_EDIT` (AI module)
- `DATA_SOURCE_VIEW` (data module)
- `ORG_INVITE_VIEW` (members module)
- `SUPER_ADMIN_EDIT` (members module)
- `ACCESS_DELETE_ALL_DATA` (members module)

The other six codes stay deprecated: `ADMIN_DASHBOARD_VIEW`, `VIEW_ALL_EMAILS`, `ORG_DEMO_EDIT`, `COPILOT_VIEW`, `CHANGE_SELECTED_ORGANIZATION`, and `ACCESS_DELETE_ACCOUNT`.

Classification tests now require that exact split. The roles workspace test checks tab counts, search, business-module filter, and enabled/disabled filter for both groups. Catalog size and the enabled total stay the same for the same permission records.

## Why

These five codes were marked deprecated in the roles UI on 2026-06-17, but later permission checks still use them. `KNOWLEDGEBASE_EDIT` was added to upload, create, and process-task paths in the 2026-09-01 hardening. `DATA_SOURCE_VIEW`, `ORG_INVITE_VIEW`, `SUPER_ADMIN_EDIT`, and `ACCESS_DELETE_ALL_DATA` also still gate their APIs. The deprecated tab was only a display classification, so the page now follows the runtime checks.

Permission codes, enabled states, default role configuration, API contracts, and backend guards are unchanged. This does not grant any role a new permission and does not change database permission records. Super-admin read-only behavior, the admin limit on administration permissions, and Demo mode hiding of the delete-data permissions stay as they are.

The TRIAL plan's `KNOWLEDGEBASE_EDIT=false` setting and the related upload 403 are a separate policy issue. This pull request does not change that behavior.

## Tests

- `corepack pnpm exec jest --config apps/cloud/jest.config.ts --runInBand` for:
  - `apps/cloud/src/app/features/setting/roles/deprecated-permissions.spec.ts`
  - `apps/cloud/src/app/features/setting/roles/roles-workspace.spec.ts`
  - `apps/cloud/src/app/features/setting/roles/roles-dialog.spec.ts`
- Result: 3 suites, 24 tests, all passed.
- ESLint on the three changed files passed.
- Prettier check passed.
- Browser verification of the roles page was not run in this change.

# Checklist

- [x] Have you followed the [contributing guidelines](https://github.com/xpert-ai/xpert/blob/master/.github/CONTRIBUTING.md)?
- [x] Have you explained what your changes do, and why they add value?

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-4e19d4f1-b74a-522d-8295-75b736c82601?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-4e19d4f1-b74a-522d-8295-75b736c82601&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
