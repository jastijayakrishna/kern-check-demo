# feat: support GITHUB_TOKEN env var for GitHub API requests

Unauthenticated GitHub API requests are subject to strict rate limits (60 req/hr), which causes failures in CI environments. This adds `GITHUB_TOKEN` support to `GitHubDownloader.getAsset()`, mirroring the [Python library's implementation](https://github.com/daijro/camoufox/blob/d6540b52ce9b3e1bfac05614e2bf439b540e2841/pythonlib/camoufox/pkgman.py#L76).

## Changes

- **`src/pkgman.ts`**: When `GITHUB_TOKEN` is set, it is passed as `Authorization: ****** on all GitHub API release-listing requests. Falls back to unauthenticated requests when unset.

```typescript
const githubToken = process.env.GITHUB_TOKEN;
const headers: HeadersInit = githubToken
    ? { Authorization: `****** }
    : {};
response = await fetch(this.apiUrl, { headers });
```

> [!WARNING]
>
> <details>
> <summary>Firewall rules blocked me from connecting to one or more addresses (expand for details)</summary>
>
> #### I tried to connect to the following addresses, but was blocked by firewall rules:
>
> - `addons.mozilla.org`
>   - Triggering command: `/opt/hostedtoolcache/node/24.14.0/x64/bin/node /opt/hostedtoolcache/node/24.14.0/x64/bin/node --experimental-import-meta-resolve --require /home/REDACTED/work/camoufox-js/camoufox-js/node_modules/vitest/suppress-warnings.cjs --conditions node --conditions development /home/REDACTED/work/camoufox-js/camoufox-js/node_modules/vitest/dist/workers/forks.js` (dns block)
> - `https://api.github.com/repos/daijro/camoufox/releases`
>   - Triggering command: `/opt/hostedtoolcache/node/24.14.0/x64/bin/node /opt/hostedtoolcache/node/24.14.0/x64/bin/node --experimental-import-meta-resolve --require /home/REDACTED/work/camoufox-js/camoufox-js/node_modules/vitest/suppress-warnings.cjs --conditions node --conditions development /home/REDACTED/work/camoufox-js/camoufox-js/node_modules/vitest/dist/workers/forks.js` (http block)
>
> If you need me to access, download, or install something from one of these locations, you can either:
>
> - Configure [Actions setup steps](https://gh.io/copilot/actions-setup-steps) to set up my environment, which run before the firewall is enabled
> - Add the appropriate URLs or hosts to the custom allowlist in this repository's [Copilot coding agent settings](https://github.com/apify/camoufox-js/settings/copilot/coding_agent) (admins only)
>
> </details>

<!-- START COPILOT CODING AGENT TIPS -->
---

💬 Send tasks to Copilot coding agent from [Slack](https://gh.io/cca-slack-docs) and [Teams](https://gh.io/cca-teams-docs) to turn conversations into code. Copilot posts an update in your thread when it's finished.
