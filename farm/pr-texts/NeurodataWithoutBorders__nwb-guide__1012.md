# Change staging.dandiarchive.org to sandbox.dandiarchive.org

Updates all references from "staging" to "sandbox" terminology throughout the codebase to reflect the recent change from the DANDI staging server to the sandbox server.

## Changes Made

### URL Updates
- Changed all URLs from `gui-staging.dandiarchive.org` to `gui-sandbox.dandiarchive.org`
- Updated external link configuration in `docs/conf_extlinks.py` from `dandi-staging` to `dandi-sandbox`

### User-Facing Text Updates
- Updated all references from "development server" to "sandbox server"
- Changed UI labels from "Development Server" to "Sandbox Server"
- Updated error messages from "staging archive" to "sandbox archive"
- Updated tutorial documentation to use consistent "sandbox" terminology

### Files Modified
- `src/schemas/json/dandi/global.json` - API key descriptions and URLs
- `src/electron/frontend/core/validation/dandi.ts` - Error message URLs and text
- `src/schemas/json/dandi/create.json` - UI labels and descriptions
- `docs/conf_extlinks.py` - External link configuration
- `docs/developer_guide.rst` - Developer setup instructions
- `docs/tutorials/dataset_publication.rst` - Tutorial instructions
- `docs/tutorials/index.rst` - Tutorial overview

### Internal Code Preserved
- Maintained existing API parameter names and types (e.g., `staging` parameter)
- Preserved environment variable names for backward compatibility
- Kept internal function signatures unchanged

All tests pass and the application builds successfully with these changes.

Fixes #1011.

> [!WARNING]
>
> <details>
> <summary>Firewall rules blocked me from connecting to one or more addresses</summary>
>
> #### I tried to connect to the following addresses, but was blocked by firewall rules:
>
> - `googlechromelabs.github.io`
>   - Triggering command: `node install.mjs` (dns block)
> - `https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.88/linux64/chrome-linux64.zip`
>   - Triggering command: `node install.mjs` (http block)
>
> If you need me to access, download, or install something from one of these locations, you can either:
>
> - Configure [Actions setup steps](https://gh.io/copilot/actions-setup-steps) to set up my environment, which run before the firewall is enabled
> - Add the appropriate URLs or hosts to my [firewall allow list](https://gh.io/copilot/firewall-config)
>
> </details>



<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
