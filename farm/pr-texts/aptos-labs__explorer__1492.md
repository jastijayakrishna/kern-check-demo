# fix(blocks): correct UTC timezone handling and add live age refresh

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Problem

The **Age** column on the Blocks list page showed incorrect values (e.g. "8h ago" for a freshly produced block). The root cause was in `useGetMostRecentBlocks.ts`: Hasura returns GraphQL timestamps as ISO 8601 strings **without a timezone suffix** (e.g. `"2024-03-19T17:40:00"`). JavaScript's `new Date()` interprets such strings as **local time**, not UTC. For a UTC+8 user this shifts every block timestamp 8 hours into the past, making brand-new blocks appear to be 8 hours old.

A secondary issue: the Age column was computed once at render time and never refreshed, so the relative time froze instead of counting up.

## Changes

### 1. Timezone fix — `app/api/hooks/useGetMostRecentBlocks.ts`

Before converting the Hasura timestamp to milliseconds, check whether the string already carries a timezone indicator (`Z` or `±HH:MM`). If not, append `Z` so it is always parsed as UTC:

```ts
const rawTs = row.timestamp as string;
const utcTs = /Z$|[+-]\d{2}:\d{2}$/.test(rawTs) ? rawTs : `${rawTs}Z`;
block_timestamp: new Date(utcTs).getTime().toString(),
```

### 2. Live age refresh — `app/pages/Blocks/Table.tsx`

Replaced the static `getBlockAge()` call with a new `useBlockAge()` hook that drives state updates via `setInterval(1 s)`, so the Age column counts up in real time. Both the desktop table cell and the mobile card use the same hook.

### 3. `timestampDisplay.formatted` fix — `app/utils/utils.ts`

This field was built with `date-fns.format()` (which outputs local time) but labelled "UTC". Replaced with explicit `getUTC*()` calls so the string is always a correct UTC representation regardless of the browser's timezone.

## Scope

- Only the Blocks list page timestamp calculation and age display are affected.
- Transaction, account, and other pages receive timestamps as microsecond integer strings from the REST API; `ensureMillisecondTimestamp` handles those correctly — no similar issue exists there.
- `timestampDisplay.formatted` has no consumers in the current codebase; the fix is defensive.

## Testing

- ✅ `pnpm test --run` — 148 tests passed
- ✅ `pnpm lint` — 0 errors (2 pre-existing unrelated warnings)
- ✅ `pnpm fmt` — no formatting changes needed
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-08a38919-4ddf-4105-a88f-bb4d096c1b26"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-08a38919-4ddf-4105-a88f-bb4d096c1b26"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
