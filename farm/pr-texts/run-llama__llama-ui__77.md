# Add workflow-specific filtering for handler hooks and stories

## Summary
- add a required `workflowName` argument to the workflow handler list and progress hooks so they filter and compute state per workflow
- persist `workflowName` on handler summaries, expose test-store helpers, and adjust the handler store sync logic to only auto-subscribe running handlers
- expand Vitest coverage and Storybook stories to validate workflow scoping, including a progress bar interaction test

## Testing
- pnpm lint
- pnpm run format-check
- pnpm run coverage *(fails: Playwright browser download is blocked in this environment)*
- pnpm run build:all

------
https://chatgpt.com/codex/tasks/task_e_68cdb16b0050832b96a94accb086ca59
