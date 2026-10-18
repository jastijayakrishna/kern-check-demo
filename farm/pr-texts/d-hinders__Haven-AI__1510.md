# fix(mcp): hosted erc7710 settle no longer reports a settled payment as failed (#1508)

Fixes #1508 — the production bug on the **default topology** (hosted MCP + local edge signer).

## The failure

Since #1456, every hosted erc7710 call returned `API_ERROR — "The payment was submitted and is waiting for confirmation."` **The settlement itself always succeeded.** The probes from #1509 pinned it:

```
after_quote=pending_signature
after_sign=pending_signature
after_settle_refused=submitted
```

Only a successful `settleX402` moves an intent to `submitted`, so the failure was strictly *after* settlement.

## Root cause

`deliverMerchantPayment`'s first act is `ensureFundingConfirmed`, and that reads `GET /payments/:id` **unconditionally**:

```ts
async ensureFundingConfirmed(paymentId: string, fundingTxHash?: string): Promise<void> {
  const status = await this.getPaymentStatus(paymentId)   // ← always runs
  await this.waitForFundingTx(fundingTxHash ?? status.txHash ?? undefined, status.chainId)
}
```

`fundingTxHash` gates the on-chain **wait**, never the **read**. By that point the settle had moved the intent to `submitted`, which the backend maps to **409** (`agentPaymentStatusHttpCode`, `agent-payment-status.ts:451`). The SDK threw, and **the merchant was never contacted**.

Deterministic, not a race — which matches it failing every run since 2026-08-15.

The #1456 author passed `undefined` believing it meant "skip":

```ts
// No funding tx to confirm — passing one would make the delivery
// helper wait for a transaction that will never exist.
undefined,
```

A fair reading, because the SDK docstring promised *"No-op when the funding tx hash … is unavailable."* **That sentence was false**, and it's corrected here — the misleading contract is as much the bug as the call site.

## The fix

A `noFundingLeg` option that skips the call **entirely** rather than tolerating its failure. On a scheme with no funding leg there is no transaction to confirm, so the wait is meaningless work whose only reachable effect was this defect.

## Why CI never caught it

The pre-existing test stubbed the payment read as **`200 / 'settled'`**. The real backend answers **409**, because `submitted` is the *expected* end state on erc7710 — the merchant redeems the `[child, budget]` chain afterwards. The fixture described a world we don't ship.

The new test pins the real response and is **mutation-verified**: with the guard forced back on (`if (true)`) it fails on `expect(fundingSpy).not.toHaveBeenCalled()`; with the fix it passes.

## Changed Surfaces

- [ ] Docs / prompts only
- [ ] Frontend UI
- [ ] Backend / API
- [x] SDK
- [x] MCP / hosted MCP / signer
- [x] Money movement, agent authority, or payment execution
- [ ] Generated artifacts, examples, credential handoffs, or demo scripts

## Workflow Used

- Captain: interactive session (owner asked to continue on the production bug)
- Agents used: none
- Agents skipped, with reason: single root cause, bounded diff
- Worker ownership boundaries, if any: n/a

## Local Checks

- [x] `git diff --check`
- [x] Package typecheck/test/build commands, if applicable:
  - `npm run typecheck -w packages/mcp-server` — clean
  - `npm run typecheck -w packages/sdk` — clean
  - `npm run test -w packages/mcp-server` — 218 passed
  - `npm run test -w packages/sdk` — 231 passed
  - Mutation check on the new test — fails against the unfixed branch, passes with the fix
- [ ] Not run, with reason:

## Browser Or Headless Verification

- Browser verification: n/a — no rendered surface
- **Rendered-screen evidence**: n/a
- If skipped, reason: hosted MCP / SDK change
- Headless equivalent, if browser verification was skipped: unit tests above; the real proof is the next `qa-dev` run, where `x402-erc7710-hosted` should go green

## Intentionally Left Out

- **The #1509 diagnostic probes stay in.** They are silent on success and would localise a residual failure. Reverting them is a follow-up once a green run confirms this fix — removing the instrument before reading the result is how you end up re-adding it.

