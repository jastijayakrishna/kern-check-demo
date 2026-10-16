# fix: set __COMFYUI_DESKTOP_VERSION__ for desktop-managed ComfyUI launches

## ELI5
ComfyUI-Manager, the add-on that installs custom nodes, decides whether it runs inside the Desktop app by checking for a name tag the app hands it at launch. The old Desktop app gave it that tag, and this app never did, so Manager thinks every Desktop user is running a hand-made git install. This PR hands the tag back, so Manager reports and behaves as a Desktop install again.

## Motivation
Registry tracking undercounts Desktop users. Over the last 30 days only about 50K registry IPs reported a Desktop form factor, far fewer than Desktop's own telemetry suggests. ComfyUI-Manager is the only registry client that reports `desktop-win` / `desktop-mac`, and it does so only when `__COMFYUI_DESKTOP_VERSION__` is set. Legacy Desktop set it (`process.env.__COMFYUI_DESKTOP_VERSION__ = app.getVersion()`), and this app does not, so Desktop installs are counted as `git-windows` / `git-mac`. Manager also falls back to `git describe` for the ComfyUI version, which reports `unknown` on installs without a `.git` folder. Fixed data only starts from the release that ships this.

## Provenance
- **Authored by:** interactive session
- **Flow:** interactive request (investigating why registry data shows so few desktop-windows users) → this PR → CodeRabbit review fix (drop an inherited marker for user-managed launches) → review fix (leave legacy `desktop` installs out)
- **Verified:**
  - Tests: `buildLaunchEnv.test.ts` passes (9/9, 3 repeated runs); the 2 inherited-marker tests fail against the pre-review code, and the original 4 fail against `main`
  - Full unit suite: 311/312 files pass; the one failure is listed below
  - Known-failing before this PR: `gpu.test.ts > checkLinuxAmdKfdAccess > warns with render-group guidance when the node is not writable` (also fails without this change; the sandbox runs as root, so the device node is always writable)
  - Typecheck (`typecheck:node`), eslint and prettier on the changed files: clean
  - Not run locally: e2e/lifecycle suites, `typecheck:web` / `:e2e` / `:integration`, full CI matrix

  <details><summary>Commands and summarized results</summary>

  - `vitest run src/main/lib/ipc/buildLaunchEnv.test.ts`: 9 passed (repeated 3×); with `shared.ts` at the pre-review commit: 2 failed (inherited marker, portable and git), 7 passed; with `shared.ts` reverted to `main`: the original 4 fail
  - `vitest run`: 311 files passed, 1 failed (`gpu.test.ts`, same failure on unchanged code); 6763 tests passed, 2 skipped
  - `pnpm run typecheck:node`: no errors
  - `eslint` + `prettier --check` on `src/main/lib/ipc/shared.ts` and the test: clean
  - Ran in a copy of the repo, because the sandbox can't reach `codeload.github.com`. The lockfile there pointed `@electron/node-gyp` at a local tarball built from the same commit; that change is not part of this PR.
  </details>
- **Deviations:** unknown (no ticket or acceptance criteria)

## Reviewer context
- **Type:** bug fix, restores a launch env var legacy Desktop set and this app dropped
- **Slots into:** no project or epic; ad-hoc work
- **Not in scope:** the frontend's own form factor (it reports Windows as `other` because ComfyUI sends `sys.platform` = `win32`, and the PyPI build never reports `desktop-*`), and storing `current_version` on the release-notes registry call. Both are separate changes in other repos.

## Summary
- `buildLaunchEnv` sets `__COMFYUI_DESKTOP_VERSION__` to `getAppVersion()` for `standalone` and `comfybuilder` installs: the ones whose ComfyUI and Manager this app installs and updates.
- Legacy `desktop` installs are left out. For them this app launches the legacy Desktop executable, not ComfyUI, and that app sets the marker itself. On macOS the launch goes through `/usr/bin/open`, which wouldn't pass our env on anyway.
- `portable` and `git` installs never get it, even when the app itself inherited the variable from its environment: `buildLaunchEnv` deletes it for those sources. They are user-managed, so Manager keeps its git-install behaviour there: self-updating `comfyui-manager` and warning when ComfyUI is outdated.
- The key is added to `RESERVED_ENV_VARS`, so a per-install env var can't override or spoof it.
- What Manager (v4 and main) does once the variable is set:
  - reports `form_factor=desktop-win` / `desktop-mac` on its registry `/nodes` calls;
  - reads the ComfyUI version from `pyproject.toml` instead of `git describe`;
  - skips self-updating `comfyui-manager`, which this app pins through `manager_requirements.txt`;
  - drops the "ComfyUI is outdated" warning;
  - in the legacy UI notice, shows `ComfyUI: <app version> [Desktop]`. That matches legacy Desktop, which used the same value.

## Change breakdown
| Category | Files | Added | Deleted | Share of changed lines |
|---|---|---|---|---|
| Product code | 1 (`src/main/lib/ipc/shared.ts`) | 18 | 2 | 24% (20/84) |
| Test code | 1 (`src/main/lib/ipc/buildLaunchEnv.test.ts`) | 64 | 0 | 76% (64/84) |

No documentation, configuration, generated, lockfile or vendored changes.

## Test plan
- [ ] Launch a standalone install on Windows and confirm Manager's registry request carries `form_factor=desktop-win` and a real `comfyui_version` (e.g. via the Manager log or a proxy)
- [ ] Same on macOS (`desktop-mac`)
- [ ] Launch a portable or git install and confirm the variable is absent and Manager still offers to update itself
- [ ] Confirm Manager's "update all" in a standalone install skips `comfyui-manager` and still updates other node packs
- [ ] No feature flag: this restores legacy Desktop behaviour, and the only user-visible effect is the missing outdated-ComfyUI warning, which doesn't apply to app-managed installs

---
_Generated by [Claude Code](https://claude.ai/code/session_013eTJN2NUv11xXiFbzeS3ji)_
