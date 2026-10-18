# Fix Home app download rejecting available storage

Home rejected the full app download at 0 B even though the Telegram screenshot showed 9.5 GB required and 10.0 GB available. The preflight check silently added a 10% reserve, producing the misleading request to free another 501 MB.

This removes the estimate-based veto. Browser estimates describe approximate per-site storage rather than physical free disk space; actual cache writes now determine whether the download can continue. Integrity checks, completion receipts and verified-file reuse remain enforced.

- Normalize real quota errors for both callers and saved state, explaining browser storage limits and retry.
- Label Home's storage figures as browser estimates.
- Offer the external-browser download action after a quota error inside Telegram, including when its Home Screen shortcut is already installed. Explain that another browser keeps a separate download.
- Preserve saved files; no asset reductions or automatic deletion to make space.

Validation: **121 focused tests pass** (110 Node + 11 component). The new tight-space/underestimated-space regressions reproduce the old rejection, then pass with the fix. Real quota failures during file writes and completion-receipt writes remain resumable and cannot falsely mark the app complete. Full Vite production source compilation passes for all four configured entries; independent review found no blocking issues. The published Git tree exactly matches the reviewed local changes.

Unchanged multi-gigabyte public assets were not downloaded/copied or repackaged for this source-only build. Browser automation could not start, so live Telegram behavior, a new portrait screenshot and a complete physical-device download remain unverified. This PR does not merge or deploy the change.

[Diagnosis, validation and storage API references](https://github.com/TonPlaygramBot/TonPlaygramWebApp/blob/codex/fix-app-download-storage/docs/validation/app-download-storage/README.md)
