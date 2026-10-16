# fix: prevent infinite re-render loop in task selection useEffect

## Summary
- Fixes infinite re-render loop in `App.tsx` that prevented tasks from running
- The `useEffect` for syncing `selectedTask` was causing infinite re-renders because:
  1. `selectedTask` object was in the dependency array
  2. `setSelectedTask(updatedTask)` created a new reference
  3. New reference triggered the effect again → infinite loop

## Changes
- Added reference equality check (`updatedTask !== selectedTask`) before calling `setSelectedTask`
- Removed `selectedTask` from dependency array (keep only `selectedTask?.id` and `selectedTask?.specId`)

## Test Plan
- [x] Verified dev server starts without infinite loop errors
- [x] Tasks can be selected and run properly
- [x] Spec creation works without freezing

Fixes #441

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Bug Fixes**
  * Optimized task selection so the app only updates when the selected task genuinely changes, preventing redundant state updates and reducing the risk of repeated re-renders—improving responsiveness and stability when switching tasks.

<sub>✏️ Tip: You can customize this high-level summary in your review settings.</sub>
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
