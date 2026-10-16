# fix: misc bug fixes

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Five unrelated, self-contained bug fixes found while reading through the codebase. Each is a one-line change.

- **`actions/AppStoreActions.ts`** — `autoSaveSchedule` guard `providerID.length < 0` can never fire; changed to `<= 0` so empty strings short-circuit as intended.
- **`backend/routers/auth.ts`** — `getSessionUserId` did `(session ?? '').userId`, which reads `.userId` off the empty string and returns `undefined` when the session lookup misses. Null-check instead.
- **`backend/routers/websoc.ts`** — removed two leftover `console.log('queryWebSoc', …)` debug lines from the hot WebSoc path.
- **`components/Calendar/CalendarCourseEvent.tsx`** — component used a bare `return;` for skeleton events, which resolves to `undefined` and trips React 18's "Nothing was returned from render". Return `null`.
- **`stores/Schedules.ts`** — `deleteCustomEvent` compared `findIndex` against `undefined`, but `findIndex` returns `-1` on miss. When the event didn't exist in a given schedule, `splice(-1, 1)` removed the last custom event instead of skipping.

## Test Plan

- Type-check and lint pass locally.
- Manual smoke: deleting a custom event that only exists in one of several schedules no longer nukes an unrelated event from the other schedules.

## Issues

Closes #

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-0ed140eb-6b37-482d-a320-f44d1f522a74"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-0ed140eb-6b37-482d-a320-f44d1f522a74"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
