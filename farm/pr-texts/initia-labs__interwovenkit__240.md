# fix(send): pin iUSD after INIT in Send asset picker

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Follow-up to #237 — the Send asset picker was still using the old INIT-only denom pin and did not place iUSD after INIT.

This change extracts `sortSendBalanceItems` from `useSortedBalancesWithValue` and applies the shared `getPinnedAssetSymbolRank` helper so Send matches Bridge, Portfolio, and Minity ordering.

## Sort order (Send picker)

1. Pinned rank (`INIT` → `iUSD`)
2. Fee token
3. USD value ↓
4. Listed in registry
5. Raw balance ↓
6. Symbol A→Z

## Test plan

- [x] `pnpm test src/data/account.test.ts`
- [x] `pnpm typecheck`
- [x] `pnpm lint`
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-efc730d8-20b6-4962-bae8-63648ed2a269"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-efc730d8-20b6-4962-bae8-63648ed2a269"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>



<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **Bug Fixes**
  * Improved send-flow balance sorting so the `INIT` asset stays pinned immediately before `iUSD`, while maintaining correct fee-token prioritization.
  * Ensures consistent, deterministic ordering for the remaining assets (including correct handling when balances are empty/treated as zero).
* **Tests**
  * Added unit tests covering pinned-asset behavior, fee-token handling, and stable alphabetical ordering when sort priorities tie.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
