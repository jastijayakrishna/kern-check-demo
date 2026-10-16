# Feat(Positions): Filter out dust positions from Zerion data

Part of https://linear.app/safe-global/issue/GRO-72/correct-portfolio-view-at-safe-specifically-avoid-double-accounting

## Summary
- filter Zerion-derived positions below $0.01 before grouping and drop empty protocols
- add helper to detect dust positions and reuse filtered data for protocol totals
- extend positions service tests to cover dust filtering and mock number formatting

## Testing
- yarn test src/routes/positions/positions.service.spec.ts

------
https://chatgpt.com/codex/tasks/task_b_68d4f9a04390832fb84977f12cd1004e
