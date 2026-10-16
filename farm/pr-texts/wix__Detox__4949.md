# fix(sync): accept null one-time event objects

## Description

- This pull request addresses the issue described here: #4942

In this pull request, I have updated the sync status schema to accept `null` for `one_time_events.description.object`, matching the iOS payload described in the issue. The one-time event formatter now treats `null` the same as a missing object description, and a regression snapshot covers that path.

## Verification

- `corepack yarn workspace detox jest src/client/actions/formatters/SyncStatusFormatter.test.js --updateSnapshot --runInBand`
- `corepack yarn workspace detox eslint src/client/actions/formatters/SyncStatusFormatter.test.js src/client/actions/formatters/sync-resources/OneTimeEventsFormatter.js`
- `git diff --check`

---

> _For features/enhancements:_
 - [ ] I have added/updated the relevant references in the [documentation](https://github.com/wix/Detox/tree/master/docs) files.

> _For API changes:_
 - [ ] I have made the necessary changes in the [types index](https://github.com/wix/Detox/blob/master/detox/index.d.ts) file.

This was implemented with Codex assistance, with the patch kept focused on the schema/formatter mismatch and reviewed against the existing unit tests.
