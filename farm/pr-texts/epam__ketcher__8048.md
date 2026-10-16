# Refactor: #8027 - This assertion is unnecessary since it does not change the type of the expression (part 2)

## Summary
- remove redundant non-null assertions when computing text layout and resolving monomer attachment points
- guard template interactions from undefined functional groups and streamline struct service initialization
- drop redundant portal option assertions in the toolbar hook

## Testing
- npm run test:types --workspaces *(fails: missing workspace dependencies and generated schema files)*

------
https://chatgpt.com/codex/tasks/task_e_68e56c5a0c6883299a3b54ee0598d4da
