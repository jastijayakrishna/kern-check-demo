# Reduce redundant RxJS/WatermelonDB observer work on app load

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
#### Summary
Reduces duplicated observable work on the startup path, mainly the channel sidebar (the first screen rendered after launch).

- **Share the sidebar pipeline** (`categories/index.ts`): `categoriesData` was subscribed separately for `flattenedItems` and `unreadChannelIds`, so every category query ran twice. It was also keyed on the whole current user record, so writes to `status`, `last_picture_update`, etc. (e.g. `fetchMe` at login) tore down and rebuilt the sidebar. It now keys on `{id, locale}` only and is wrapped in `shareReplay`.
- **Create shared inputs once, not per category** (`observe_flattened_categories.ts`): each category created its own hidden DM/GM preference, autoclose preference, and current/last unread channel observables (about 6N queries for N categories). These are now built once per sidebar subscription and shared.
- **Share the global system/config observers** (`queries/servers/system.ts`, new `utils/observable.ts`): `observeCurrentUserId`, `observeCurrentTeamId`, `observeCurrentChannelId` and `observeConfigValue` have hundreds of call sites. For example, every channel list row subscribes to the current user and channel id, and each call built a new WatermelonDB query with no deduplication. They now return one cached, `distinctUntilChanged` observable per database and key, via `cachePerDatabase`.

The shared `shareLatest()` operator replays the latest value and releases the source one tick after the last unsubscribe. That way a pipeline swapped by `switchMap` doesn't restart the query. The cache is a `WeakMap` keyed by `Database`, so a recreated server database gets fresh observables.

#### Ticket Link
NONE

#### Checklist
- [x] Added or updated unit tests (required for all new features)

New tests fail on the previous implementation:
- The sidebar pipeline was built twice.
- 4 categories made 16 preference queries instead of 4, and category changes resubscribed them.
- System observers weren't shared and re-emitted unchanged values.

The full Jest suite passes except for `app/utils/time.test.ts`. That test fails on `stainless-steel` without this change, because the CI VM's dependencies don't have the 2026d timezone data. `npm run check` passes.

#### Device Information
Not device tested. The Cloud Agent VM can't run simulators. Verified with Jest, ESLint, and TypeScript.

#### Release Note
```release-note
Improved app loading performance by removing duplicated database observers.
```
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-40efb312-9d75-465a-8a29-c490ffbd2025?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-40efb312-9d75-465a-8a29-c490ffbd2025&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
