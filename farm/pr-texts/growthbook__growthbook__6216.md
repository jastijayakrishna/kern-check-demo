# feat: show Projects nav link for users who can view projects

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
### Features and Changes

Previously, the Projects link in the sidebar was only shown to users who had permission to manage projects (`canManageSomeProjects()`). This meant non-admin users couldn't see the Projects page even if they had read access to projects.

This PR adds a new `canViewProjectsPage()` method to the Permissions class that returns true if:
- User can manage some projects (existing behavior), OR  
- User has `readData` permission globally or in at least one project

The sidebar nav filter now uses this new method, allowing users with read access to view the Projects page. The page itself already handles action permissions correctly - Create/Edit/Delete buttons are disabled based on user permissions.

**Changes:**
- Added `canViewProjectsPage()` method to `packages/shared/src/permissions/permissionsClass.ts`
- Updated sidebar nav filter in `packages/front-end/components/Layout/sidebarNav.ts`
- Added test coverage for `canViewProjectsPage()` across all role types

### Dependencies

None

### Testing

1. Run the permissions tests: `pnpm --filter shared test -- test/permissions.test.ts`
2. All tests pass including the new `canViewProjectsPage()` assertions for each role:
   - `noaccess`: false (can't manage projects AND can't read data)
   - `readonly`: true (can't manage projects BUT can read data)  
   - Other roles with read access: true

### Screenshots

No UI changes to the Projects page itself. The only change is the visibility of the "Projects" link in the sidebar navigation, which will now appear for users who can view projects even if they can't manage them.
<!-- CURSOR_AGENT_PR_BODY_END -->

[Slack Thread](https://growthbookapp.slack.com/archives/C0A8XE4PAL9/p1782410717631309?thread_ts=1782410717.631309&cid=C0A8XE4PAL9)

<div><a href="https://cursor.com/agents/bc-be8c0694-a45e-549f-92bf-cf0b7952364b"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-be8c0694-a45e-549f-92bf-cf0b7952364b"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
