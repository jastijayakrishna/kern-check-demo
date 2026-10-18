# fix(core): stop forcing a web search on complete plain-text Stage-1 answers (27s → 5.5s)

## Problem

Stage-1 sometimes answers in **plain prose** instead of the structured field envelope. That path (`synthesizeSimpleReplyFromPlainText`) runs through `applyDirectCurrentCandidateBackstopToMessageHandler`, whose inference tags almost any interrogative with `WEB_FETCH`/`WEB_SEARCH` candidates. The backstop then **unconditionally** promoted the turn to `requiresTool: true` — so a *complete* plain-text answer got forced through a pointless web search plus an extra slow planner round.

Measured live (same question, same agent):

| Stage-1 output shape | Path | Latency |
|---|---|---|
| structured JSON (`contexts:["simple"]`) | direct reply | ~5s |
| plain prose (identical answer) | forced `WEB_SEARCH` + 2 planner rounds | **~27s** |

Examples that hit it live: "my lucky number is 4291. what is my lucky number?" (answer already complete), and a solved logic riddle — both correct answers, both dragged through a web search whose results the evaluator then discarded.

## Fix

Give the plain-text backstop the **same** structural valve the structured-envelope path already uses (`shouldPreferCompleteDirectReply`): a finished answer whose only planning signals are weak/injectable ones (simple/general context + search/shell-class candidates) stays direct. Two adjustments make it exactly equivalent, not looser:

- gated by `!looksLikeCodingWorkRequest(currentMessageText)` — mirroring the structured path's `modelCommittedToDelegation` guard, because spawn-class actions are also in the weak-override set; a plain-text "build the app" reply can never be kept direct.
- `WEB_FETCH` added to `WEAK_DIRECT_REPLY_OVERRIDE_ACTIONS` (`WEB_SEARCH` was already there) — the backstop infers both, and a finished answer tagged with either is the same weak signal.

Live-info stays correct by construction: its Stage-1 reply is an ack ("Checking the price now."), which fails `looksLikeCompleteDirectReply`, so price/weather still force the fetch.

## Evidence (live, before/after)

- Before: riddle → `messageHandler → toolSearch → planner ×2 → tool → evaluation`, `REPLY + WEB_SEARCH`, 27.4s.
- After: same-shape riddle → `messageHandler` only, direct reply, **5.5s**, answer correct ("5 minutes — the printers run in parallel…").
- Live-info regression check after the fix: "what is the current price of bitcoin right now?" → `WEB_FETCH` → "$58,546 (via CoinGecko)" — still fetches.

## Tests

4 new regression tests in `message-routing-live-regression.test.ts`: complete plain-text answer stays direct (2 shapes); live-info **ack** still forces the tool; coding-work request with a complete-looking reply still plans. Suites on this branch: `message-routing-live-regression` + `message-handler-bogus-candidates` → 59/59 green; core typecheck clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

