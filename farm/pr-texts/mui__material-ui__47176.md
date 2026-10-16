# [code-infra] Enable Next.js build cache to improve CI performance

Enable Next.js build cache and CI improvements

**Main Changes:**
- ✅ Enable Next.js build cache to improve CI performance (50% faster on cache hit)
- ✅ Fix Windows issue with llms build scripts
- ✅ Increase CPU in CI with `os.availableParallelism()` (4 in Windows/Linux, 3 in macOS, 6 in Netlify)
- ✅ Split packages build and docs build into separate steps
- ✅ Move types validation to CircleCI
- ✅ Fix double pnpm typo in CircleCI config

**Performance Impact:**
- Ubuntu test-dev job: 50% reduction in `build:ci` time on exact cache hit
- macOS run significantly improved (see https://github.com/mui/material-ui/actions/runs/19105313775/job/54590022351?pr=47176)

**Note:** One EMFILE error occurred during testing (https://github.com/mui/material-ui/actions/runs/19105313775/job/54587423928?pr=47176) - monitoring recommended.

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
