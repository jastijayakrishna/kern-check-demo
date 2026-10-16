# Add private_key_path to Snowflake config schema

## Summary
- support `private_key_path` field for Snowflake connections in `.bruin.yml`
- update Snowflake connection validation to accept `private_key_path`

## Testing
- `npm run test` *(fails: Cannot find module 'crypto', etc.)*
- `npm run test:webview` *(fails: vitest not found)*

------
https://chatgpt.com/codex/tasks/task_e_685c1d5ed3ac8320aba032d904c80c24
