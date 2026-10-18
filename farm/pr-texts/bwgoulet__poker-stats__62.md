# Default scope to one minimum night

### Motivation

- Make the scope filter default to 1 minimum night so the UI and server-side parsing align with the desired default scope.

### Description

- Set the UI default in `GlobalFilterBar.tsx` by changing `defaultMinNights` from `3` to `1`.
- Set the server-side default in `src/lib/filters/filter-data.ts` by changing `DEFAULT_MIN_NIGHTS` from `3` to `1` and keep `MIN_NIGHTS_OPTIONS` unchanged.
- Update `test/filter-data.test.ts` to expect the new default and the new invalid-value fallback behavior.

### Testing

- Ran `npm test -- --testTimeout=15000` and all tests passed (37 tests).
- Ran `npm run typecheck` and TypeScript checks succeeded.
- Ran `git diff --check` with no issues reported.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a9928679180833280cf8a3c27cb31a4)
