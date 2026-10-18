# feat: coordinator reschedule approval flow

## Summary
- `FinalClass.oneTimeReschedules` now stores `sessionId`, `status` (PENDING/APPROVED/REJECTED), `requestedBy`, `requestedAt`, `rejectionReason`
- `parentService.requestParentReschedule` updated to populate all new fields
- Three new coordinator endpoints: list pending requests, approve (calls `rescheduleSession`), reject
- On approve: session date is updated + parent notified. On reject: parent notified with reason

## Test plan
- [ ] Parent submits reschedule → entry appears in coordinator's pending list
- [ ] Coordinator approves → ClassSession date changes to requested date
- [ ] Parent receives approval/rejection notification
- [ ] Already-processed requests return 400 if re-submitted

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Coordinators can now view pending session reschedule requests.
  * Added actions to approve or reject a specific reschedule request.

* **Bug Fixes**
  * Reschedule requests now track status, requester, request time, and optional rejection reason.
  * Approval and rejection updates are now reflected in the request workflow and notifications.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
