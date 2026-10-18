# Fix group class renewal parity with single classes

## Summary
- Group classes had no cycle tracking, session generation, or renewal endpoint, so they silently never advanced cycles or renewed.
- Adds `completedSessions`/`currentCycleNumber`/`cycleStartPending` to `GroupClass`, wires cycle-completion into `attendanceSheetService`, adds a group-aware cycle payments path, and a new `POST /api/group-classes/:id/renew` endpoint.
- Includes two backfill scripts (already run against production) to bring existing group class data and their historical `ClassSession` records in line with the new fields.

## Test plan
- [x] `npx tsc --noEmit` passes
- [x] `npm run backfill:group-class-cycles` run against production (1 group class, no-op since it had no prior attendance)
- [x] `npm run backfill:group-class-sessions` run against production (0 sessions needed, confirmed no prior attendance history)
- [ ] Manually exercise `POST /api/group-classes/:id/renew` end-to-end once a group class completes a cycle

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Added group class renewal, including optional plan updates and attendance-sheet handling.
  * Group class sessions can now be scheduled automatically by cycle and tracked through completion.
  * Added cycle completion notifications for tutors.
  * Added group-class payment generation for active student enrollments.
  * Parent profiles are now automatically created or updated when classes are finalized.

* **Improvements**
  * Added support for restoring group-class cycle progress and session records from existing attendance data.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
