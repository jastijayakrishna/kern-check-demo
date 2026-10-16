# Fix auto-instantiation to persist user settings

## Summary
- ensure auto-instantiated templates persist the generated user settings instead of child final settings
- add a regression test that catches storing derived final settings in project settings

## Testing
- bun run test *(fails: jest: command not found in container)*

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_6918a1f1d8d083289c92ca7e07acc2cd)
