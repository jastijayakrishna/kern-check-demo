# ✨ (sample) [NO-ISSUE]: Add Solana signer disabled features setting

### 📝 Description

Adds a **Solana Signer** section to the sample app Settings page (same as the existing Ethereum Signer section). It has a multi-select dropdown where you can disable one or more Solana signer features:

- SPL tokens (`spl`)
- Transaction checks (`transactionChecks`)
- Delayed signing (`delayedSigning`)
- Generic clear sign (`genericClearSign`)

The selected features are passed to `SignerSolanaBuilder` as `disabledFeatures`, so they are force-disabled whatever app version is installed. The setting is saved to localStorage with the other settings, has a Reset link and defaults to none. The labels are typed as a `Record<SolanaSignerFeaturesNames, string>`, so adding a new signer feature fails typecheck until it is added to the dropdown.

### ❓ Context

- **JIRA or GitHub link**: [NO-ISSUE]
- **Feature**: Sample app tooling to test Solana signer feature fallbacks

### ✅ Checklist

- [ ] **Covered by automatic tests**: sample app UI/settings only, no tests added
- [x] **Changeset is provided**
- [x] **Documentation is up-to-date**
- [x] **Impact of the changes:**
  - Sample app only: new Settings section; Solana signer is rebuilt when the selection changes

---

### 🧐 Checklist for the PR Reviewers

- [ ] **The code aligns with the requirements** described in the linked JIRA or GitHub issue.
- [ ] **The PR description clearly documents the changes** made and explains any technical trade-offs or design decisions.
- [ ] **There are no undocumented trade-offs**, technical debt, or maintainability issues.
- [ ] **The PR has been tested** thoroughly, and any potential edge cases have been considered and handled.
- [ ] **Any new dependencies** have been justified and documented.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
