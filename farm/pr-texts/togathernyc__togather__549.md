# feat(events): templates library UI + item editors (Phase 2)

## Event templates — Phase 2 (frontend)

Builds the **frontend** for the per-location (per-GROUP) event templates
feature on top of the Phase 1 model + CRUD (no backend changes). Leaders can
create/rename/delete **task templates** and **run-sheet templates** and edit
each template's items — reusing the existing Event Tasks grid and run-sheet
editor rather than duplicating them.

### What's included
- **Templates library** (`TemplatesLibraryScreen`, route
  `/rostering/[group_id]/templates`): two sections (Task templates / Run-sheet
  templates), each listing templates with item counts, a "+ New …" row, and
  per-row rename/delete (⋯ / long-press). Leader-gated.
- **Task-template editor** (route `.../templates/task/[template_id]`): renders
  the plan **`EventTasksGrid`** wired to the task-template-item mutations, with
  the same phase/segment + multi-select team/role editing and a tap-to-rename
  header.
- **Run-sheet-template editor** (route `.../templates/runsheet/[template_id]`):
  reuses the run sheet editor's row/cell building blocks + shared
  `GridScrollList`, wired to the run-sheet-template-item mutations
  (add/edit/delete/duplicate/reorder, When/Dur/Owner-Role/Notes/Song). Clock
  times are omitted (templates hold durations only).
- **Entry point**: a "Templates" item in the roster grid's ⋯ overflow (beside
  Cross-team).

### How grids were reused vs extracted
- **Event Tasks grid — reused verbatim.** `EventTasksGrid` never reads `planId`,
  so template items are adapted to its `PlanTask` shape and its callbacks wired
  to the template mutations. The id-brand mismatch (template item vs plan task)
  is bridged with localized casts at the container boundary — **zero change to
  the shared grid**, so plan Event Tasks is untouched.
- **Run sheet editor — extracted shared parts (DRY).** The presentational,
  plan-agnostic row/cell editors (`WhenPill`, `DurationCell`, `NotesEditor`,
  Who/Notes/Song modal bodies, `AddButton`, segment types/`ItemPatch`) moved
  from `RunSheetScreen` into a new `RunSheetItemEditors` module used by **both**
  the plan run sheet and the template editor. `RunSheetScreen` now imports them
  — same props, no behavior change; plan-specific clock times / service ranges
  stay in the screen.

### Regression risk
- Main risk is the `RunSheetScreen` extraction. The move is mechanical and
  `tsc` is clean; the plan run sheet uses the extracted components with
  identical props. **Not runtime-verified** (no simulator) — worth a quick
  manual smoke of the plan run sheet.

### Explicitly deferred to Phase 3/4
Plan↔template linkage, propagation, save-to-template, and plan-side pickers —
this phase is library + item editors only.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01GSwZmWmrY1LisZYjSZYx49
