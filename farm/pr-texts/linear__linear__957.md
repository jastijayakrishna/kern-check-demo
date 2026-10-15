# Fix GitLab CSV import: convert time estimates from seconds to points

GitLab exports time estimates in seconds (e.g., 28800s for 8 hours), but Linear's API expects estimate values in the range 0-64 points. This caused imports to fail with "estimate must not be greater than 64."

## Changes

- **Added `convertTimeEstimateToPoints()` function**: Maps GitLab's time-based estimates (seconds) to Linear's point-based scale using a modified fibonacci sequence
  - 0-1h → 1pt, 1-2h → 2pt, 2-4h → 3pt, 4-8h → 5pt, 8-16h → 8pt, 16-32h → 13pt, 32-64h → 21pt, 64h+ → 64pt (capped)
  
- **Updated import logic**: Parse `Time Estimate` field and convert before setting issue estimate

## Example

```typescript
// Before: Direct assignment caused validation errors
estimate: safeParseInt(row["Time Estimate"])  // 28800 → Error!

// After: Converted to point scale
const timeEstimateSeconds = safeParseInt(row["Time Estimate"]);
estimate: convertTimeEstimateToPoints(timeEstimateSeconds)  // 28800s (8h) → 5pt
```

<!-- START COPILOT CODING AGENT SUFFIX -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>gitlab import is broken - estimates are not allowed to be greater than 64, but gitlab issue exports estimates in seconds</issue_title>
> <issue_description>for an 8h estimate
> 
> ```
>  █████████████████░░░░░░░░░░░░░░░░░░░░░░░ 41% | ETA: 82s | 113/273
> tw [Error]: Argument Validation Error - estimate must not be greater than 64.
>     at fw (/Users/x/.npm-packages/lib/node_modules/@linear/import/node_modules/@linear/sdk/dist/index-cjs.min.js:1:1472991)
>     at /Users/x/.npm-packages/lib/node_modules/@linear/import/node_modules/@linear/sdk/dist/index-cjs.min.js:1:1852053
>     at process.processTicksAndRejections (node:internal/process/task_queues:105:5) {
>   type: 'InvalidInput',
>   errors: [
>     iw {
>       type: 'InvalidInput',
>       userError: true,
>       path: [Array],
>       message: 'estimate must not be greater than 64.'
>     }
>   ],
> 
> ...
>       estimate: 28800
> 
> ```
> 
> </issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>

- Fixes linear/linear#827

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
