# feat(events): plan↔template linkage, forward propagation, save-as-template (Phase 3 backend)

## Phase 3 (backend): plan ↔ template linkage, forward propagation, save-as-template

Backend-only. All UI (template pickers, link/switch/save/revert affordances) is deferred to **Phase 4**.

### The model
A plan can LINK to a task template and (independently) a run-sheet template. A linked plan still **owns** its own `eventTasks` / `eventItems` rows — they are **materialized** from the template's items, each carrying a `sourceTemplateItemId` back-pointer. Template edits propagate **forward** to **future** linked plans' still-synced rows; **past plans (eventDate < now) are frozen** and never touched. Per-row overrides + save-to-template are supported.

### Row semantics (both `eventTasks` and `eventItems`)
- `sourceTemplateItemId` set + `templateDetached` falsy → **SYNCED**: propagation updates/deletes it to match the template.
- `sourceTemplateItemId` set + `templateDetached` true → **OVERRIDDEN**: propagation leaves it alone.
- `sourceTemplateItemId` unset → **LOCAL** (plan-owned addition): propagation ignores it.
- template item id in the plan's `detached…ItemIds` → user removed it locally: propagation must not re-add it.

### Forward propagation (`propagateTaskTemplate` / `propagateRunSheetTemplate`)
Called at the end of **every** template ITEM mutation (add/update/delete/duplicate/reorder). For each plan linked to the template with `eventDate >= Date.now()`:
- template item exists + SYNCED row → patch the row to match (all fields, template ordering).
- template item exists + OVERRIDDEN row → leave it.
- template item exists + no row + id not in the plan's detached set → insert a new synced row.
- template item deleted + SYNCED row → delete the row (task completions cascaded via `cascadeTaskCompletions`).
- On a task's role↔team-level flip during a synced patch, stale completions are cleared.

### Freeze-on-date
`setPlan*Template` rejects a plan whose `eventDate < Date.now()`; propagation only considers plans with `eventDate >= Date.now()`.

### Override marking (in existing plan mutations, surgical / guarded on `sourceTemplateItemId`)
- `updateTask` / `updateItem`: editing a template-sourced row sets `templateDetached: true`.
- `deleteTask` / `deleteItem`: records the removed item's `sourceTemplateItemId` in the plan's `detached…ItemIds` so propagation won't re-add it.
- `reorderTasks` / `reorderItems`: detach only rows whose position **actually changes**.
- `createTask` / `createItem`: new rows are plain local (no source tag) — already ignored by propagation, no change needed.
- **No behavior change for plans with no template link** (all paths are guarded on `sourceTemplateItemId`).

### Link / switch / unlink (`setPlanTaskTemplate` / `setPlanRunSheetTemplate`)
- `templateId: null` → unlink: strip source tags from rows (become local), clear pointer + detached set.
- `templateId` set → link/switch: remove currently-synced rows, instantiate the new template's items as fresh synced rows, reset the detached set. `carryover`: `"discard"` drops overridden + local rows; `"copy"` keeps them as plain local rows alongside the new template rows. Same-group enforced. Roster/completions untouched.

### Save-as-template (`saveTaskTemplateFromPlan` / `saveRunSheetTemplateFromPlan`)
- `{kind:"new", name}` → create a template in the plan's group from the plan's current effective list, then link the plan to it (rows become synced).
- `{kind:"existing", templateId, strategy:"replace"|"merge"}` → replace clears + repopulates and relinks the source plan clean; merge appends the plan's list. Both propagate forward to the template's other future plans.

### Revert (`revertPlan*TemplateEdits`)
Drops all of the plan's rows (overridden + local, cascading completions), clears the detached set, and re-instantiates from the linked template. No-op if unlinked.

### Read contract for Phase 4 UI
`getPlanTemplateState({token, planId})` (group-member auth, with `returns` validator) → `{ taskTemplateId, taskTemplateName, hasTaskTemplateEdits, runSheetTemp
