# fix(misc): prevent crash when opening browser in Podman+WSL container

`open@8.4.2` uses `is-docker@2.2.1` to skip WSL browser-via-PowerShell logic, but `is-docker` only checks `/.dockerenv` — missing Podman containers (which use `/run/.containerenv`). Result: `nx graph` crashes with `spawn /mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe ENOENT` inside Podman containers on WSL.

## Changes

- **`packages/nx/package.json`**
  - Upgraded `open` from `^8.4.0` to `^10.1.0`, which includes `is-inside-container@1.0.0` that properly detects both Docker and Podman containers

- **`packages/nx/src/command-line/graph/graph.ts`**
  - Replaced static CJS `import * as open from 'open'` with a dynamic ESM import using the `new Function` pattern (required because `open@10` is ESM-only)
  - Added `.catch()` handler to prevent unhandled promise rejections crashing the process in other edge cases

```typescript
// Dynamic ESM import (open@10 is ESM-only)
if (args.open) {
  (new Function('return import("open")')() as Promise<typeof import('open')>)
    .then((m) => m.default(url.toString()))
    .catch(() => {
      // Ignore errors when opening browser (e.g. no browser available)
    });
}
```

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>`nx graph` without `--open=false` attempts to spawn Powershell in Linux container under Podman+WSL</issue_title>
> <issue_description>### Current Behavior
> 
> `nx graph` (unless disabled with `--open=false`) uses the [`open`](https://github.com/sindresorhus/open) package to direct the user's browser to the graph web UI.
> 
> If this is done in a container running in Podman on WSL (i.e. on Windows), `open` incorrectly detects the environment as running directly on WSL and attempts to spawn Powershell via `/mnt/c`, which fails.
> 
> This is a bug in `open` that was fixed in version 9.0.0; Nx uses version 8.4.2. This cannot be easily overridden as 8.4.2 is the last version before Sindre's move to ESM-only.
> 
> ### Expected Behavior
> 
> `nx graph` should open the user's browser, even when running in a container under Podman+WSL.
> 
> ### GitHub Repo
> 
> https://github.com/nrwl/nx-examples
> 
> ### Steps to Reproduce
> 
> 1. Run a container in Podman with WSL. For example, a devcontainer based on `node:latest`, though I believe any Linux container with the necessary dependencies to run Node/npm/Nx would work.
> 2. `npm install --legacy-peer-deps`
> 3. `npx nx graph` fails with an error like `spawn /mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe ENOENT`
> 
> 
> ### Nx Report
> 
> ```shell
> Node           : 25.6.1
> OS             : linux-x64
> Native Target  : x86_64-linux
> yarn           : 4.2.2
> daemon         : Available
> 
> nx                     : 22.5.0-beta.5
> @nx/js                 : 22.5.0-beta.5
> @nx/eslint             : 22.5.0-beta.5
> @nx/workspace          : 22.5.0-beta.5
> @nx/angular            : 22.5.0-beta.5
> @nx/jest               : 22.5.0-beta.5
> @nx/cypress            : 22.5.0-beta.5
> @nx/devkit             : 22.5.0-beta.5
> @nx/eslint-plugin      : 22.5.0-beta.5
> @nx/module-federation  : 22.5.0-beta.5
> @nx/react              : 22.5.0-beta.5
> @nx/rollup             : 22.5.0-beta.5
> @nx/rspack             : 22.5.0-beta.5
> @nx/vite               : 22.5.0-beta.5
> @nx/vitest             : 22.5.0-beta.5
> @nx/web                : 22.5.0-beta.5
> @nx/webpack            : 22.5.0-beta.5
> typescript             : 5.9.2
> ---------------------------------------
> Registered Plugins:
> @nx/eslint/plugin
> @nx/cypress/plugin
> @nx/jest/plugin
> ---------------------------------------
> Community plugins:
> @ngrx/component-store : 21.0.0
> @ngrx/effects         : 21.0.0
> @ngrx/entity          : 21.0.0
> @ngrx/operators       : 21.0.0
> @ngrx/router-store    : 21.0.0
> @ngrx/store           : 21.0.0
> @ngrx/store-devtools  : 21.0.0
> ---------------------------------------
> Cache Usage: 0.00 B / 100.69 GB
> ```
> 
> ### Failure Logs
> 
> ```shell
> NX   Project graph started at http://127.0.0.1:4211/projects
> 
> node:events:486
>       throw er; // Unhandled 'error' event
>       ^
> 
> Error: spawn /mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe ENOENT
>     at ChildProcess._handle.onexit (node:internal/child_process:285:19)
>     at onErrorNT (node:internal/child_process:483:16)
>     at process.processTicksAndRejections (node:internal/process/task_queues:90:21)
> Emitted 'error' event on ChildProcess instance at:
>     at ChildProcess._handle.onexit (node:internal/child_process:291:12)
>     at onErrorNT (node:internal/child_process:483:16)
>     at process.processTicksAndRejections (node:internal/process/task_queues:90:21) {
>   errno: -2,
>   code: 'ENOENT',
>   syscall: 'spawn /mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe',
>   path: '/mnt/c/Windows/System32/WindowsPowerShell/v1.0/powershell.exe',
>   spawnargs: [
>     '-NoProfile',
>     '-NonInteractive',
>     '–ExecutionPolicy',
>     'Bypass',
>     '-EncodedCommand',
>     'UwB0AGEAcgB0ACAAIgBoAHQAdABwADoALwAvADEAMgA3AC4AMAAuADAALgAxADoANAAyADEAMQAvAHAAcgBvAGoAZQBjAHQAcwAiAA=='
>   ]
> }
> 
> Node.js v25.6.1
> ```
> 
> ### Package Manager Version
> 
> _No response_
> 
> ### Operating System
> 
> - [ ] macOS
> - [ ] Linux
> - [x] Windows
> - [ ] Other (Please specify)
> 
> ### Additional Information
> 
> _No response_</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes nrwl/nx#34502

<!-- START COPILOT CODING AGENT TIPS -->
---

💬 We'd love your input! Share your thoughts on Copilot coding agent in our [2 minute survey](https://gh.io/copilot-coding-agent-survey).
