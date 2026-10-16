# feat(web): Add version-specific release link to contract version in Settings

Adds a "View release" link below the contract version in Settings → Setup, linking to the specific GitHub release tag matching the deployed Safe version.

## Changes

- Added `getReleaseUrl` helper that strips L2 suffixes (e.g., "1.3.0+L2" → v1.3.0)
- Added "View release" `ExternalLink` below the contract version display
- Link points to `https://github.com/safe-fndn/safe-smart-account/releases/tag/v{version}`
- Conditionally renders only when Safe version is loaded
- Added Storybook stories for ContractVersion component

## Files Modified

- `apps/web/src/components/settings/ContractVersion/index.tsx`
- `apps/web/src/components/settings/ContractVersion/ContractVersion.stories.tsx` (new)

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/safe-global/safe-wallet-monorepo/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Low risk UI-only change that adds a derived external URL based on the loaded Safe version; main risk is incorrect link formatting for uncommon version strings.
> 
> **Overview**
> Adds a version-specific **"View release"** link to the Settings contract version display, pointing to the Safe Smart Account GitHub release tag for the currently deployed Safe version (with `+L2` suffix stripped).
> 
> Introduces Storybook coverage for `ContractVersion` with *latest*, *outdated*, and *loading* states to validate the new link behavior.
> 
> <sup>Written by [Cursor Bugbot](https://cursor.com/dashboard?tab=bugbot) for commit 12747298b8fb1504d14c0891a4a0b2ee03936f74. This will update automatically on new commits. Configure [here](https://cursor.com/dashboard?tab=bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
