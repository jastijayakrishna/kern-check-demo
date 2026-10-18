# fix(resource-editor): keep single-value property text selectable (DEV-7034)

Fixes [DEV-7034](https://linear.app/dasch/issue/DEV-7034/single-value-property-fields-text-cant-be-selectedcopied-click).

## Problem

In the resource editor, text in a **single-value** property could not be selected with the mouse, so it could not be copied. Any mousedown on the value immediately entered drag/reorder mode. Multi-value properties were unaffected.

## Root cause

Drag enablement and drag-handle rendering encoded the same invariant — *"this row is draggable"* — in two independent places in `property-values.component.ts`, and they disagreed at exactly one value:

- `showHandle` = `canReorder && values.length > 1`
- `dragDropDisabled` = `!canReorder || …` — **no value-count gate**

So for an editor on a single-value property, drag was enabled while no `cdkDragHandle` was rendered. In `@angular/cdk/drag-drop`:

- `DragRef._pointerDown` falls back to the root element as the drag surface when `_handles.length === 0`, so mousedown anywhere in `.value-row` starts the sequence.
- `_initializeDragSequence` calls `DragDropRegistry.startDragging()` **on mousedown, before the 5px drag threshold**.
- `startDragging` registers a global *capturing* `selectstart` listener bound to `_preventDefaultWhileDragging`, which `preventDefault()`s while any drag instance is active.

Text selection was therefore cancelled at the first mousedown, whether or not the row ever actually moved. Multi-value rows were fine because `withHandles()` makes CDK ignore mousedowns outside the handle; read-only users were fine because `disabled` short-circuits `_pointerDown`.

Regression from the value-reorder feature (DEV-6611 / DEV-6856).

## Fix

- Fold the value-count check into `canReorder` and bind `[showHandle]="canReorder"`, so the handle gate and the drag gate derive from **one source of truth** and cannot diverge again.
- Guard `[cdkDragDisabled]` on `values.length < 2` inside `DraggableValueListComponent`, so the component enforces its own invariant regardless of what a caller passes — a row is never draggable-without-a-handle again.

Reordering a single value was a no-op anyway, so nothing is lost functionally.

## Tests

- `property-values.component.spec.ts` — two cases covering the single-value path (`canReorder` false, `dragDropDisabled` true).
- `draggable-value-list.component.stories.ts` — new `SingleValueIsNotDraggable` story asserting the row carries `cdk-drag-disabled` and renders no handle.

## Verification

- `nx test vre-resource-editor-resource-editor --testPathPatterns=property-value` — 42/42 pass
- `nx lint vre-resource-editor-resource-editor` — clean
- `test-storybook` — `draggable-value-list` 3/3 (incl. the new story), `property-values` 3/3

🤖 Generated with [Claude Code](https://claude.com/claude-code)
