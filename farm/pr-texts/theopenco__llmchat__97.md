# fix(api,widget): stop the holding ack once a human replies + anchor it in chronological order

Two complementary fixes to the post-escalation holding message (bug 3), both visible in the real escalation flow.

## Problem 2 (priority) — the ack fired even while a human was actively replying

The guard only checked `escalatedAt && !archivedAt`, so the "our support team will follow up" ack was re-served (every ~5 min) for every escalated visitor message — even after an operator had joined and was responding. Contradictory.

**Fix** (`chat.ts`): inside the guard, probe for an `admin`-role message in the conversation. If one exists → `holdingStreamResponse(null)` (fully silent — no ack, no model call; the visitor sees the operator's real replies via polling). Otherwise → the throttled ack (the waiting gap).
- **Bot stays muted in BOTH branches** — neither calls `streamChat`, so the free-muted-turn property holds (no assistant row / usageEvent / meter).
- **Throttle is lazy** — `shouldSendHolding` is only evaluated in the no-admin branch, so the admin-replied path never dirties the STATE cooldown.
- The probe is scoped to **this conversation AND role `admin`** (operator replies; visitor/inbound replies are role `user`, so they never trip suppression).

## Problem 1 — the ack rendered out of order (floated to the bottom)

The ack is streamed but never persisted (no sequence), so `mergeMessages` tail-dumped it below later admin replies / visitor turns.

**Fix** (`messages-sync.ts`): anchor the holding row to the server slot of the visitor message it acknowledges, so it renders in chronological order. **Only the holding row is anchored** — the normal in-flight pair (just-sent user + streaming reply) still tails; handles N holdings; no duplication (a holding can never both anchor and tail, and never matches a server row).

## Constant sharing
`ESCALATED_HOLDING_MESSAGE` moved to `@llmchat/shared` via a **narrow `./holding` subpath** (not the barrel — keeps the lean widget IIFE free of the models snapshot + its import-time validation; verified the built bundle excludes it, size unchanged at 900 kB). `apps/api/src/lib/holding.ts` re-exports it, so `chat.test.ts`'s import + its deliberate non-mock of that module are unchanged.

## Verification
- **shared 38 / api 446 / widget 98** pass. New tests: admin→silent (no ack, no model, throttle untouched), gap→ack+throttle-consulted, probe-scoping (no cross-conversation/wrong-role leak), anchoring (correct slot above a later admin reply, no float, N holdings, in-flight still tails, transient pre-poll, non-rateable).
- Adversarial review (correctness×2 + integration/scope) → **ship**, zero blocking; I closed the one worthwhile note (the predicate-scope test) and softened a comment.
- Preserves the bug-3 mute guarantee, the free-muted-turn property, and Decision-B (`/v1/resolve` sets `archivedAt` → the guard short-circuits; no interaction). Does not touch escalation-email, resolve, bug-1/2, or the reopen-latch.

## Notes
- Within-session ordering only — a full reload drops the unpersisted ack (by design).
- `pnpm-lock.yaml` carries the widget→shared workspace link plus benign optional-peer (`@babel/core`) re-resolution churn.

Deploy: widget + shared change — if the preview's `kind: nextjs` builder flakes "No executable pnpm found", known transient, re-trigger once.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
