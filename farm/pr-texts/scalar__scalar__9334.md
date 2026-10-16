# feat(analytics): add save and sync analytics events

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Adds three new `log:` analytics events to track document save and registry sync activity, giving the team visibility into how many users are saving and syncing.

### New events

| Event | When it fires |
|-------|--------------|
| `log:save-document` | When a user saves a local document (via the Save button or Cmd/Ctrl+S) |
| `log:sync-pull-document` | When a user initiates a pull from the registry |
| `log:sync-push-document` | When a user successfully pushes a document to the registry |

### Changes

- **`packages/workspace-store/src/events/definitions/log.ts`** — declares the three new `LogEvents` entries
- **`packages/api-client/src/plugins/posthog/sanitize-event-payload.ts`** — adds them to the `TRACKED_EVENTS` allowlist with `empty` extractors (event fact only, no payload)
- **`projects/scalar-app/src/features/app/hooks/use-document-sync.ts`** — emits the events from `handleSaveDocument`, `handlePullDocument`, and `handlePushDocument`
- **`packages/api-client/src/plugins/posthog/sanitize-event-payload.test.ts`** — covers the new events in the existing test suite

### Why these events, why now

The existing `ui:save:local-document` event only fires from the keyboard shortcut handler — clicking the Save button in the header calls `handleSaveDocument` directly without emitting. Similarly, `hooks:on:rebase:document:complete` covers pull completion but there is no event for push. These gaps mean PostHog has no way to answer "how many people are saving?" or "how many people are pushing?".

<!-- CURSOR_AGENT_PR_BODY_END -->

[Slack Thread](https://apidocumentation.slack.com/archives/C07RNPTKCB1/p1779482972517419?thread_ts=1779482972.517419&cid=C07RNPTKCB1)

<div><a href="https://cursor.com/agents/bc-315fcd17-305d-5131-a583-e8297ae80f00"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-315fcd17-305d-5131-a583-e8297ae80f00"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
