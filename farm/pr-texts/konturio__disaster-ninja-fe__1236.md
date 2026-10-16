# fix(map-ruler): disable layer clicks during measurement

https://kontur.fibery.io/Product_management/Pain_Point/Ruler-While-measuring-when-I-click-on-the-map-an-active-contributor-page-opens-in-a-new-tab-and-dist-217

## Summary
- prevent feature clicks while measuring distance by using highest priority listeners
- document Map Ruler priority in event management docs
- cover Map Ruler listener priority with a unit test

## Testing
- `pnpm lint`
- `pnpm vitest run`


------
https://chatgpt.com/codex/tasks/task_e_688fd1f2da14832fa13735788a8982c7

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **Bug Fixes**
  * Increased the priority of Map Ruler event listeners to ensure they take precedence over other map interactions.

* **Documentation**
  * Updated all documentation to reflect the new Map Ruler listener priority value (changed from 1 to 100) in diagrams, tables, and descriptions.

* **Tests**
  * Added tests to verify that Map Ruler event listeners are registered with the correct (higher) priority.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
