# Remove Pontem Wallet from supported wallets

## Summary
- Remove Pontem Wallet from AvailableWallets type
- Remove Pontem Wallet from AIP-62 wallet registry
- Remove Pontem from README documentation

## Test plan
- [x] Verify TypeScript types compile without Pontem Wallet
- [ ] Test wallet adapter functionality in example app

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Low risk change limited to removing a wallet entry and documentation, but it can be a breaking change for consumers referencing `"Pontem Wallet"` or relying on it appearing in the AIP-62 registry list.
> 
> **Overview**
> **Pontem Wallet is no longer treated as a supported AIP-62 wallet.** The PR removes the Pontem entry from `aptosStandardSupportedWalletList` and drops `"Pontem Wallet"` from the `AvailableWallets` type union.
> 
> Docs are updated (`README.md`, `READMEV2.md`) to remove Pontem from the listed supported wallets.
> 
> <sup>Written by [Cursor Bugbot](https://cursor.com/dashboard?tab=bugbot) for commit f7df1950b25de75302c5f95d2fdfbe2b7b7b72f2. This will update automatically on new commits. Configure [here](https://cursor.com/dashboard?tab=bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
