# improvement: remove last-admin check for project memberships

<!-- ccr-slack-attribution -->
_Requested by **Daniel Hougaard** · [Slack thread](https://infisical.slack.com/archives/C098PEY86SV/p1782217982034699?thread_ts=1782217982.034699&cid=C098PEY86SV)_

## Before / After

**Before:** removing or downgrading the last admin of a project returned a `400` "This action would leave the project with no admin. Promote another user to admin first." error, blocking the action.

**After:** project memberships can be updated, removed, or left even when doing so would leave the project without an admin. This is safe because org admins can always re-join any project via the "Access all organization projects" permission.

The same protection still applies to **organization** memberships — you still cannot leave or downgrade the last admin of an organization.

## How

- Removed the `assertWillRetainAdmin` calls from the three project code paths:
  - membership role update (shared `membership-user-service.ts` update path)
  - member removal (shared `membership-user-service.ts` delete path)
  - leave-project / bulk delete (`project-membership-service.ts`)
- Guarded the shared update path so the check only runs when `scope === AccessScope.Organization`.
- The shared `assertWillRetainAdmin` helper and the organization call sites (`org-service.ts`, `org-fns.ts`) are unchanged.
- Removed the now-unused `assertWillRetainAdmin` import (and an unused `project` lookup) from `project-membership-service.ts`.

## Notes

- The frontend still has a client-side warning in `DeleteProjectSection.tsx`. That is left out of scope here (this is a backend-only change) and can be addressed as a possible follow-up.
