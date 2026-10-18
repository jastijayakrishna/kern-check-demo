# feat(operations): exclude a single operation from spending average

## What

Adds a per-operation **"Exclude from spending average"** toggle on the **edit operation** modal. When enabled, that operation is left out of the daily spending average and the burndown forecast, while still counting as a normal expense everywhere else (account balances, pie charts, category totals). This lets a one-off large purchase not skew the forecast.

## Why

Requested: an option to exclude a single operation from being counted in the average spending used by the burndown/forecast. Conceptually the successor to the old category-level `exclude_from_forecast` (removed in migration 0004), but now per-operation and more granular.

## How it works

- The forecast/daily-average is derived solely from `getTotalExpenses` (consumed only by the balance-history hook), so the exclusion is applied there and nowhere else — the account balance line still reflects the real expense; only the forecast slope ignores it.

## Changes

- **Schema + migration** — new `operations.exclude_from_avg` column (`integer`, default 0); `drizzle/0013_operation_exclude_from_avg.js`, registered in `migrations.js` + `_journal.json`.
- **`db.js`** — `detectAppliedMigrations` marker **and** `isSchemaComplete` check for 0013 (the latter is required or existing users would skip the migration).
- **`OperationsDB`** — map `excludeFromAvg` (boolean) on read; persist in create/update/split (split children inherit the parent's flag); filter flagged ops out of `getTotalExpenses`. New column placed before `latitude`/`longitude` in every INSERT so those stay the last params.
- **`OperationModal` + `useOperationForm`** — react-native-paper `Switch` row, shown for **edited, non-shadow expense** operations.
- **`BackupRestore`** — column added to CSV export and JSON restore for round-trip fidelity.
- **i18n** — `exclude_from_average` + `exclude_from_average_hint` across all 11 languages (parity verified: all 513 keys, all valid JSON).
- **Tests** — read-mapping, create/update persistence, and the `getTotalExpenses` exclusion.

## Notes / design calls

- Toggle is **edit-only** and **expense-only** (the average is expense-based); applied via **Save**.
- ⚠️ I could not run `npm test` locally (no node/npm in the dev environment). Edits were designed to keep existing assertions green; **CI is the source of truth for the suite here.**

🤖 Generated with [Claude Code](https://claude.com/claude-code)
