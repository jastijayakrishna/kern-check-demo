# feat(layby): Expired tab at Hub 1 — warehouse returns expired laybys to stock

Hub 1 holds the parcels, so hub 1 clears the expired ones. Store credit stays a till job — nothing here touches money.

## ⚠️ Do not deploy alone

**Store-app half of a two-repo change.** Until the POS half lands, a clerk could return an expired layby to stock while a cashier can still tap "Request this layby" for goods already back on the shelf. Deploy both together.

## What it does

An **Expired** tab in the Hub 1 layby view: past-due, still-open laybys, oldest first. Tap **View items** to see the actual contents, then **Confirm return** — units go back to Hub 1 as `received` movements and the layby goes terminal.

## Three things worth reviewing

**Expired is derived, never stored.** No layby record has ever carried status `expired`. `contract.isLaybyExpired` mirrors the POS's `isOverdue` exactly — if the two apps disagree, the warehouse returns goods the POS still thinks are live.

**`received`, not `return` — forced by the rules.** `return` requires stockRole `pos|store|admin`; `received` allows `warehouse|admin`. The people doing this are warehouse staff, so a `return` movement would be refused by RTDB on every line. Mutation-proved.

**Contents come from the POS sale.** A layby record has only `itemCount` — no product, size or qty. Lines live on `/pos/sales/{saleId}/lineItems`. On live data **29 of 30 resolve, 1 doesn't**, so the flow refuses rather than guesses, shows the list before committing, and returns only what's still held after a partial refund.

## Hazards closed

- **Double-return** → create-if-absent transaction on a claim node; one winner, loser is told who has it
- **Mid-parcel failure** → claim released (retryable), reports how far it got, no silent auto-reversal

New terminal status `expiredReturnedToStock`, distinct from `returned` (customer-cancelled, POS-initiated) — the POS message depends on telling them apart.

## Verification

**981 tests** (17 new). Mutations: dropping the claim fails 2; `received`→`return` fails 1; allowing partial returns fails 1.

Also caught pre-merge: the mount passed `stockRole`, not in scope in `WarehouseView` — a runtime ReferenceError the build doesn't catch. Now uses `crActorRole`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01C2e2jhVmVmRaUwqgXmvGDq

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Added an Expired sub-queue for laybys that have passed their due date.
  * Staff can review expired parcel items, validate return destinations, and return eligible stock to inventory.
  * Added status and error feedback for successful, duplicate, invalid, or partially failed returns.
  * Expired laybys are routed to the appropriate storage hub and processed safely.

* **Bug Fixes**
  * Prevented duplicate expired-layby returns and restored claim state when stock updates fail.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
