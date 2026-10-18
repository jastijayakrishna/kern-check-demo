# Help Center: remember article ratings on the server

Part of https://linear.app/a8c/issue/DOTCOM-18102/help-center-articles-can-be-rated-multiple-times-by-the-same-user

The wpcom side is merged: 239241-ghe-Automattic/wpcom (rating store) and 239246-ghe-Automattic/wpcom (endpoint) add `user_rating` to `GET /help/article` and the `POST /help/article/rating` endpoint. wp-admin additionally needs the Jetpack proxy in https://github.com/Automattic/jetpack/pull/51978; until that ships, wp-admin still shows the persisted rating but the save request fails silently.

## Proposed Changes

* `PostObject` gains an optional `user_rating` (1 = yes, 2 = no, `null` = not rated). It is only sent for logged-in users.
* `HelpCenterFeedbackForm` seeds its state from `user_rating`, so a rated article shows the answer instead of "Was this helpful?". A "Yes" answer now renders as "You found this article helpful." with the thumbs-up icon, since it stays on the article permanently. The two state variables were merged into one.
* New `useRateArticle` mutation posts the rating (wpcom directly, or the `help-center/article-rating` Jetpack proxy in wp-admin). It also remembers the answer in memory for the page session, so reopening the article shows it even before the article is fetched again. If the server already had an earlier rating on record, the form switches to that one.
* When the server sent no `user_rating` field (logged-out user), nothing is sent and the answer is only remembered for the page session. No `localStorage` is used.
* `GetSupport` buttons reset the browser's default button background and border. In the article view there is no global button reset, so the "No" path showed a gray box.

## Why are these changes being made?

Article feedback lived only in component state, so every remount of the article offered the buttons again and the same user could rate an article any number of times. Storing the rating on the server keeps it consistent across tabs, browsers and devices, and works the same in Calypso and wp-admin.

## Testing Instructions

* Sandbox `public-api.wordpress.com` with the wpcom branch applied.
* Open the Help Center, open any support article, scroll to the bottom and click **Yes**. Confirm "You found this article helpful." replaces the buttons.
* Close and reopen the Help Center, or reload and reopen the same article. Confirm the buttons are not offered again.
* Open another article. Confirm the buttons are available.
* Rate an article **No**. Confirm the support options appear with no gray background on the buttons, close and reopen: the support options are shown, not the buttons.
* Logged out (e.g. `/support` on the sandboxed site): rating still hides the buttons for the session, and no `article/rating` request is made.
* `yarn jest -c packages/support-articles/jest.config.js packages/support-articles`

## Screenshot

The rated state below the article, showing the new string "You found this article helpful.":

<img width="1568" height="689" alt="Help Center article showing the rated state: a thumbs-up icon followed by the text You found this article helpful." src="https://github.com/user-attachments/assets/0e1cbdcd-c6c1-487f-a257-23a55d4552e0" />

## Pre-merge Checklist

- [x] Has the general commit checklist been followed? (PCYsg-hS-p2)
- [x] [Have you written new tests](https://github.com/Automattic/wp-calypso/blob/trunk/docs/testing/index.md) for your changes?
- [ ] Have you tested the feature in Simple (P9HQHe-k8-p2), Atomic (P9HQHe-jW-p2), and self-hosted Jetpack sites (PCYsg-g6b-p2)?
- [x] Have you checked for TypeScript, React or other console errors?
- [ ] For UI changes, have you tested the affected components in [dark mode](https://github.com/Automattic/wp-calypso/blob/trunk/docs/dark-mode.md)?
- [ ] Have you tested accessibility for your changes? Ensure the feature remains usable with various user agents (e.g., browsers), interfaces (e.g., keyboard navigation), and assistive technologies (e.g., screen readers) (PCYsg-S3g-p2).
- [ ] Have you used memoizing on 
