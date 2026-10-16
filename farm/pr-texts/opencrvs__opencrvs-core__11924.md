# Implement audit log writes for key endpoints

- [x] Create `writeAuditLog` storage function with `AuditLogParams` type in commons
- [x] Implement audit logging for all 9 endpoints (create, get, search, notify, 3×correction, integrations, attachments)
- [x] Move all type definitions to `packages/commons/src/events/AuditLog.ts` using `type` (not `interface`)
- [x] Define explicit per-operation types joined into `AuditLogOperation` union
- [x] `writeAuditLog` propagates errors naturally and returns promise result
- [x] Restructure `EventActionAuditLog` as single type with union `operation` field — eliminates `as Extract<...>` cast in `actions/index.ts`; all call sites are fully type-safe with no unsafe casts
- [x] Remove unused `operation` field from tRPC context (`trpc.ts`)

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>Implement audit log writes for key endpoints</issue_title>
> <issue_description>**Description:**
> Implement audit log entry creation for the following endpoints when called by a system client. Each should write a `request_data` capture and a meaningful `response_summary`:
> 
> - `POST /events` — Create event
> - `GET /events/{eventId}` — Fetch full event document
> - `POST /events/{eventId}/notify` — Notify event
> - `POST /events/{eventId}/correction/request` — Request correction
> - `POST /events/{eventId}/correction/approve` — Approve correction
> - `POST /events/{eventId}/correction/reject` — Reject correction
> - `POST /integrations` — Create new integration client
> - `POST /attachments` — Upload file attachment
> - `POST /events/search` — Search (request_data: search terms; response_summary: result count + document IDs)
> 
> Not all endpoints need logging — only the ones listed above are in scope for this ticket.
> Make the audit log writing function such that the controller layer will have to supply all information. So do not pass JWT to the write function for instance. Client id must be supplied</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes opencrvs/opencrvs-core#11908

<!-- START COPILOT CODING AGENT TIPS -->
---

🔒 GitHub Advanced Security automatically protects Copilot coding agent pull requests. You can protect all pull requests by enabling Advanced Security for your repositories. [Learn more about Advanced Security.](https://gh.io/cca-advanced-security)
