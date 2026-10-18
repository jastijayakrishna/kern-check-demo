# Agents Manager: show the chat on the Site Editor navigation view

Related to AI-1056

## Proposed Changes

* Revert the Site Editor navigation-view chat hiding introduced in #112164, so the AI chat is available on the navigation view (the hub/list view of `site-editor.php`) again:
  * Remove `useHideChatOnSiteEditorNavigation` and its tests.
  * Remove the dock's navigation-view render gate and the `isReady` wiring into `useAgentLayoutManager`.
  * Remove the now-unused `isSiteEditorCanvasEditMode()` helper.
  * Un-export `ADMIN_BAR_BUTTON_ID` / `ADMIN_BAR_AI_CHAT_BUTTON_ID` and the sidebar container class constants — the removed hook was their only external consumer.
* Two pieces of #112164 are deliberately kept, as they are unrelated to the hiding: the docked `#wpadminbar` height fix and the `shouldRenderChat` → `isChatEnabled` rename.

## Why are these changes being made?

* We want the AI chat available on the Site Editor navigation view; the constraint that motivated hiding it there no longer holds. Part of AI-1056.
* The Jetpack counterpart (https://github.com/Automattic/jetpack/pull/50273) removes the backend pre-render gate (`Agents_Manager::is_site_editor_navigation()` and the docked-shell pre-render skip). Ship both together: with only the Jetpack side deployed, the frontend would still hide the chat on the navigation view; with only this PR, the chat renders but the docked shell isn't pre-rendered there (a minor flash, not breakage).

## Testing Instructions

Sandbox (Simple site with the unified experience enabled):

1. `cd apps/agents-manager && yarn dev --sync` — only `widgets.wp.com` needs sandboxing, not the site itself.
2. Optionally apply the Jetpack counterpart PR (https://github.com/Automattic/jetpack/pull/50273) to the sandbox to also restore the docked-shell pre-render on the navigation view.
3. Open `/wp-admin/site-editor.php` (the navigation view, no `?canvas=edit`).
4. Verify the Ask AI button and the Help menu show in the admin bar, the chat opens and docks, and (with the Jetpack PR applied and the chat previously open + docked) the docked sidebar shell pre-renders on load without a flash.
5. Navigate into the editing canvas (`?canvas=edit`) and back to the navigation view — the chat keeps working in both directions and the docked state persists.

Calypso:

1. `yarn start`, log in at `http://calypso.localhost:3000`.
2. Verify the masterbar AI chat entry still opens the chat on Calypso screens (no regression from the constant un-exports).

Unit tests: `yarn jest -c test/packages/jest.config.js --testPathPattern=agents-manager` (37 suites, 388 tests).

## Pre-merge Checklist

- [ ] Has the general commit checklist been followed? (PCYsg-hS-p2)
- [ ] [Have you written new tests](https://github.com/Automattic/wp-calypso/blob/trunk/docs/testing/index.md) for your changes?
- [ ] Have you tested the feature in Simple (P9HQHe-k8-p2), Atomic (P9HQHe-jW-p2), and self-hosted Jetpack sites (PCYsg-g6b-p2)?
- [x] Have you checked for TypeScript, React or other console errors?
- [ ] For UI changes, have you tested the affected components in [dark mode](https://github.com/Automattic/wp-calypso/blob/trunk/docs/dark-mode.md)?
- [ ] Have you tested accessibility for your changes? Ensure the feature remains usable with various user agents (e.g., browsers), interfaces (e.g., keyboard navigation), and assistive technologies (e.g., screen readers) (PCYsg-S3g-p2).
- [ ] Have you used memoizing on expensive computations? More info in [Memoizing with create-selector](https://github.com/Automattic/wp-calypso/blob/trunk/packages/state-utils/src/create-selector/README.md) and [Using memoizing selectors](https://react-redux.js.org/api/hooks#using-memoizing-selectors) and [Our Approach to Data](https://github.com/Automattic/wp-calypso/blob/trunk/docs/our-approach-to-data.md)
- [ ] Have we added the "[Status] String Freeze" label as soon as any new strings were ready for translation (p4TIVU-5Jq-p2)?
    - [ ] For UI changes, have we tested the change in various languages (for example, ES, PT, FR, o
