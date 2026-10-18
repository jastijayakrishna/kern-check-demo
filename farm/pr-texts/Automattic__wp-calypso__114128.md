# Help Center chat: refetch the chat when the user comes back to the tab

Fixes [DOTSUP-470](https://linear.app/a8c/issue/DOTSUP-470). Alternative to #113901, which keeps tabs in sync with a `BroadcastChannel`.

## Proposed Changes

* Remove the `BroadcastChannel` mirroring between tabs: the `broadcast-messages` module, the per-tab `odieBroadcastClientId`, and every `broadcastOdieMessage` call.
* Add `useRefreshChatOnFocus`, mounted by the chat component. When the document becomes visible or the window gains focus, it refetches the support interaction, invalidates the Odie chat, and puts the chat in its loading state so `useGetCombinedChat` rebuilds it from fresh data, and re-downloads a Zendesk conversation, the same way it does on open, reconnect and Smooch re-init. It waits for the interaction refetch first, so a chat escalated in another tab switches to Zendesk instead of settling on the stale interaction. It skips chats that don't exist yet, never interrupts a send or transfer, and runs at most once every five seconds.
* One change in `useGetCombinedChat`: a failed conversation fetch now leaves the loading state, keeping the conversation the chat already shows or settling into the same Odie-history-only Zendesk state used when Zendesk can't be reached. Before, the effect re-ran, fetched again and started another interaction, forever; a refresh-on-focus design would hit that far more often.
* Share the support interaction query key between the query, the mutations that write to its cache, and the new invalidation.

## Why are these changes being made?

When the same signed-in user has more than one Help Center chat open, messages typed in one chat showed up in the others: the broadcast between tabs only checked "not my own message", so every tab received every message. Mirroring messages also meant every tab kept a second copy of each message that had to be reconciled against the real one (the greyed `is-sending` copy, dedup against the Smooch echo, escalations that other tabs had to follow), and each review round on #113901 found another edge of that reconciliation.

With no second copy there is nothing to reconcile. Each tab owns its chat, and a tab you come back to refetches it. Background tabs stay stale until you return to them; that is the trade-off, and it matches how the Help Center is used.

## Testing Instructions

Unit: `yarn test-packages packages/odie-client packages/help-center` (184 tests). New coverage in `use-refresh-chat-on-focus.test.tsx` (refetch order, focus, skip while sending, skip without a chat, logged-out chats, throttle) and a regression test in `use-get-combined-chat.test.tsx` for the failed-fetch fix.

Manual, verified on a local build with two tabs on `/sites` and the Help Center open:

1. Open a new Odie chat in tab 1 and send a message. Open tab 2: it restores the same chat.
2. Send in tab 2, switch to tab 1: the message and reply are there. Same the other way round.
3. Send in tab 1 and switch away and back before Odie replies: the reply still arrives, no reload in between.
4. Escalate to Zendesk in tab 2, switch to tab 1: it switches to the Zendesk conversation.
5. Send Zendesk messages in either tab and switch: each appears once, marked sent.
6. Start a different chat in tab 2 and send in both tabs: nothing crosses over.
7. Switch tabs with an empty new chat, and with the Help Center closed: nothing happens.

## Pre-merge Checklist

- [x] Has the general commit checklist been followed? (PCYsg-hS-p2)
- [x] [Have you written new tests](https://github.com/Automattic/wp-calypso/blob/trunk/docs/testing/index.md) for your changes?

🤖 Generated with [Claude Code](https://claude.com/claude-code)

