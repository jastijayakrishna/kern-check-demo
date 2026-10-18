# feat(mobile): add Firebase Crashlytics alongside Sentry

## What & why

Adds **Firebase Crashlytics** to the mobile app, **alongside** Sentry — not replacing it. Sentry stays the primary reporter and the triage surface.

The justification is one specific gap. **Sentry arms from JavaScript, so a crash that happens before its `init()` completes is invisible to it, by construction.** That is not hypothetical here — it is the last shipped outage:

> `docs/COLD-START-CRASH-RCA-2026-08-21.md` (**MOB-BOOT-04**) — build #31 died at `app/_layout.tsx` module scope because `@sentry/react-native`'s own import threw under the New Architecture. The crash reporter *was* the crash. Nothing was reported, and the failure had to be diagnosed from a photograph of a tester's phone.

Crashlytics has no such dependency: the Firebase Android SDK arms from a `ContentProvider` during Application startup, before React Native loads and before the Hermes bundle is evaluated.

⚠️ **This deliberately bends a rule in `docs/APP-SIZE.md`** ("one SDK per use case … never add a second analytics/telemetry SDK alongside it"). That is argued explicitly rather than slipped past — see `docs/CRASHLYTICS.md` §1 and the new audit-table row. If MOB-BOOT-04-class boot crashes stop feeling like a live risk, **this** is the SDK to drop, not Sentry.

Full spec, provisioning and caveats: **`docs/CRASHLYTICS.md`** (new).

### What's wired

| File | Role |
|---|---|
| `src/telemetry/crashlytics.ts` | JS seam. Same contract as `sentry.ts`: deferred require, never throws on the boot path, inert without provisioning. |
| `app/_layout.tsx` | `bootStep(initCrashlytics)`; `bootStep`'s catch now reports to **both** reporters. |
| `app.config.ts` | Both config plugins, attached **only** when a `google-services.json` is present. |
| `firebase.json` | The three flags RNFirebase 21.14.0 actually reads. |
| `src/ui/index.tsx` | LR20 forced-crash gate now covers both pipelines. |
| jest mocks + `tools/parity/` shims | Both lanes render as unprovisioned builds. |

**No new credential** — Crashlytics rides the same `google-services.json` that already provisions FCM push. The founder step is one click: Firebase console → Release & Monitor → Crashlytics → Enable.

A few decisions worth surfacing:

- **Plugins are gated on `googleServicesFile`** because the app plugin's Android mod *throws* without `android.googleServicesFile` (verified in the installed plugin source). Attaching unconditionally would break prebuild for local dev and the QA APK lane.
- **`crashlytics_javascript_exception_handler_chaining_enabled` is load-bearing** — it is what keeps Sentry seeing unhandled JS errors with a second handler installed.
- **The QA gate kept two buttons, not four.** RN's Android `Alert` slices `buttons` to three and *silently drops the rest*, so a fourth option would render as a gate that looks present and tests nothing. Each existing button now exercises both reporters.
- **Two flags deliberately omitted** from `firebase.json`: `crashlytics_ndk_enabled` and `crashlytics_debug_enabled` exist as constants in 21.14.0 but are **not read** by the init provider — writing them would be config that looks like it does something and does nothing.

## Risk & rollout

- **User-facing?** No new UI. Only the QA test-build banner's forced-crash dialog changes, and that renders nothing in a store build.
- **DB migration?** No.
- **Wire-contract change?** No.
- **Mobile:** **Needs a new binary (native change).** New native modules + Gradle plugins shift the expo-updates `fingerprint` runtimeVersion — no OTA can carry this, and no OTA can repair it (REL-01/REL-02).

**Size:** measured `expo export --platform android`, before vs after on this branch:

| | Before | After | Δ |
|---|---|---|---|
| Hermes JS bundle | 6,206,687 B | 6,348,686 B | **+141,999 B (+2.29%)** |
| Android export total | 6,558,323 B | 6,700,322 B | **+141,999 B (+2.17%)** |

Within budget, so **`size-budget.json` was NOT raised** — but Hermes headroom falls **3.8% → 1.6%** (≈104 KiB). Flagged rather than 
