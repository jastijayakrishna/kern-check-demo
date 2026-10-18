# feat(core): add inspector quick activation gestures

## Summary

Adds quick inspector activation while holding Command on macOS or Control elsewhere, and lets double-click selection activate the inspector flow before editing.

## Impact

This makes the inspector easier to invoke during local slide development without keeping it manually toggled on.

## Validation

- `pnpm check`

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Inspector now opens while holding **Command** on macOS or **Control** on other platforms.
  * You can select elements by **double-clicking** within the inspector, without triggering unwanted slide text selection.
* **Bug Fixes**
  * Improved interaction handling so inspector opening/selection behaves more consistently when active or inactive.
  * Updated hit detection and selection clearing for smoother overlay behavior.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
