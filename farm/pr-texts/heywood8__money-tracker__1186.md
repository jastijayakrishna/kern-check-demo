# feat(accounts): choose rounding method for automatic transactions

## What

Adds a **rounding method** choice to the per-account automatic-transaction rounding setting. Alongside the existing rounding **step** (Off / 10 / 100 / 1000), the user can now pick how that step is applied:

- **Nearest** — round to the nearest multiple, ties up (the previous, unchanged behaviour)
- **Up** — always round the amount up to the next multiple
- **Down** — always round the amount down to the previous multiple

## Why

Requested: for account rounding, let the user choose the direction — up / down / nearest boundary (as before). Previously rounding of amounts from bank notifications was hard-coded to "nearest, ties up".

## How it works

- Rounding is applied only to the booked amount of operations created (or confirmed from the review queue) from **bank notifications** — same scope as before. The new mode selects the decimal.js rounding constant: `nearest → ROUND_HALF_UP`, `up → ROUND_UP`, `down → ROUND_DOWN` (amounts are non-negative magnitudes, so up/down behave as ceil/floor).
- `NULL` mode is treated as `nearest`, so existing accounts and old backups are unchanged.

## Changes

- **Schema + migration** — new `accounts.auto_txn_rounding_mode` column (`text`, nullable); `drizzle/0014_account_rounding_mode.js`, registered in `migrations.js` + `_journal.json`.
- **`db.js`** — `detectAppliedMigrations` marker **and** `isSchemaComplete` check for 0014 (the latter is required or existing users would skip the migration).
- **`currency.js`** — new `roundToStep(amount, step, mode, currencyCode)` with nearest/up/down; `roundToNearest` kept as a thin backward-compatible wrapper.
- **`processBankNotifications`** — all four rounding call sites (auto-create purchase/transfer + review-queue purchase/transfer confirm) now pass the account's mode.
- **`resolveNotification`** — surfaces `accountRoundingMode` alongside `accountRounding`.
- **`AccountsDB` / `AccountsActionsContext`** — read-map `autoTxnRoundingMode` and persist it in create/update.
- **`AccountsScreen`** — a second segmented control ("Rounding method") shown under the step selector, only when a step is chosen.
- **`BackupRestore`** — column added to CSV export column list and both JSON-restore INSERTs for round-trip fidelity.
- **i18n** — `auto_txn_rounding_mode` + `rounding_mode_nearest/up/down` across all 11 languages (all valid JSON); `en`/`zh` hint reworded to drop "nearest" now that direction is configurable.
- **Tests** — `roundToStep` (all three modes, currency formatting, mode fallback, invalid step) and two notification-processing cases (mode `up` / `down`).

## Notes / design calls

- The mode selector is hidden when the step is **Off** (direction is meaningless with no rounding). `NULL`/unknown mode falls back to `nearest`.
- Existing `roundToNearest` behaviour and all its tests are preserved unchanged.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

