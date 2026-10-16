# Add context workflow identifier support

## Summary
- allow `Purchases.configure` to accept an optional context with a workflow identifier
- store the workflow identifier in `EventsTracker` and include it on emitted events
- update API report and tests for the new configuration surface

## Testing
- npm run build
- npm run extract-api
- npm run test -- src/tests/behavioral-events/events-tracker.test.ts

------
[Codex Task](https://chatgpt.com/codex/tasks/task_b_6916efe7bad4832997fd82453b2320d4)
