# Implement misc fixes and schema cleanup

## Summary
- remove duplicate `schemas.ts` and switch imports to `@motif/schema`
- add `pretest` script
- add `zod` dependency for `@motif/schema`
- handle `import.meta.env` in logger
- update SVGO v4 config and fix svg parser root detection
- type-guard analysis API responses
- move range slider gradient to CSS and adjust component
- skip file size check for synthetic files
- refactor `<MotionElement>` with `forwardRef`
- update related tests

## Testing
- `git log -1 --stat`

------
https://chatgpt.com/codex/tasks/task_e_6880657a2c2483248733bbb6107107c1
