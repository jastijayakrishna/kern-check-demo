# improvement(executor): correctness-by-construction for workflow logs

## Summary
- Drain pending block-callback promises at terminal boundaries via try/finally in `DAGExecutor.execute()` / `executeFromBlock()` — covers interactive, queued, HITL, and child-workflow paths automatically
- Mint a per-invocation `blockExecutionId` on `block:started`; thread through `BlockLog`, `block:completed`, `block:error`, and `ConsoleEntry`
- Switch console store primary keying to `entryIdByBlockExecutionId` (O(1)); keep legacy index as fallback for cross-deploy in-flight runs and IndexedDB hydration, with telemetry on actual fallback usage
- Unify `consoleMode`: always create placeholder on `block:started`, update on terminal — `addConsole` idempotent on `blockExecutionId`
- Delete reconciliation layer: `reconcileFinalBlockLogs`, `finalBlockLogs` SSE piggyback, terminal-handler `cancelRunningEntries`, store cross-checks

## Type of Change
- [x] Improvement

## Testing
Tested manually — three repros from #4372 stay fixed, reconnect mid-run, queued runs, HITL pause/resume, loop iterations, child workflows.

## Checklist
- [x] Code follows project style guidelines
- [x] Self-reviewed my changes
- [x] Tests added/updated and passing
- [x] No new warnings introduced
- [x] I confirm that I have read and agree to the terms outlined in the [Contributor License Agreement (CLA)](./CONTRIBUTING.md#contributor-license-agreement-cla)
