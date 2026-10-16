# feat(skills): add starkzap-sdk workflow skill

## Summary
- add new `starkzap-sdk` skill under `skills/starkzap-sdk/SKILL.md`
- add the skill to `skills/README.md`
- regenerate `skills/manifest.json` to include the new skill

## Validation
- `python3 scripts/quick_validate_skill.py skills/starkzap-sdk`
- `python3 scripts/skills_manifest.py --check`

## Notes
- this skill is focused on workflows for `keep-starknet-strange/starkzap` (SDK internals, onboarding, wallets, ERC20, staking, tests, and generated artifacts).

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Added a new Starkzap SDK skill with comprehensive user-facing documentation for wallet onboarding, sponsored transactions, ERC20 flows, and staking.
  * Includes focused reference guides for signer integration, sponsored transactions, ERC20 helper patterns, and staking reliability.
  * Added runnable example and diagnostic scripts demonstrating wallet execution, pool discovery, and Privy signing workflows.
  * Manifest updated to expose the new skill for discovery.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
