# Help Center: Persist remapped Odie chat ids for logged-in users

## Proposed Changes

* When Odie returns a new `chat_id` for a logged-in support interaction (e.g. legacy-bot remapping), persist that id via `addEventToInteraction` instead of only when the interaction has no odie chat yet.
* Prefer the latest odie event in `getOdieIdFromInteraction` so subsequent turns and history follow the remapped chat rather than the original legacy id.
* Add unit coverage for the remapped-chat case.

## Why are these changes being made?

Server-side handling can return a new `chat_id` when a logged-in user continues a legacy Odie chat. The logged-out path already stores that id; the logged-in path dropped it because it only updated the interaction when `! odieId`. That left every later message posting to the legacy id (another orphaned turn-one chat), and those remapped chats never appeared in Help Center history.

## Testing Instructions

### Calypso

1. Run `yarn start`.
2. Open the Help Center as a logged-in user who has (or can start) an Odie conversation tied to a legacy chat / bot path that remaps to a new `chat_id`.
3. Send a message and confirm the response succeeds.
4. Send a follow-up message in the same conversation and confirm the bot sees prior context (not a fresh turn-one reply).
5. In DevTools → Network, confirm later POSTs use the remapped chat id from the first response, not the legacy id.
6. Open Support History and confirm the remapped conversation is listed and reopenable.

### Simple/Atomic/CIAB

1. Sandbox `widgets.wp.com`.
2. Run `cd apps/help-center && yarn dev --sync`.
3. Visit any Simple, Atomic, or CIAB site (the site itself does not need sandboxing).
4. Repeat the logged-in remapped-chat continuity checks above in the Help Center.

### Regression

1. Start a brand-new logged-in Odie chat (no prior odie event) and confirm the first response still creates/links the interaction correctly.
2. Confirm logged-out chat continuity still works (session `chatId` updates as before).

## Pre-merge Checklist

- [x] Has the general commit checklist been followed? (PCYsg-hS-p2)
- [x] [Have you written new tests](https://github.com/Automattic/wp-calypso/blob/trunk/docs/testing/index.md) for your changes?
- [ ] Have you tested the feature in Simple (P9HQHe-k8-p2), Atomic (P9HQHe-jW-p2), and self-hosted Jetpack sites (PCYsg-g6b-p2)?
- [ ] Have you checked for TypeScript, React or other console errors?
- [ ] For UI changes, have you tested the affected components in [dark mode](https://github.com/Automattic/wp-calypso/blob/trunk/docs/dark-mode.md)?
- [ ] Have you tested accessibility for your changes? Ensure the feature remains usable with various user agents (e.g., browsers), interfaces (e.g., keyboard navigation), and assistive technologies (e.g., screen readers) (PCYsg-S3g-p2).
- [ ] Have you used memoizing on expensive computations? More info in [Memoizing with create-selector](https://github.com/Automattic/wp-calypso/blob/trunk/packages/state-utils/src/create-selector/README.md) and [Using memoizing selectors](https://react-redux.js.org/api/hooks#using-memoizing-selectors) and [Our Approach to Data](https://github.com/Automattic/wp-calypso/blob/trunk/docs/our-approach-to-data.md)
- [ ] Have we added the "[Status] String Freeze" label as soon as any new strings were ready for translation (p4TIVU-5Jq-p2)?
    - [ ] For UI changes, have we tested the change in various languages (for example, ES, PT, FR, or DE)? The length of text and words vary significantly between languages. 
- [ ] For changes affecting Jetpack: Have we added the "[Status] Needs Privacy Updates" label if this pull request changes what data or activity we track or use (p4TIVU-aUh-p2)?

Made with [Cursor](https://cursor.com)
