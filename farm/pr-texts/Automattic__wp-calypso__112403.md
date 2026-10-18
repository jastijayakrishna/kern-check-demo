# Dashboard: serve shell for unknown routes instead of default Express 404

## Proposed Changes

* Register a hostname-gated catch-all in the dashboard Express routing that serves the dashboard shell for any otherwise-unmatched path, so the client router renders its own not-found page. Registered after the explicit routes, so those still win.
* Return an HTTP 404 for those responses (truthful status, not a 200).
* Generalize `handleSectionPath` to accept a `RegExp` path and multiple extra middleware (backward compatible).

## Why are these changes being made?

On the dashboard (e.g. `my.wordpress.com`), the Express server returns early before registering the classic catch-all 404 handler. Any unknown top-level path (e.g. `/asdfasdf`) matched no route and fell through to Express's built-in default — a raw, unstyled `Cannot GET /asdfasdf`.

The dashboard already ships a client-side `NotFound` route; it just never rendered because the server never delivered the HTML shell for these paths. This change delivers the shell so the branded 404 renders.

## Testing Instructions

* Run `yarn start-dashboard` (sets `CALYPSO_ENV=dashboard-development`).
* Visit `my.localhost:<port>/some-unknown-path` → the dashboard's "404 Not Found" page renders with a 404 status, instead of `Cannot GET`.
* Confirm a known route (`my.localhost:<port>/sites`) is unaffected.
* Automated coverage added in the server pages tests: unmatched path → 404 + dashboard shell; known route → not a 404.

Note: plain `yarn start` (the `development` env) still shows the classic Calypso 404 for these paths — the fix targets dashboard environments, matching production. See Considerations.

Note: until #112369 lands, the rendered not-found page shows the duplicate-header / empty-sidebar issue described under Related.

## Considerations

* **Serve the shell vs. a server-rendered 404 page.** Chose to serve the shell and let the existing client-side `NotFound` render (branded, consistent with the rest of the dashboard) rather than reuse the classic server `render404()`.
* **Scope to `isDashboardEnv()`.** The catch-all only activates in dashboard environments (where the bug lived and where production runs). The looser local `development` path keeps the classic 404. Extending it to `development` for parity is possible if desired, but adds complexity for a local-only case.

## Pre-merge Checklist

- [ ] Has the general commit checklist been followed? (PCYsg-hS-p2)
- [x] [Have you written new tests](https://github.com/Automattic/wp-calypso/blob/trunk/docs/testing/index.md) for your changes?
- [ ] Have you tested the feature in Simple (P9HQHe-k8-p2), Atomic (P9HQHe-jW-p2), and self-hosted Jetpack sites (PCYsg-g6b-p2)?
- [x] Have you checked for TypeScript, React or other console errors?
- [ ] For UI changes, have you tested the affected components in [dark mode](https://github.com/Automattic/wp-calypso/blob/trunk/docs/dark-mode.md)?
- [ ] Have you tested accessibility for your changes?
- [ ] Have you used memoizing on expensive computations?
- [ ] Have we added the "[Status] String Freeze" label as soon as any new strings were ready for translation (p4TIVU-5Jq-p2)?
- [ ] For changes affecting Jetpack: Have we added the "[Status] Needs Privacy Updates" label if this pull request changes what data or activity we track or use (p4TIVU-aUh-p2)?

🤖 Generated with [Claude Code](https://claude.com/claude-code)
