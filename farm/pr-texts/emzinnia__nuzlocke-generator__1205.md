# Fix custom areas being dropped on state restore

## Bug and impact
Custom encounter areas were silently dropped whenever app state was restored through JSON import or undo/redo history sync. Users who saved custom areas and then imported a run, or moved through history states containing custom areas, would lose that user-entered data.

## Root cause
The `customAreas` reducer read from `replaceWith.areas` / `syncWith.areas`, but the state field is named `customAreas`. Those restore paths always fell back to `[]`.

## Fix
Read `customAreas` during `REPLACE_STATE` and `SYNC_STATE_FROM_HISTORY`, and add focused reducer tests for direct updates, import restore, and history sync restore.

## Validation
- `npm run test:run -- src/reducers/__tests__/areas.test.ts src/store/__tests__/persistence.test.ts src/utils/__tests__/nuzlockeJson.test.ts`
- `npm run typecheck`
- `npm run test:run`

<div><a href="https://cursor.com/agents/bc-c90615d9-981c-485f-86e3-aa0f6eba7b16"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/automations/d352b560-b9d6-489e-8516-491096482ea6"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/view-automation-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/view-automation-light.png"><img alt="View Automation" width="141" height="28" src="https://cursor.com/assets/images/view-automation-dark.png"></picture></a>&nbsp;</div>
