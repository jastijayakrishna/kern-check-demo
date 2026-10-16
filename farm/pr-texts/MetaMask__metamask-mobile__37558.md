# feat: change memecoin TDP tab order to feed, overview, security

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## **Description**

Reorders the tabs on the new Token Details Page V1 (TDP v1 / memecoin TDP) so the order is now **Feed → Overview → Security** (previously Overview → Security → Feed).

The entire tab order for TDP v1 is driven by a single array constant, `TOKEN_DETAILS_V1_TABS` in `app/components/UI/TokenDetails/constants/constants.ts`. This one array controls:

- the tab bar order,
- the swipeable pager page order, and
- the default/landing active tab (which falls back to `TOKEN_DETAILS_V1_TABS[0]`).

So reordering the array is the only source change required for the ordering itself. As a consequence, **Feed is now the default landing tab** (index 0).

Note: Feed content is gated on the social leaderboard feature flag (`socialEnabled`) plus a valid asset id. Without the flag, the first tab renders the placeholder panel rather than the social feed.

### Tests updated

- `app/components/UI/TokenDetails/components/TokenDetailsV1TabBar.test.tsx` — tab render order, default/initial active tab (now `feed`), lazy-mount expectations, and `resolveSwipeTargetTab` neighbour/edge cases.
- `app/components/UI/TokenDetails/Views/TokenDetailsV1.test.tsx` — default landing panel (now Feed), stacked-page layout expectations, lazy-mount of tab pages, and `resolveSwipeTargetTab` cases. The Overview-wiring test now activates the Overview tab first since it is no longer the default.
- `app/components/UI/TokenDetails/components/tabs/FeedTab.test.tsx` — reviewed; no ordering assertions, so no changes needed.

## **Changelog**

CHANGELOG entry: null

## **Related issues**

Fixes: https://consensyssoftware.atlassian.net/browse/ASSETS-4119

## **Manual testing steps**

```gherkin
Feature: Token Details V1 tab order

  Scenario: Opening the memecoin Token Details page
    Given the TDP v1 (memecoin) experience is enabled
    When the user opens a token's details page
    Then the tab bar shows Feed, then Overview, then Security
    And the Feed tab is selected by default

  Scenario: Feed tab without the social leaderboard flag
    Given the social leaderboard feature flag is disabled
    When the user opens the Token Details page
    Then the default Feed tab shows the placeholder panel
```

## **Screenshots/Recordings**

### **Before**

N/A — tab-order/constant change covered by unit tests.

### **After**

N/A — tab-order/constant change covered by unit tests.

## **Pre-merge author checklist**

- [x] I've followed [MetaMask Contributor Docs](https://github.com/MetaMask/contributor-docs) and [MetaMask Mobile Coding Standards](https://github.com/MetaMask/metamask-mobile/blob/main/.github/guidelines/CODING_GUIDELINES.md).
- [x] I've completed the PR template to the best of my ability
- [x] I've included tests if applicable
- [x] I've documented my code using [JSDoc](https://jsdoc.app/) format if applicable
- [ ] I've applied the right labels on the PR (see [labeling guidelines](https://github.com/MetaMask/metamask-mobile/blob/main/.github/guidelines/LABELING_GUIDELINES.md)). Not required for external contributors.

## **Pre-merge reviewer checklist**

- [ ] I've manually tested the PR (e.g. pull and build branch, run the app, test code being changed).
- [ ] I confirm that this PR addresses all acceptance criteria described in the ticket it closes and includes the necessary testing evidence such as recordings and or screenshots.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-9c6edefe-2161-4089-a619-da53b25f79ba?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-9c6edefe-2161-4089-a619-da53b25f79ba&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
