# feat: allow multiple language_ranges values in getVersions()

## Summary
- rename the Bible client language range schema to use the expected plural name
- add direct coverage of ApiClient query string building for scalar and array parameters

## Testing
- YVP_API_HOST=api.youversion.com pnpm test
- pnpm --filter @youversion/platform-core build


------
[Codex Task](https://chatgpt.com/codex/tasks/task_b_6944728e77008328857a8e182ca06086)
