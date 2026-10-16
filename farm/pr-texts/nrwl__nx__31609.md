# feat(core): add env var for cache size

## Summary
- support configuring max cache size via NX_MAX_CACHE_SIZE env var
- show max cache size from env var in `nx report`
- document the new `NX_MAX_CACHE_SIZE` option
- test NX_MAX_CACHE_SIZE in e2e cache tests

## Testing
- `pnpm nx run-many -t lint,test,build` *(failed: NX Lexer error)*
- `pnpm test:e2e` *(failed: Command "test:e2e" not found)*
- `pnpm e2e` *(failed: Failed to process project graph)*

------
https://chatgpt.com/codex/tasks/task_e_68503bff022c832c8c014c61432aa2ed
