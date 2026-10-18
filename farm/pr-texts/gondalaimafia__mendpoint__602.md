# fix(ops): trigger the customer backup on-machine at a cadence derived from the RPO

## What this fixes

`GET /ready` on `mendpoint-fettler-production` intermittently failed on exactly one check, `last_verified_backup: "overdue"`. The evidence on the volume was valid, not missing: HMAC verified under `customer-backup-key-v2`, just old.

The cause was the trigger, not the backup. `customer-backup.yml` asked for a once-per-30-minutes cron against a 3600s RPO, and GitHub drops high-frequency crons. The scheduled deliveries this repo actually received landed **2h13m to 8h23m apart, every gap wider than the RPO**, and every run that fired succeeded. The backup already runs on the customer machine, so the workflow was only reaching in over SSH to run `scripts/customer-backup.ts`.

This moves the **trigger** onto the machine. It does not port the backup.

## Where it lives, and why

Least privilege decided the host. `customerWardenChildEnvironment` strips every sensitive value per child and restores only that role's list:

| role | `MENDPOINT_BACKUP_KEY` | object-store credentials | can take a backup |
|---|---|---|---|
| `worker` | no | no | no |
| `api` | yes | no | no |
| `backup` | **added here** | already had them | yes |

A scheduler in the worker would have spawned a child throwing `customer_backup_key_required` on every tick: loud, but never once taking a backup. The `backup` role already existed for this credential set and was used only for the startup object-store probe, so the privilege delta is **exactly one variable**.

**Behaviour change, stated plainly:** `MENDPOINT_APPLICATION_DATA_KEY` is deliberately withheld from the backup role, so the key-distinctness check at `disaster-recovery.ts:1080-1087` **no longer runs at backup time**. `customerBackupInputFromEnv` *skips* distinctness when the app key is absent, so on the backup path enforcement becomes **advisory rather than a hard refusal**: a backup key wrongly equal to the application data key would no longer be refused at backup time, and would instead surface as `/ready` `last_verified_backup: missing_or_invalid`. That is acceptable because the hard refusal still runs where the key *is* present -- boot preflight and the api process -- so a machine cannot start in that state; the alternative was giving the backup process the ability to decrypt live application data.

## The changes

- **Cadence, object-store budget and hard kill all derive from `CORE_DISASTER_RECOVERY_POLICY.rpoSeconds`** — the same policy object `customerBackupInputFromEnv` attaches to the input `assessCustomerBackupReadiness` measures against. Half the RPO, so a whole run can be missed and the evidence is still current. This reconciles the 4h `MENDPOINT_BACKUP_OPERATION_TIMEOUT_MS` in `fly.customer-warden.toml`: a 4h budget cannot hold against a 30-minute cadence, so the schedule wins and the child is told so explicitly.
- **Configuration is proved through both layers** (`customerBackupInputFromEnv` *and* `loadCustomerObjectStoreConfig`) before `assessCustomerBackupReadiness` is read, because its outer catch turns "cannot evaluate" into `missing_or_invalid`, indistinguishable from "no backup yet". A role that cannot publish now reports itself misconfigured instead of spawning a doomed child every tick.
- **Non-critical supervision.** `start-fly.mjs` gains an explicit `{ critical }` option. The backup child is the first whose death must not be fatal, so its exit is logged and retried with backoff (30s doubling to 10m, reset after a clean uptime window) instead of escalating to a machine shutdown. It is started only on the customer profile, and every idle path parks on a **ref'd** timer.
- **Dead-owner fence reaped at boot**, before `initializeWithMutationLease` — the only point where that is reachable, since the scheduler is started inside the lease closure. `recoverStaleMutationMarker` already had a manual caller (`npm run backup:fence:recover`); what it lacked was an automatic one, so recovery needed a human exactly when the machine would not start.
- **Process-group kill** so a t
