# fix(sql-editor): treat data-modifying CTEs as writes

## Bug and impact
PostgreSQL (and other engines that allow data-modifying CTEs) can run statements like:

```sql
WITH wiped AS (
  DELETE FROM orders RETURNING id
)
SELECT * FROM wiped;
```

`isWriteStatement` only inspected the verb **after** the `WITH … AS (…)` list, so this looked like a `SELECT`. That bypassed:
- SQL Editor **Safe mode** confirmation
- Node `sql` bridge write rejection when Safe mode is on
- Edit Table **index fragmentation** custom SQL “SELECT-only” guard (newly added endpoint)

Impact: silent data deletion/updates under a read-looking statement; Safe mode fails closed incorrectly; fragmentation probe can mutate data.

## Root cause
CTE walk skipped bodies and only classified the outer/main verb.

## Fix
- Scan each CTE body (including nested `WITH`) for write/DDL verbs in `isWriteStatement` / `isMutatingDmlStatement`
- Reuse `isWriteStatement` in `isSafeIndexFragmentationCustomSql`

## Validation
- `npx vitest run packages/core/src/modules/sql-splitter.test.ts packages/core/src/modules/dialect-index-fragmentation.test.ts` — 55 passed

<div><a href="https://cursor.com/agents/bc-76e2c89a-8f62-4a1a-b088-1316a97acbd5"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/automations/cc55dc47-87da-11f1-b532-320a589b8025"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/view-automation-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/view-automation-light.png"><img alt="View Automation" width="141" height="28" src="https://cursor.com/assets/images/view-automation-dark.png"></picture></a>&nbsp;</div>

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Medium Risk**
> Changes security-sensitive write classification shared by SQL Editor Safe mode, Node SQL bridge, and custom probe validation; logic is heuristic but directly closes a data-mutation bypass with added test coverage.
> 
> **Overview**
> Fixes a **safe-mode bypass** where `WITH … AS (DELETE/UPDATE/INSERT … RETURNING …) SELECT …` was classified as read-only because only the outer verb after the CTE list was checked.
> 
> **`sql-splitter`:** `walkWithCtes` now collects each CTE body and recursively scans nested `WITH` for write/DDL verbs in `isWriteStatement` and `isMutatingDmlStatement` (via `sqlTextIsWrite` / `sqlTextIsMutatingDml`).
> 
> **`dialect-index-fragmentation`:** `isSafeIndexFragmentationCustomSql` calls `isWriteStatement` so custom fragmentation probes cannot mutate data through data-modifying CTEs.
> 
> Tests cover DELETE/UPDATE/INSERT RETURNING patterns, nested CTEs, and the fragmentation custom-SQL guard.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit da9e5d5b177905d43d7c6775dfcf60c400be0abe. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
