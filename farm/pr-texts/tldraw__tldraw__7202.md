# fix(dotcom): disable sidebar file drag without groups flag

## Summary
- gate sidebar file dragging on the groups feature flag so drag-and-drop is disabled for users without the flag

### Change type

- [x] `bugfix` 

### Test plan

1. Verify that dragging sidebar files is disabled when the 'groups_frontend' flag is off.
2. Verify that dragging is disabled on coarse pointer devices (mobile).

- [ ] Unit tests
- [ ] End to end tests

### Release notes

- Disabled sidebar file dragging for users without the groups feature flag enabled.

------
[Codex Task](https://chatgpt.com/codex/tasks/task_b_6925774b242083219b294d017154f942)

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> Enable sidebar file dragging only when `groups_frontend` is on and the pointer is not coarse (e.g., mobile).
> 
> - **Sidebar**:
>   - Gate file drag interactions in `TlaSidebarFileLink.tsx` behind `useHasFlag('groups_frontend')`.
>     - Introduce `isDragEnabled = hasGroups && !isCoarsePointer`.
>     - Apply to `draggable` and `onDragStart` so dragging is disabled without the flag and on coarse pointers.
> 
> <sup>Written by [Cursor Bugbot](https://cursor.com/dashboard?tab=bugbot) for commit b620a3f1aeda8982d26542dc63535f8726345221. This will update automatically on new commits. Configure [here](https://cursor.com/dashboard?tab=bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
