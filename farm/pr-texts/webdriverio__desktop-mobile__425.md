# feat(flutter-service): zero-config execute/mock via auto VM-service setup (#405)

Closes #405. **Stacked on #424 (#378)** — review/merge that first; this PR's diff is only the Flutter-specific delta.

Builds on the shared mechanism. The #378 port seam now auto-allocates `appium:dartVmServicePort` per worker (Flutter's `portCapKey`), so `execute`/`mock` are **zero-config** — no hand-pinned port, no up-to-60s log scrape. This PR adds the Flutter-specific preflight.

- **`diagnostics.ts`**: `flutter`-on-PATH check + a fork-presence check that greps the installed `appium-flutter-driver` for `flutter:getVMServiceUrl`, **warning (not erroring)** when absent. We validate the fork — we don't mutate `node_modules` (pnpm-store-unsafe); CI keeps delivering it until the upstream PR lands.
- **launcher**: compose `flutterDoctorChecks` over the shared base checks.
- **README**: document the now-automatic port + the `autoInstallDriver`/`doctor` options.

### Fork delivery — the real exit
The goosewobbler `appium-flutter-driver` fork carries the Android `vm-service-port` intent extra + `getVMServiceUrl`. The iOS half is **already upstreamed** (appium/appium-flutter-driver#870, which invited the Android follow-up). A follow-up upstream PR for the Android half will retire the fork, the CI override, and this doctor check entirely.

### Tests
106 flutter-service tests (+6 diagnostics).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
