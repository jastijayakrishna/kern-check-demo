# Add reporting-specific lead access

### Motivation
- Reports should operate on the full historical lead set (including archived and converted leads) while operational screens must keep their filtered view, so reporting conversion metrics reflect the entire funnel.

### Description
- Added `listAllLeadsForReporting()` in `lib/data.ts` that returns leads without filtering out `archived_at` or `converted_client_id`.
- Updated `app/reports/page.tsx` to use `listAllLeadsForReporting()` and added inline comments documenting that archived and converted leads are intentionally included in conversion metrics.
- Kept `listLeads()` unchanged for operational pipeline screens and added a clarifying comment in `app/dashboard/page.tsx` noting the intentional filters.

### Testing
- Ran `npm run lint` and it completed successfully.
- Ran `npm run typecheck` and it completed successfully.
- Ran `npm run test` (Vitest) and all tests passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a3429979f5083328d47853f3316a1f9)
