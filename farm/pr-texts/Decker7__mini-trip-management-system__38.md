# Remove Clerk Organizations dependency from the sidebar and nav filtering

## Summary
Reported: the "Organizations feature required" Clerk dev-warning dialog was appearing on every dashboard page after Organizations was disabled on the Clerk instance (a separate, already-applied config change — `npx clerk disable orgs` on the development instance).

Root cause: two components called Clerk's organization hooks unconditionally as part of the core app shell, not just the isolated Workspaces/Team/Billing template pages:
- `AppSidebar` rendered `<OrgSwitcher/>` (which calls `useOrganizationList()`) in the sidebar header, on every dashboard page.
- `useFilteredNavItems` (`src/hooks/use-nav.ts`) called `useOrganization()` unconditionally for every nav-filtering render.

Neither did anything for this app: `nav-config.ts` has no item using `requireOrg` or `permission` (already pruned in an earlier commit), and the Staff/Admin role always came from the User's `publicMetadata`, never organization membership.

## Changes
- Deleted `src/components/org-switcher.tsx` (no longer referenced anywhere).
- `AppSidebar`: removed the `useOrganization()` call, the org-gated Billing menu item, and replaced the sidebar header with a static app title instead of the org switcher.
- `use-nav.ts`: removed the `useOrganization()` call and the dead `requireOrg`/`permission` filtering branches.
- `PermissionCheck` type (`src/types/index.ts`): dropped the now-unused `requireOrg`/`permission` fields.
- Updated the stale nav-config.ts doc comment and one `infoconfig.ts` help-text string that referenced the removed checks.

Not touched: the still-unused Workspaces/Team/Billing/Exclusive template pages themselves (not reachable from the UI, out of scope for this fix — happy to remove them in a follow-up if wanted).

## Test plan
- [x] `npm run typecheck`
- [x] `npm run lint`
- [x] `npm run format:check`
- [x] `npm run test` (94 passing)
- [x] `npm run build`
- [ ] Manual: log in as Admin/Staff and confirm the "Organizations feature required" dialog no longer appears on any dashboard page — needs a real authenticated session to verify

🤖 Generated with [Claude Code](https://claude.com/claude-code)



<!-- greptile_comment -->

<h3>Greptile Summary</h3>

The PR removes Clerk Organizations dependencies from the shared dashboard navigation and aligns the related types and documentation with user-metadata-based role filtering.
- Replaces the organization switcher with a static application header and removes the organization-gated Billing link.
- Removes organization and permission checks from navigation filtering and `PermissionCheck`.
- Updates Clerk and navigation RBAC documentation to describe the supported authentication model.

<h3>Confidence Score: 5/5</h3>

The PR appears safe to merge.

No blocking failure remains.

<details><summary><h3>Important Files Changed</h3></summary>




| Filename | Overview |
|----------|----------|
| src/components/layout/app-sidebar.tsx | Removes organization hooks and UI from the shared sidebar while retaining user-role-filtered navigation and account actions. |
| src/components/org-switcher.tsx | Deletes the organization switcher that unconditionally invoked Clerk Organizations APIs. |
| src/hooks/use-nav.ts | Simplifies navigation filtering to use the signed-in user's public-metadata role without organization state. |
| src/types/index.ts | Removes the unsupported organization and permission fields from the navigation access type. |
| docs/nav-rbac.md | Updates the navigation guide so it no longer documents the removed organization and permission access fields. |
| docs/clerk_setup.md | Reframes Clerk setup around authentication-only usage and documents Organizations and Billing as disabled. |

</details>

<sub>Reviews (2): Last reviewed commit: ["Update stale nav/Clerk docs after removi..."](https://github.com/decker7/mini-trip-management-system/commit/9da350dbf97dc17526b244b22483f90dcfc5d7a5) | [Re-trigger Greptile](https://app.greptile.com/api/retrigger?id=58314139)</sub>

<!-- /greptile_comment --
