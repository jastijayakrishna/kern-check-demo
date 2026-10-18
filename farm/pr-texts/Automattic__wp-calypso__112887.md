# A4A MSD: open agencieshelp links in the Help Center

## Proposed Changes

* Add a `forceOpenInHelpCenter` opt-in prop to the Dashboard's `InlineSupportLink`. When set, a bare support URL that has no wpcom `postId` (e.g. an `agencieshelp.automattic.com` knowledge-base article, which the Help Center fetches by URL) opens inside the Help Center panel instead of a new tab. The default is `false`, so all existing usages are unchanged.
* Convert the A4A agency "Learn more" links to use it: referrals consolidated views, payout cards, empty state, and tiers influenced revenue. Non-`agencieshelp` external links (e.g. Tipalti) are left as plain external links.
* Add `my.a4a.localhost` to the `wpcom-proxy-request` local dev-host allowlist.

## Why are these changes being made?

* In the A4A Multi-site Dashboard, `agencieshelp.automattic.com` "Learn more" links navigated the user out of the app. The Help Center panel is already mounted there, so these should open in-panel like they do in the classic A4A client.
* The article view fetches by URL (`/help/article?post_url=`), which is product-independent — so an opt-in on the existing `InlineSupportLink` is enough; no new component or duplicate helper is needed.
* The dev-host allowlist entry fixes the actual failure found while testing: on `my.a4a.localhost` (the A4A dashboard dev host, per `config/dashboard-development.json` and `app-a4a/routing.ts`), `canAccessWpcomApis()` returned `false` because the host was missing from `localDevHosts`. That made the article fetch fall back to `apiFetch('/help-center/fetch-post')`, which resolved against the local origin and returned 404. Adding the host makes the fetch use `wpcomRequest('/help/article')` through the proxy, matching how the rest of the app already works.

## Testing Instructions

1. Run the dashboard dev server and open the A4A dashboard at `my.a4a.localhost:3000`.
2. Go to **Earn → Referrals** (or **Tiers**) and open a card's info popover / description with a "Learn more" link.
3. Click the link. Expected: the Help Center panel opens and renders the knowledge-base article in-panel (it should not open a new tab).
4. In DevTools Network, confirm the request is `help/article?post_url=…` via the proxy (not the local `help-center/fetch-post`, which previously 404'd).
5. Regression check: on a dotcom surface, an existing `InlineSupportLink` (e.g. a domains "Learn more") still behaves as before.

### Follow-ups (not in this PR)

* `agencies-beta.automattic.com` is an A4A dashboard host but is not in the `wpcom-proxy-request` origin allowlist, so the same fallback would occur there. Left out because it is a production origin.
* Passing the A4A Help Center configuration (`product: 'a4a'` — search source, chat, contact-form variant) to the MSD panel is a separate change.

## Pre-merge Checklist

- [ ] Has the general commit checklist been followed? (PCYsg-hS-p2)
- [ ] [Have you written new tests](https://github.com/Automattic/wp-calypso/blob/trunk/docs/testing/index.md) for your changes?
- [ ] Have you tested the feature in Simple (P9HQHe-k8-p2), Atomic (P9HQHe-jW-p2), and self-hosted Jetpack sites (PCYsg-g6b-p2)?
- [x] Have you checked for TypeScript, React or other console errors?
- [ ] For UI changes, have you tested the affected components in [dark mode](https://github.com/Automattic/wp-calypso/blob/trunk/docs/dark-mode.md)?
- [ ] Have you tested accessibility for your changes? Ensure the feature remains usable with various user agents (e.g., browsers), interfaces (e.g., keyboard navigation), and assistive technologies (e.g., screen readers) (PCYsg-S3g-p2).
- [ ] Have you used memoizing on expensive computations? More info in [Memoizing with create-selector](https://github.com/Automattic/wp-calypso/blob/trunk/packages/state-utils/src/create-selector/README.md) and [Using memoizing selectors](https://react-redux.js.org/api/hooks#using-memoizing-selectors) and [Our Approach to Data](https://github.com/Automattic/wp-calypso/blob/trunk/docs/our-approach-to-data.md)
- [ ] Have we added the "[Statu
