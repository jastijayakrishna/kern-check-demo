# test(qa): make the hosted funding-leg runnable, not skipped (#1441)

Corrects #1512. QA fixture only — no product code, no Haven-side behaviour change.

## What #1512 got wrong

It made `x402-hosted-mcp-signer` **skip** on an erc7710 quote, arguing the funding-leg invariant was unreachable once #1450 made Haven prefer erc7710, and that coverage existed elsewhere. The live run rejected that on the repo's own terms:

```
⚠ green-with-skips: 1 scenario(s) NEVER RAN
✗ QA_REQUIRE_ALL_LEGS=1: refusing to report green with unexercised legs
```

`QA_REQUIRE_ALL_LEGS=1` is set as a repo variable. I wrote that escalation into my own comment and doc and never checked whether the flag was on.

The policy is stronger than "covered somewhere" — **a leg that does not RUN is not coverage** — and it's right: this is the topology #1138 broke while every gate stayed green, which is why #1154 exists.

## The fix: make it runnable

`vpn_pro` becomes deliberately **EIP-3009-only**, and the leg buys `{plan:'pro'}` at both quote and settle.

**This does not weaken #1450 and changes no Haven code.** The preference rule still prefers erc7710 wherever advertised. Withholding it on *one otherwise-unused demo product* reproduces the merchant shape that dominates the real world — ≈every live x402 merchant is EIP-3009-only, as the epic itself notes — so the funding-leg path stays exercised end to end.

Blast radius checked: every other leg buys `vpn_basic`; `storage_50gb` remains the verify-without-settle sweep fixture; **all 56 demo-merchant tests pass** with the narrowed product (none pinned its settlement methods).

## The skip branch is retained, re-scoped

From *expected outcome* to **fixture-regression detector**. Reaching it now means `vpn_pro` started advertising erc7710 again or the leg was repointed, and the message names the exact file and field to check. Under `QA_REQUIRE_ALL_LEGS=1` that skip fails the run — the intended alarm.

New assertions pin that **both** the quote and the settle buy `pro`; a mismatch there would settle a different purchase than the one authorized.

## Changed Surfaces

- [ ] Docs / prompts only
- [ ] Frontend UI
- [ ] Backend / API
- [ ] SDK
- [ ] MCP / hosted MCP / signer
- [ ] Money movement, agent authority, or payment execution
- [ ] Generated artifacts, examples, credential handoffs, or demo scripts

QA harness + demo-merchant **test fixture** (`packages/qa-agent`, `packages/demo-merchant-mcp`). No Haven product code.

## Workflow Used

- Captain: interactive session (owner approved this approach after the failed run)
- Agents used: none
- Agents skipped, with reason: bounded fixture change
- Worker ownership boundaries, if any: n/a

## Local Checks

- [x] `git diff --check`
- [x] Package typecheck/test/build commands, if applicable:
  - `npm run typecheck -w packages/demo-merchant-mcp` / `-w packages/qa-agent` — clean
  - `npm run test -w packages/demo-merchant-mcp` — 56 passed
  - `npm run test -w packages/qa-agent` — 160 passed
- [ ] Not run, with reason:

## Browser Or Headless Verification

- Browser verification: n/a — no rendered surface
- **Rendered-screen evidence**: n/a
- If skipped, reason: harness/fixture change
- Headless equivalent, if browser verification was skipped: the `qa-dev` run after the demo-merchant redeploys, which should be 13/13 with **zero** skips

## Intentionally Left Out

- **Unsetting `QA_REQUIRE_ALL_LEGS`** — that would weaken a deliberate guard to fit my change rather than fixing the change.
- **`packages/mcp-server`'s exact `@haven_ai/sdk` pin** where CLAUDE.md requires `"*"` — unrelated, still a live trap.
- **Recording the merchant settlement hash as erc7710 evidence** — follow-up to the #1511 decision.

## Generated Artifacts And Handoffs

- [x] No generated artifacts or handoffs changed
- [ ] Updated generated docs, `.env` examples, SDK snippets, demo scripts, or skill bundles
- [ ] Reviewed credential semantics and product language

## CASP / MiCA Guardrail Check

- [ ] Not applicable
- [x] Applicable and reviewed against `docs/regulatory/casp-
