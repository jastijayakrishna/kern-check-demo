# [ONEROSTER-78]: restrict public health check output — remove tenant IDs and raw DB errors

The public `/health-check` endpoint leaks internal infrastructure details (tenant IDs, raw database error messages) to unauthenticated callers.

### Changes

**`src/controllers/healthController.js`**
- **Multi-tenant mode:** dropped the `tenants` array from the response entirely; aggregate `{ status, mode }` is sufficient for a public health probe
- **Error responses:** removed `message: err.message` from the outer catch and `error: err.message` from per-tenant failure objects — all failure paths now return only the generic `"database unreachable"` string to callers
- **Server-side logging:** per-tenant catch now logs `err.message` rather than the full error object to avoid accidentally persisting connection strings or credentials in log sinks

**Before → After (multi-tenant failure):**
```json
// Before
{
  "status": "fail",
  "mode": "multi-tenant",
  "tenants": [
    { "tenant": "acme", "status": "pass" },
    { "tenant": "beta", "status": "fail", "error": "password authentication failed for user \"sa\" at 10.0.0.5:1433" }
  ]
}

// After
{ "status": "fail", "mode": "multi-tenant" }
```

**`tests/unit-tests/healthController.test.js`** *(new)*
- 8 unit tests covering single-tenant and multi-tenant paths; explicitly assert tenant IDs and raw error strings are absent from every response body

Relates to [ONEROSTER-78](https://edfi.atlassian.net/browse/ONEROSTER-78) / parent epic ONEROSTER-66.

<!-- START COPILOT CODING AGENT SUFFIX -->



<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> Issue: ONEROSTER-78
> Summary: Restrict public health check output: remove tenant IDs and raw DB errors
> Description: Problem
> The public health check endpoint exposes tenant IDs and raw database error messages. This leaks internal infrastructure details to unauthenticated callers.
> Files
> - src/app.js
> - src/controllers/healthController.js
> Acceptance Criteria
> - Public health check response does not expose tenant IDs
> - Raw database error messages are not returned to unauthenticated callers
> - Deep diagnostic health checks (if any) are protected by authentication
> Labels: security
> 
> Custom Fields:
> Development: {}
> Epic Link: ONEROSTER-66
> Rank: 1|i00i34:
> 
> Parent Issue: ONEROSTER-66
> Parent Summary: OneRoster 1.0 hardening
> Parent Description: Hardening tasks for the Ed-Fi OneRoster 1.0 API implementation, addressing security vulnerabilities, test coverage gaps, and code quality issues identified in a comprehensive automated code review conducted on 2026-05-25.
> Areas Covered
> - Security: multi-tenant authorization, encryption, CORS, health check exposure, dependency vulnerabilities
> - Test coverage: CI pipeline, integration tests, middleware tests, boundary tests
> - Code cleanliness: ESM/CommonJS compatibility, DB connection centralization, dead code, SQL coupling
> 
> You have been assigned to a work item "Restrict public health check output: remove tenant IDs and raw DB errors". Analyze the details of the work item and get started.
> Summary: Restrict public health check output: remove tenant IDs and raw DB errors
> Description: Problem
> The public health check endpoint exposes tenant IDs and raw database error messages. This leaks internal infrastructure details to unauthenticated callers.
> Files
> * src/app.js
> * src/controllers/healthController.js
> Acceptance Criteria
> * Public health check response does not expose tenant IDs
> * Raw database error messages are not returned to unauthenticated callers
> * Deep diagnostic health checks (if any) are protected by authentication
> 
> User: You have been assigned to a work item "Restrict public health check output: remove tenant IDs and raw DB errors". Analyze the details of the work item and get started.
> 
> Agent: I received your request and will let you know when the PR is ready.
> 
> Agent: 🔍 I'm checking if I have everything I need to get started.
> 
> User: [https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster](https://github.com/Ed-Fi-Alliance-OSS/edfi-oneroster)
> 
> ## Branch naming
> 
> This task relates to issue ONEROSTER-78 — preserve that identifier somewhere in the branch name and pull request title for traceability. Do not treat the identifier as a verbatim slug or prepend it with a hyphen by default; instead, adapt the full branch name to comply with the repository's branch-naming pattern, adding any required prefix or restructuring the shape as needed.
> 
> Include a link to the original issue in the pull request description: https://edfi.atlassian.net/browse/ONEROSTER-78


</details>



[ONEROSTER-78]: https://edfi.atlassian.net/browse/ONEROSTER-78?atlOrigin=eyJpIjoiNWRkNTljNzYxNjVmNDY3MDlhMDU5Y2ZhYzA5YTRkZjUiLCJwIjoiZ2l0aHViLWNvbS1KU1cifQ
