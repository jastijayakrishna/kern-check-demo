# fix: getLanguages shouldn't require a country parameter

## Summary
- expand mocked language fixtures to cover pagination beyond the maximum page size and include mixed country coverage
- adjust language client tests to request the maximum page size without a country filter and verify country-filtered pagination without brittle tokens

## Testing
- YVP_API_HOST=api.youversion.com pnpm --filter @youversion/platform-core test
- pnpm --filter @youversion/platform-core build
- pnpm --filter @youversion/platform-react-hooks test


------
[Codex Task](https://chatgpt.com/codex/tasks/task_b_6944720489e083289681f0cbc1a58a76)
