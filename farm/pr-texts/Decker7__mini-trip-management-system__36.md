# Split Staff Management into Staff/Admin tables, add revoke access (v2)

## Summary
Redo of #34 (reverted in #35). Fixes the three P1 findings Greptile raised there:

1. **Roleless users become Staff** — `staffUsers` used to filter on `role !== 'admin'`, so a roleless account (including one just revoked) landed in the Staff table with a Revoke button, and `revokeStaffAccess` would always reject it. Fixed by adding a third "Unassigned" section (`role === null`) with the role dropdown but no Revoke button — the account stays visible and recoverable instead of disappearing or exposing a guaranteed-failing action.
2. **Pending revoke remains dismissible** — `AlertModal`'s Cancel button / backdrop / Escape closed the dialog even mid-request, making a revoke that actually went through look cancelled. `AlertModal` now ignores dismissal while `loading` is true (fixes the same latent issue in the existing trip-delete flow for free, no behavior change when not loading).
3. **Stale role snapshot permits revoke** — `updateUserRole` and the original `revokeStaffAccess` did a GET then a PATCH replacing `publicMetadata` wholesale, so a concurrent metadata write could be silently lost. Both now call Clerk's dedicated `PATCH /users/:id/metadata` endpoint, which deep-merges server-side and removes a key when set to `null` — no GET-modify-write cycle, no clobbering.

Also: Manage Staff still splits into a Staff table and an Admin table (same live Clerk data, no new Convex table), and "Revoke Access" remains Staff-only, reversible via reassigning a role. `CONTEXT.md` gained an "Unassigned" term alongside "Revoke Access"; the ADR now also documents the metadata-endpoint choice.

Not in this PR (needs Clerk Dashboard access, not code): enabling required First/Last name fields on the invite-acceptance sign-up screen, and confirming password auth is the enabled sign-in strategy.

## Test plan
- [x] `npm run typecheck` / `npm run typecheck:convex`
- [x] `npm run lint`
- [x] `npm run format:check`
- [x] `npm run test` (94 passing, incl. updated/new `revokeStaffAccess` and `updateUserRole` cases asserting calls hit `/metadata`)
- [x] `npm run build`
- [ ] Manual check of the Staff/Admin/Unassigned tables and Revoke Access flow — blocked here by Clerk sign-in, needs a run against a real logged-in Admin session

🤖 Generated with [Claude Code](https://claude.com/claude-code)



<!-- greptile_comment -->

<h3>Greptile Summary</h3>

The PR separates Staff, Admin, and Unassigned users in the management UI and adds reversible Staff access revocation through Clerk metadata.
- Adds server-authorized and tested role revocation using Clerk’s metadata endpoint.
- Applies confirmed role changes locally so failed refreshes cannot restore the previous UI state.
- Prevents confirmation dialogs from being dismissed while requests are pending.
- Documents the Unassigned state and Clerk-only account architecture.

<h3>Confidence Score: 5/5</h3>

The PR appears safe to merge.

No blocking failure remains.

<details><summary><h3>Important Files Changed</h3></summary>




| Filename | Overview |
|----------|----------|
| convex/staffAccounts.ts | Adds an Admin-authorized Staff revocation action and moves role writes to Clerk’s metadata-merge endpoint. |
| convex/staffAccounts.test.ts | Covers authorization, Staff-only revocation, and metadata-endpoint request payloads at the Convex function seam. |
| src/features/staff/components/staff-listing.tsx | Splits users into Staff, Admin, and Unassigned tables and immediately reflects confirmed role changes before refreshing. |
| src/components/modal/alert-modal.tsx | Blocks Cancel, backdrop, and Escape dismissal while a confirmation request is pending. |
| CONTEXT.md | Defines Revoke Access and Unassigned consistently with the implemented account lifecycle. |
| docs/adr/0001-staff-accounts-live-in-clerk-only.md | Documents Clerk as the account source of truth and the metadata endpoint used for role changes. |

</details>


<details open><summary><h3>Sequence Diagram</h3></summary>

```mermaid
sequenceDi
