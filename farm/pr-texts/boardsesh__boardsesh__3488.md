# fix(mobile): pin RN fetch to kill expo/fetch NativeResponse crash

## Summary

A fatal, unhandled `EXC_BAD_ACCESS` (`EXC_ARM_DA_ALIGN`, PC → `0x2`) is crashing the production iOS app (`com.boardsesh.app@2.2.0+5`, channel `production`) — [Sentry 7595562195](https://boardsesh.sentry.io/issues/7595562195/).

**Root cause (not our code).** Expo 57's WinterCG runtime installs `expo/fetch` as the global `fetch` (`node_modules/expo/src/winter/runtime.native.ts:52`). `expo/fetch`'s native `NativeResponse.state.didSet` hops onto a background dispatch queue and clears its `stateChangeOnceListeners` there (`ios/Fetch/NativeResponse.swift:15-20`). Those listeners capture the JS promise resolvers, so releasing them off the JS thread runs `facebook::jsi::Object::~Object` / `JavaScriptPromise` deinit on the wrong thread → Hermes JSI pointer corruption → the crash on the report's Thread 15. Every GraphQL HTTP POST (`graphql-request` → `authenticatedFetch` → global `fetch`) routes through it, so it hit hard.

**Fix.** Set `EXPO_PUBLIC_USE_RN_FETCH=1`. Expo then leaves the global `fetch` as React Native's XHR/`whatwg-fetch` implementation, which never touches `NativeResponse`. This is Expo's own supported opt-out (`runtime.native.ts:41-53`), and babel-preset-expo special-cases this exact var for `node_modules` inlining ([expo/expo#46982](https://github.com/expo/expo/issues/46982)), so it folds `useRnFetch → true` inside Expo's own runtime.

**Ships as an OTA hotfix — no store build needed.** The flag is referenced only in Expo's JS runtime, never in `app.config.ts`, so it doesn't enter the resolved Expo config and **does not move the fingerprint**. Verified empirically — `expo-updates runtimeversion:resolve` is byte-identical (`64ef94bc…`) with and without the `.env` line. So a production OTA republish reaches the already-installed 2.2.0 binaries and kills the crash.

`graphql-request` only does JSON POSTs, which RN fetch fully supports — no functional regression.

### What changed
- Added `EXPO_PUBLIC_USE_RN_FETCH: '1'` to every mobile bundling context: `mobile-ota-production.yml` (the hotfix), `ios-testflight-rn.yml` / `android-apk-rn.yml` (both gate + build `.env`), `android-apk-dev-client.yml`, and the `mobile-ota-preview/backport/check` workflows.
- Added the key to `mobile-ota-compat-check.ts`'s `ENV_KEYS` so the **preview publish** ships the same behaviour (otherwise PR testers would still hit the crash).
- Guarded it in `mobile-ci-env-parity.test.ts` (`SHARED_ENV_KEYS`) so it can't silently drop out of one channel and revert it to the crashing `expo/fetch`.
- Documented in `docs/mobile-ota-updates.md` and `packages/mobile/.env.example` (so local dev matches production).

## Release Notes

- Fixed a rare crash that could close the app while it was loading climbs.

## Test plan

- `vp test run mobile-ci-env-parity mobile-ota-compat` — 56 passed (parity test now guards the flag across all six fingerprint workflows).
- `vp check` on all changed files — format + lint + types clean.
- **Fingerprint OTA-compatibility verified empirically**: `bunx expo-updates runtimeversion:resolve --platform ios` returns the identical hash with and without `EXPO_PUBLIC_USE_RN_FETCH=1` in `.env` → the fix is bundle-only and delivers over OTA to shipped binaries.
- **Mechanism verified at the source**: `runtime.native.ts:41-53` gates the global-fetch install on this var, and `babel-preset-expo/configs/expo.js:234-239` explicitly inlines it inside `node_modules` — so the flag genuinely reaches Expo's runtime and skips `install('fetch', …)`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
