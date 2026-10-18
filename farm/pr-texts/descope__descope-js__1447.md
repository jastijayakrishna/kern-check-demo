# fix(user-profile-widget): rebuild preloaded modal flow on value change RELEASE

## Summary
- The user-profile widget preloads each attribute's edit/delete flow (a `<descope-wc>`) once so opening a modal has no ~1s load delay. The preloaded flow captured the value at load and never refreshed, so after deleting (or otherwise changing) a value the edit modal still showed the **old** value until it was closed and reopened.
- Fix: rebuild a modal's preloaded flow whenever its value changes, so the flow re-fetches fresh data. A modal that is currently open is skipped, so an in-progress flow isn't dropped.
- Applies to phone, email, name and builtin-attribute modals. Custom attributes already refresh on change, so they're unchanged.

## Linked
- Issue: descope/etc#17202 ("[Bug] Delete Phone in widget is buggy")
- Related PRs: none (change is contained to descope-js)

## Changes
- `ModalDriver`: add `isOpen` / `isClosed` getters (read the `opened` attribute).
- `initPhone/Email/Name/UserBuiltinAttributes` mixins: content is now built by a single `#refreshModalsContent()` path driven off the value subscription — it preloads on the first (seeding) call and rebuilds on later changes, skipping open modals. Removed the separate init-time build so each modal is built once at mount (no double flow-start).

## Manual test plan
- Set a phone (or use an attribute that has a value), reload the widget, delete it, click the edit (pencil) icon → the modal shows the value cleared on the **first** open (previously showed the stale value).
- Repeat for email and a name attribute.
- Edit a value → save → reopen edit → shows the new value (no regression).
- Edit modal opens instantly (preload intact) — no blank/loading gap.
- Modal still renders with the configured theme.

## Risk / review focus
- `ModalDriver.isOpen`/`isClosed` are new public getters on a shared lib (`@descope/sdk-component-drivers`) — additive, used only by this widget.
- Single-build refactor: verified live that the edit modal still renders themed when its flow is built via the refresh path (e2e stubs `descope-wc`, so theming was checked manually against the real component).
- New e2e regression tests (`e2e/user-profile-widget.spec.ts`) confirmed to fail without the fix and pass with it.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
