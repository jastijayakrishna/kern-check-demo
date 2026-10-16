# Port capacitor-updater changes since 2026-09-14 (8.52.x through 8.53.0)

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

Syncs `@capgo/electron-updater` with relevant `@capgo/capacitor-updater` changes after the last electron-updater alignment (2026-09-14), through release **8.53.0**.

## Ported vs skipped

| Area | Capacitor reference | Electron status | Notes |
|------|---------------------|-----------------|-------|
| HTTPS to HTTP redirect block | [8.52.0](https://github.com/Cap-go/capacitor-updater/compare/8.51.25...8.52.0), `allowHttpsToHttpRedirect` in definitions | **Ported** | Default blocked; opt in via config |
| Zip slip / path traversal | [#919](https://github.com/Cap-go/capacitor-updater/pull/919), [#920](https://github.com/Cap-go/capacitor-updater/pull/920), [#938](https://github.com/Cap-go/capacitor-updater/pull/938) | **Ported** | Shared `path-security` helpers; safe bundle ids |
| Checksum before unzip | [#938](https://github.com/Cap-go/capacitor-updater/pull/938) | **Ported** | Verify SHA256 before decrypt and extract |
| Stricter AES session handling | [4f6d677](https://github.com/Cap-go/capacitor-updater/commit/4f6d677), CryptoCipher | **Ported** | 16 byte IV and AES key validation |
| Manifest requires `sessionKey` when `publicKey` set | [#917](https://github.com/Cap-go/capacitor-updater/pull/917) | **Ported** | Download and manifest paths |
| Rollback on `appReadyTimeout` | [314fa53](https://github.com/Cap-go/capacitor-updater/commit/314fa53), [8.52.0](https://github.com/Cap-go/capacitor-updater/releases/tag/8.52.0) | **Ported** | Calls `rollback()` before reload |
| Stale `notifyAppReady` after reload | [8.52.0](https://github.com/Cap-go/capacitor-updater/releases/tag/8.52.0) | **Ported** | Reload generation guard |
| Clear `next` on `set()` | [#948](https://github.com/Cap-go/capacitor-updater/pull/948) | **Already present** | Verified in `BundleManager.set` |
| `reload()` applies pending when delays met | [d6c5021](https://github.com/Cap-go/capacitor-updater/commit/d6c5021) | **Ported** | Matches native docs |
| `autoUpdate` string modes | definitions 8.52.x | **Ported** | `off`, `atBackground`, `atInstall`, `onLaunch`, `always`, `onlyDownload` |
| `updaterEvent` unified listener | [#956](https://github.com/Cap-go/capacitor-updater/pull/956), **8.53.0** | **Ported** | Legacy events still emitted |
| `update_check_error` stats | [#956](https://github.com/Cap-go/capacitor-updater/pull/956), [#971](https://github.com/Cap-go/capacitor-updater/pull/971) | **Ported** | Failed background checks only |
| `updateCheckResult` event | definitions 8.45.11+ | **Ported** | Emitted on auto check |
| `set` / `setNext` events | definitions | **Ported** | On apply and queue |
| `conditionMode` AND/OR delays | [#955](https://github.com/Cap-go/capacitor-updater/pull/955) | **Ported** | Persisted in storage |
| `allowSetDefaultChannel` / `unsetChannel` guard | [#924](https://github.com/Cap-go/capacitor-updater/pull/924) | **Ported** | `disabled_by_config` error code |
| `reset({ usePendingBundle })` | definitions | **Ported** | |
| `nativeUpdatePrompt` | [#968](https://github.com/Cap-go/capacitor-updater/pull/968) | **Ported (Electron)** | `dialog` + optional `shell.openExternal(link)` |
| Types and docs | 8.52.x through 8.53.0 | **Ported** | README, FEATURE_SPECIFICATION |
| Android/iOS background download worker | [04b753f](https://github.com/Cap-go/capacitor-updater/commit/04b753f) | **Skipped** | No Android Activity on Electron |
| Play flexible / in-app update APIs | definitions | **Skipped** | Mobile store only |
| Preview session APIs (`allowPreview`, `listPreviews`, …) | 8.47+ | **Skipped** | Not in electron scope this pass |
| `autoSplashscreen` / loader | definitions | **Skipped** | Capacitor splash-screen only |
| Logger eval injection hardening | [#923](https://github.com/Cap-go/capacitor-updater/pull/923) | **Skipped** | Android WebView logger bridge |
| Maestro / example-app CI | many commits | **Skipped** | Not applicable to this package |
| Remove bundled native deps (8.52 breaking) | [8.52.0](https://github.com/Cap-go/capacitor-updater/releases/tag/8.52.0) | **Skipped** | Electron has no bundled mobile SDK |

## Tests

- `path-security`, `auto-update-mode`, `download-manager` session key guard
- `delay-manager` OR mode, `events` `emitUpdaterEvent`, crypto IV validation
- `constants` `update_check_error`

## Version

Package and `PLUGIN_VERSION` bumped to **0.0.8**.

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-69dc09e9-2189-585d-bf36-d00e94e29da0?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-69dc09e9-2189-585d-bf36-d00e94e29da0&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

<!-- codesmith:footer -->
---
<a href="https://app.blacksmith.sh/Cap-go/codesmith/electron-updater/pr/7?autoLogin=true&ref=codesmith_pr_footer"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v3.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-light-v3.svg"><img alt="View with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v3.svg"></picture></a> <a href="https://backend.blacksmith.sh/track/enable-autofix?expires=1794618698&installation_model_id=430928&pr_number=7&ref=codesmith_pr_footer&repository=Cap-go%2Felectron-updater&return_to=https%3A%2F%2Fgithub.com%2FCap-go%2Felectron-updater%2Fpull%2F7&signature=9a2341f15965899eac5d7c01bd5e02a12d48c130c4c6a5e5959fa61af4879bfc"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-light.svg"><img alt="Autofix with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"></picture></a>
<sup>Need help on this PR? Tag <code>@codesmith-bot</code> with what you need.</sup>

<!-- codesmith:autofix:disabled -->
<!-- /codesmith:footer -->

<!-- This is an auto-generated description by cubic. -->
<a href="https://cubic.dev/pr/Cap-go/electron-updater/pull/7?utm_source=github" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/review-in-cubic-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/review-in-cubic-light.svg"><img alt="View guided diff" src="https://www.cubic.dev/buttons/review-in-cubic-light.svg"></picture></a> <a href="https://www.cubic.dev/action/auto-fix/pr/Cap-go/electron-updater/7?returnTo=https%3A%2F%2Fgithub.com%2FCap-go%2Felectron-updater%2Fpull%2F7&source=description" target="_blank" rel="noopener noreferrer" data-no-image-dialog="true"><picture><source media="(prefers-color-scheme: dark)" srcset="https://www.cubic.dev/buttons/turn-on-auto-fix-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://www.cubic.dev/buttons/turn-on-auto-fix-light.svg"><img alt="Turn on auto-fix" src="https://www.cubic.dev/buttons/turn-on-auto-fix-light.svg"></picture></a>
<!-- End of auto-generated description by cubic. -->



<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Added configurable automatic update modes, including background checks, download-only behavior, and context-based update installation.
  * Added optional native-update reminders with configurable messages and cooldowns.
  * Added update-result, bundle-change, and unified updater events, plus AND/OR logic for delayed updates.
  * Added controls for resetting to a pending bundle and changing whether the default channel can be unset.

* **Security**
  * HTTPS-to-HTTP redirects are blocked by default, and encrypted downloads require a session key when encryption is configured.
  * Improved validation of bundle identifiers, file paths, and encryption key lengths.

* **Documentation**
  * Clarified that encrypted bundles remain unreadable by Capgo and that checksum verification occurs before unzipping.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
