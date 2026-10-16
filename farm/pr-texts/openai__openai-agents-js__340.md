# feat(agents-core): expose RunState history getter

Fixes #293 
Fixes #278

## Summary
- allow accessing the combined input and output history directly from RunState
- verify RunState history with new unit tests

## Testing
- `pnpm -r build-check`
- `CI=1 pnpm test` *(fails: Cannot find package '@openai/agents-core/_shims')*
- `pnpm lint`


------
https://chatgpt.com/codex/tasks/task_i_689e4b6fef28833187917f24c7ebd7ec
