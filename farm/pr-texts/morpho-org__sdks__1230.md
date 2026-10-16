# fix(morpho-sdk): reserve accrual buffer under target caps in blue reallocations

## Summary

Fixes the `AbsoluteCapExceeded()` reverts on Arc borrows (VAU-2118, [incident thread](https://morpholabs.slack.com/archives/C07G53ZCV5K/p1790767135815289), e.g. [tx](https://arc.etherscan.io/tx/0xed956a609a1c287292ae9f15b92a4eb9ef3dbf871412783c8e53779cef17147f)).

`computeVaultV2BlueReallocationsAtUtilizationInPlace` sized the target-market allocation exactly to `absoluteCap − allocation` at the snapshot `timestamp`. The vault's existing allocation accrues a few wei of interest between the quote block and the mined block, so the BluePublicAllocator / Vault V2 post-allocate cap check fails whenever the cap is the binding constraint (always the case on a market at 100% utilization, since the planner tries to bring it back to 90%).

Change: canonical market/vault state and the returned post-state stay at `timestamp`. Each (vault, adapter, market) position involved in the plan gets a cap reserve equal to the interest its shares would accrue through `timestamp + capAccrualBuffer`. That reserve is added in every target-cap check: `allocatorHeadroom` (BluePublicAllocator cap), `blockedTargetIds`, and the cap-compatibility probe (all three Vault V2 cap ids), for both the `allocateFromIdle` and `reallocate` paths.
- Target position: reserved on all target cap ids.
- Market-source position: reserved on the cap ids it shares with the target (adapter id, shared collateral id), because on-chain `deallocate` books that interest onto those ids too.
- Reserves carry across legs and passes. Positions from accepted legs stay counted in every later leg's checks for that vault. The reserve state is a plan-scoped `CapReserveState` created once per plan and passed alongside the copy-on-write `SimulationContext`, so the `borrow`/`withdraw` fallback pass (second planner call at `maxWithdrawalUtilization = WAD`) reuses the friendly pass's snapshot, touched pairs and memoized reserves instead of starting fresh.
- Reserves are frozen at pre-plan state. They are computed once from a pre-plan market snapshot and the pre-plan shares, so a leg that changes utilization or rate does not shrink later reserves.
- Projections are lazy and memoized. A forward accrual runs only when a cap check actually needs that position's reserve. This means unsupported-IRM targets still return an empty plan, and an unused source projection cannot throw.

Vault accrual and relative-cap denominators are unchanged (the probe still runs at `timestamp`), so the buffer can only make plans more conservative.

```ts
// VaultV2BluePublicAllocatorOptions
readonly capAccrualBuffer?: BigIntish; // seconds, default DEFAULT_CAP_ACCRUAL_BUFFER = 2h, 0n disables (validated up front)

interface CapReservePair { key; ids: AdapterIds; reserve: () => bigint } // key = vault:adapter:marketId
CapReserveState = { initialMarkets, marketAccruals, touchedPairs, reserveByPairKey } // one per plan (createCapReserveState), shared by friendly + fallback passes
pair.reserve = memo(() => zeroFloorSub(
  initialMarkets[id].accrueInterest(timestamp + capAccrualBuffer).toSupplyAssets(preplanShares),
  initialMarkets[id].accrueInterest(timestamp).toSupplyAssets(preplanShares),
));
capReserve(vault, capId, candidatePairs) =
  sum(pair.reserve() for pair in dedupe(touchedPairs[vault] ∪ candidatePairs) if pair.ids.includes(capId));

allocatorHeadroom = config.getMaxIn(allocation + untracked + targetPair.reserve());
withinCap = allocation.allocation + capReserve(vault, id, [targetPair, sourcePair?]) <= capacity; // probe
// on accept: touchedPairs[vault] += targetPair, sourcePair
```

Note on the buffer value: the Public Allocator V1 planner had no explicit cap buffer (its docs said it added no implicit delay margin). This PR reuses the SDK's existing 2h forward-accrual horizon, the same default as the Permit/authorization deadline.

Tests:
- Idle and market-source plans (with and without `operation: borrow/withdraw`) stay `< headroom` by exactly the projected interest, and match the old value with `capAccrualBuffer: 0n`.
- Incident reproduction: the buffered plan applied at `timestamp + 2h` stays `<= absoluteCap`, while the unbuffered plan applied one second later exceeds it.
- Binding shared adapter-id cap: the market-source candidate is dropped by default and kept with `0n`.
- Multi-leg plans applied at the horizon stay under every target cap, with exact leg sizes and final allocation `= absoluteCap − reserves`: a market leg followed by an idle leg on a shared cap, and an idle leg followed by a cap-sized market leg (frozen target reserve).
- Friendly pass + fallback pass (`maxWithdrawalUtilization` 0.7, target adapter-market cap binding at `allocation + shortfall + reservePrePlan + 1`): the plan fits only with the frozen pre-plan reserve (a reserve recomputed from post-friendly state throws `InsufficientSharedLiquidityError`), and the final allocation is exact.
- `getAvailableLiquidityToUtilization` forwards `capAccrualBuffer` (default < `0n`; `0n` includes the full cap headroom).
- BluePublicAllocator max-in with loose vault caps: the default plan is smaller than the `0n` plan by exactly the projected target-share interest.
- Unused source projection on a market without `rateAtTarget` does not throw.
- An unsupported-IRM target returns `[]`.
- The returned target market has `lastUpdate === timestamp`.
- A binding relative cap gets strictly tighter.
- `getPublicReallocationLiquidity` forwards the option.
- A negative buffer throws `NegativeInputError` up front.

The fork test keeps the exact relative-cap maximum with `0n` and broadcasts the default-buffer plan. Changeset: `@morpho-org/morpho-sdk` minor (new export + option).

Link to Devin session: https://app.devin.ai/sessions/02b2870bde4d4dda87ce8b700159bcc4
Open in Devin Desktop: https://app.devin.ai/desktop/session/02b2870bde4d4dda87ce8b700159bcc4?variant=devin
Requested by: @0xbulma
