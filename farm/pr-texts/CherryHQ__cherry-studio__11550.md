# fix: set CLAUDE_CONFIG_DIR to avoid path encoding issues on Windows with non-ASCII usernames

### What this PR does

Before this PR:
AGENT crashes on Windows when the username contains Chinese characters (or other non-ASCII). The Claude Agent SDK attempts `mkdirSync` on `C:\Users\YZM-一只猫\.claude`, but Windows corrupts the path encoding to `C:\Users\YZM-һֻè`, causing `EPERM: operation not permitted`.

After this PR:
Sets `CLAUDE_CONFIG_DIR` to redirect SDK config to `%APPDATA%\CherryStudio\.claude`, which avoids the problematic user home directory path.

```typescript
CLAUDE_CONFIG_DIR: path.join(app.getPath('userData'), '.claude')
```

Fixes #11549 

### Why we need it and why it was done in this way

The `@anthropic-ai/claude-agent-sdk` uses the user's home directory by default for its config. On Windows, paths containing non-ASCII characters can be corrupted when passed to child processes. The `CLAUDE_CONFIG_DIR` environment variable is the SDK's supported override mechanism.

The following tradeoffs were made:
- SDK config now lives in app userData rather than user home. This is acceptable since Cherry Studio already manages its own data here.

The following alternatives were considered:
- Patching the SDK itself (not feasible, external dependency)
- Using Windows short path names (unreliable, not always enabled)

### Breaking changes

None. Existing users may have `.claude` config in their home directory; the SDK will create a new config in the new location.

### Special notes for your reviewer

The fix is minimal: one import (`path`) and one env var addition.

### Checklist

