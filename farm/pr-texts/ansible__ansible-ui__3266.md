# feat: update empty state messaging across AAP for consistency (AAP-70100)

## Summary

Updates empty state messaging throughout the AWX frontend for improved clarity and consistency, as specified in [AAP-70100](https://redhat.atlassian.net/browse/AAP-70100). Based on comprehensive UX/documentation review documented in the [UI elements audit spreadsheet](https://docs.google.com/spreadsheets/d/1nw1FteRMVVtB2vXATuCO7kB-ydfI-2t0aFhX71oLuMw/edit?usp=sharing).

## Type of Change

- [ ] Bug fix
- [x] Enhancement
- [x] Tests
- [ ] Documentation
- [ ] Other (please specify)

## Risk Analysis - REQUIRED

- [ ] **High** — Broad platform impact (e.g., SWR config, shared framework components, authentication, routing, API wrappers, build/bundler config). Changes affect multiple workspaces or could cause widespread regressions.
- [ ] **Medium** — Scoped but cross-cutting (e.g., shared utility functions, changes to multiple pages within one workspace, component library updates, test infrastructure). Limited blast radius but touches common code paths.
- [x] **Low** — Narrowly scoped (e.g., single page fix, styling tweak, documentation, test-only changes, copy/string updates). Minimal risk of unintended side effects.

## Changes

### Messaging Pattern Updates

#### Before → After
- "Please run a job to populate this list" → "Run a job to populate this list."
- "Please create a schedule by using the button below" → "Create a schedule to populate this list."
- "There are currently no groups added to this inventory" → "No groups are assigned to this inventory"
- "No teams assigned to {{resource}}" → "No teams are assigned to this {{resource}}."
- "To get started, assign teams to this {{resource}}" → "To get started, assign a team to this {{resource}}"

### Key Improvements
1. **Removed "Please"** - More direct, action-oriented language
2. **Standardized terminology** - "added to" → "assigned to" or "created for"
3. **Simplified button references** - "by using the button below" → "to populate this list"
4. **Singular team assignment** - "assign teams" → "assign a team" (more accurate)
5. **Added periods** - Consistent sentence structure
6. **Fixed typo** - "adminstrator" → "administrator"

### Affected Areas

**Automation Execution (AWX):**
- Jobs list
- Schedules (Templates, Projects, Management Jobs)
- Templates list
- Survey questions
- Projects
- Inventory: Groups, Hosts, Sources
- Hosts (global list)
- Host groups
- Instance groups
- Notifiers
- Notifications (Templates, Projects)

**Access Management (Common):**
- Team Access (all resources - Templates, Projects, Inventories, Credentials, Notifiers, Instance Groups)

### Files Modified: 22 files

**Source Files (16):**
- `frontend/awx/views/jobs/JobsList.tsx`
- `frontend/awx/views/schedules/SchedulesList.tsx`
- `frontend/awx/resources/templates/TemplatesList.tsx`
- `frontend/awx/resources/templates/TemplatePage/TemplateSurvey.tsx`
- `frontend/awx/resources/projects/Projects.tsx`
- `frontend/awx/resources/inventories/InventoryPage/InventoryGroups.tsx`
- `frontend/awx/resources/inventories/InventoryPage/InventoryHosts.tsx`
- `frontend/awx/resources/inventories/InventoryPage/InventorySources.tsx`
- `frontend/awx/resources/inventories/inventoryHostsPage/InventoryHostGroups.tsx`
- `frontend/awx/resources/hosts/Hosts.tsx`
- `frontend/awx/resources/notifications/ResourceNotifications.tsx`
- `frontend/awx/administration/notifiers/Notifiers.tsx`
- `frontend/awx/administration/management-jobs/ManagementJobPage/ManagementJobSchedules.tsx`
- `frontend/common/access/components/Access.tsx`
- `frontend/common/access/components/AccessList.tsx`
- `frontend/common/access/components/PlatformAccess.tsx`

**Test Files (6):**
- `frontend/awx/resources/templates/TemplatesList.test.tsx`
- `frontend/awx/resources/inventories/InventoryPage/InventoryGroups.test.tsx`
- `frontend/awx/resources/inventories/InventoryPage/InventoryHosts.test.tsx`
- `frontend/awx/resources/inventories/InventoryPage/InventorySources.test.tsx`
- `frontend/awx/resources/inventories/inventoryHostsPage/InventoryHostGrou
