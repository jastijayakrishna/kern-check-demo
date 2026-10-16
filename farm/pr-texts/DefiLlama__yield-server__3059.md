# makina: add Merkl reward APY

Adds Merkl rewards to the **makina** pools, the same way `superform` and other adaptors do.

- `makina/index.ts`: pools go through `addMerklRewardApy(pools, 'makina', pool => pool.token)`. Makina campaigns are HOLD campaigns on the machine share tokens, so pools are matched on their share token (`token`) rather than the pool id.
- `merkl/index.js`: adds `makina` to `protocolsBlacklist`, since the rewards are now integrated in the makina adaptor.

Current live campaign: "Supply to multiple tokenized stocks vaults on Makina" on Base, 10% APR paid in USDC (2026-10-12 → 2026-11-12). It covers the 7 tokenized-stock machines in a single opportunity; the helper matches each share token in the opportunity's token list.

`npm run test --adapter=makina`: 184 passed. yAAPLc, yGOOGLc, yMETAc, yNVDAc, yMSFTc, yAMZNc and yTSLAc get `apyReward` 10% with `rewardTokens` [USDC]. ySPCXc (not in the campaign) and the Ethereum pools are unchanged.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Makina pools now include applicable Merkl reward APY in their displayed yield information.
* **Bug Fixes**
  * Makina opportunities are excluded from the general Merkl opportunity listings.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