- [x] PR: The PR description is expressive enough and will help future contributors
- [x] Code: [Write code that humans can understand](https://en.wikiquote.org/wiki/Martin_Fowler#code-for-humans) and [Keep it simple](https://en.wikipedia.org/wiki/KISS_principle)
- [x] Refactor: You have [left the code cleaner than you found it (Boy Scout Rule)](https://learning.oreilly.com/library/view/97-things-every/9780596809515/ch08.html)
- [x] Upgrade: Impact of this change on upgrade flows was considered and addressed if required
- [ ] Documentation: A [user-guide update](https://docs.cherry-ai.com) was considered and is present (link) or not required. You want a user-guide update if it's a user facing feature.

### Release note

```release-note
Fixed AGENT crash on Windows when username contains Chinese or other non-ASCII characters
```

> [!WARNING]
>
> <details>
> <summary>Firewall rules blocked me from connecting to one or more addresses (expand for details)</summary>
>
> #### I tried to connect to the following addresses, but was blocked by firewall rules:
>
> - `cdn.sheetjs.com`
>   - Triggering command: `/usr/local/bin/node /usr/local/bin/node /home/REDACTED/work/cherry-studio/cherry-studio/.yarn/releases/yarn-4.9.1.cjs install` (dns block)
>   - Triggering command: `/usr/local/bin/node /usr/local/bin/node /home/REDACTED/work/cherry-studio/cherry-studio/.yarn/releases/yarn-4.9.1.cjs install --immutable` (dns block)
>   - Triggering command: `/usr/bin/curl curl -v REDACTED` (dns block)
>
> If you need me to access, download, or install something from one of these locations, you can either:
>
> - Configure [Actions setup steps](https://gh.io/copilot/actions-setup-steps) to set up my environment, which run before the firewall is enabled
> - Add the appropriate URLs or hosts to the custom allowlist in this repository's [Copilot coding agent settings](https://github.com/CherryHQ/cherry-studio/settings/copilot/coding_agent) (admins only)
>
> </details>

<!-- START COPILOT CODING AGENT SUFFIX -->



<details>

<summary>Original prompt</summary>


----

*This section details on the original issue you should resolve*

<issue_title>[Bug]: AGENT crashes on startup when Windows username contains Chinese characters</issue_title>
<issue_description>> [!NOTE]
> This issue/comment/review was translated by Claude.

### Issue Checklist

- [x] I understand that issues are for feedback and problem solving, not for complaining in the comment section, and will provide as much information as possible to help solve the problem.
- [x] My issue is not listed in the [FAQ](https://github.com/CherryHQ/cherry-studio/issues/3881).
- [x] I've looked at **pinned issues** and searched for existing [Open Issues](https://github.com/CherryHQ/cherry-studio/issues), [Closed Issues](https://github.com/CherryHQ/cherry-studio/issues?q=is%3Aissue%20state%3Aclosed), and [Discussions](https://github.com/CherryHQ/cherry-studio/discussions), no similar issue or discussion was found.
- [x] I've filled in short, clear headings so that developers can quickly identify a rough idea of what to expect when flipping through the list of issues. And not "a suggestion", "stuck", etc.
- [x] I've confirmed that I am using the latest version of Cherry Studio.

### Platform

Windows

### Version

v1.7.0

### Bug Description

On Windows systems, if the current logged-in account contains Chinese characters (e.g., "一只猫"), the built-in AGENT function in Cherry Studio 1.7.0 will crash instantly upon startup.

### Steps To Reproduce

1. Create a new Chinese Windows local account, for example "YZM-一只猫"
2. Log into that account, install or update to Cherry Studio 1.7.0
3. Open Cherry Studio → AGENT → Send any conversation
4. After one second, an error occurs and cannot continue

### Expected Behavior

The AGENT function should start normally regardless of whether the username is Chinese or not; or at least provide a friendly prompt and alternative solutions.

### Relevant Log Output

```shell
Error name: AI_ProviderSpecificError
Error message: node:fs:1363
  const result = binding.mkdir(
                         ^

Error: EPERM: operation not permitted, mkdir 'C:\Users\YZM-һֻè'
    at mkdirSync (node:fs:1363:26)
    at t.mkdirSync (node:electron/js2c/node_init:2:17237)
    at Object.mkdirSync (file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/cli.js:9:1358)
    at pAB (file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/cli.js:327:8249)
    at i0 (file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/cli.js:327:7174)
    at iAB (file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/cli.js:341:1243)
    at file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/cli.js:4254:12990)
    at B (file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/cli.js:8:6527)
    at Object.callback (file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/cli.js:4531:162)
    at file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/cli.js:4248:1991)
{
  errno: -4048,
  code: 'EPERM',
  syscall: 'mkdir',
  path: 'C:\\Users\\YZM-һֻè'
}

Node.js v22.21.1


Claude Code process exited with code 1
Stack trace: AI_ProviderSpecificError: node:fs:1363
  const result = binding.mkdir(
                         ^

Error: EPERM: operation not permitted, mkdir 'C:\Users\YZM-һֻè'
    at mkdirSync (node:fs:1363:26)
    at t.mkdirSync (node:electron/js2c/node_init:2:17237)
    at Object.mkdirSync (file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/cli.js:9:1358)
    at pAB (file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/cli.js:327:8249)
    at i0 (file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/cli.js:327:7174)
    at iAB (file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/cli.js:341:1243)
    at file:///C:/Users/YZM-%E4%B8%80%7E1/AppData/Local/Temp/366BF0joxTOXFAAbfYJjU4ELyQX/resources/app.asar.unpacked/node_modules/@anthropic-ai/claude-agent-sdk/...

</details>

- Fixes CherryHQ/cherry-studio#11549

<!-- START COPILOT CODING AGENT TIPS -->
---

✨ Let Copilot coding agent [set things up for you](https://github.com/CherryHQ/cherry-studio/issues/new?title=✨+Set+up+Copilot+instructions&body=Configure%20instructions%20for%20this%20repository%20as%20documented%20in%20%5BBest%20practices%20for%20Copilot%20coding%20agent%20in%20your%20repository%5D%28https://gh.io/copilot-coding-agent-tips%29%2E%0A%0A%3COnboard%20this%20repo%3E&assignees=copilot) — coding agent works faster and does higher quality work when set up for your repo.
