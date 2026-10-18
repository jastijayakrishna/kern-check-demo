# test(qa): probe the intent status across the erc7710 hosted handoff (#1508)

## Summary

**Temporary diagnostic — to be reverted once #1508 is understood.** No fix here; this makes the failing run answer a question I could not answer by reading code.

`x402-erc7710-hosted` fails at settle with *"The payment was submitted and is waiting for confirmation"* — the intent is already `submitted` when settle runs. Three things in the code say that cannot happen:

| Step | Claim |
|---|---|
| `haven_pay_mcp_tool` (erc7710 branch) | only PREPARES — `prepareX402Erc7710`, `tools.ts:881-935` |
| signer `haven_sign({ payment_id })` | read-only `GET /x402/:id/sign-context`, `sign-context.ts:66` |
| `POST /x402/:id/settle` | the only caller of `markIntentSubmittedForSettlement` |

One of those is false in the deployed system. Reading more code will not say which — so this samples `GET /payments/:id` at each boundary and folds the trail into the failure detail.

## What it adds

- `after_quote` — right after the hosted quote returns
- `after_sign` — right after the local signer returns, before settle is called
- `after_settle_refused` — in the refusal path, plus the `payment_id`

Read-only, and it **never fails the leg on its own** (a read failure is reported as `read-failed(<code>)`, not thrown). A probe that could fail the run would layer a second failure mode onto the one under investigation. The trail goes into the failure *detail* rather than stdout because the run report is the only artefact that survives the runner.

## How to read the result

| Trail | Means |
|---|---|
| `after_quote=submitted` | the hosted quote is submitting — the prepare/submit split (#1456) is not holding |
| `after_quote=pending_signature after_sign=submitted` | the signer's "read-only" fetch is not read-only |
| both `pending_signature`, refusal anyway | settle is refusing for a reason unrelated to status, and the error string is misattributed |

That third case is live: `settleX402`'s own guard returns ``Payment is ${intent.status}, expected pending_signature`` (`settle.ts:33-35`), which is **not** the string we see. The observed text is `describeAgentPaymentStatus`'s (`agent-payment-status.ts:355`).

## Already ruled out (recorded on #1508)

1. **Idempotency replay** — `findExistingByKey()` returns `null` without an `idempotency_key`; this leg passes none.
2. **The signer's fetch mutating state** — documented and implemented as a read-only GET.
3. **Sibling-leg leakage** — `x402-hosted-mcp-signer` fails on response shape before signing or settling.
4. **A stale hosted deploy** — old `main` REQUIRED `payment_header` (`z.string().min(1)`) and contains zero `submitX402Erc7710`; that build would have failed at the schema with `INVALID_INPUT`, not `API_ERROR`. Owner also confirmed in Railway: Source = `dev`, `HAVEN_API_URL` = `havenbackend-dev-8b95` — so both 2026-08-06 faults are excluded too.

## Changed Surfaces

- [ ] Docs / prompts only
- [ ] Frontend UI
- [ ] Backend / API
- [ ] SDK
- [ ] MCP / hosted MCP / signer
- [ ] Money movement, agent authority, or payment execution
- [ ] Generated artifacts, examples, credential handoffs, or demo scripts

QA harness only (`packages/qa-agent`). No product code. Adds read-only observation to a leg that is already failing.

## Workflow Used

- Captain: interactive session (owner asked to continue on the production bug)
- Agents used: none
- Agents skipped, with reason: single-file diagnostic
- Worker ownership boundaries, if any: n/a

## Local Checks

- [x] `git diff --check`
- [x] Package typecheck/test/build commands, if applicable:
  - `npm run typecheck -w packages/qa-agent` — clean
  - `npm run test -w packages/qa-agent` — 155 passed, 13 files
- [ ] Not run, with reason:

## Browser Or Headless Verification

- Browser verification: n/a — no rendered surface
- **Rendered-screen evidence**: n/a
- If skipped, reason: QA harness change
- Headless equivalent, if browser verification was skipped: the dispatched `qa-dev` run is the verification

## Intentionally Left Out

- **Any fix for #1508.** 
