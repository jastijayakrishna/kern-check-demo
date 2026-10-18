# fix(voice): end the call on an exceeded token cap even when a classifier consumed the event (#1204)

## Defect

`recordCompletionUsage` (sentiment classifier and vulnerability grader) records classifier spend on the session's `SessionCostTracker` and discards the events `recordUsage` returns. The tracker emits `cost_cap_exceeded` once per dimension. The call-ending decision (`recordCost` in `create-voice-turn-processor.ts`, which Gather reaches at `twilio-adapter.ts` ~2398/~2497 and Media Streams reaches through `speechTurn`) only acted when the turn's own `recordUsage` returned that event. So when a classifier took the call across the cap between turns, for example 1,450 of 1,500 output tokens plus a 60-token grade, it consumed the event. No later turn ended the call, and it ran on until the 40¢ cost cap or the 15-minute duration cap.

## Fix

`recordCost` now makes a level-triggered decision:

- It records the turn's usage and emits `cost_incurred` as before.
- It then reads the tracker's existing read-only `isExceeded` getter. That getter stays true until `reset()`, and the same `recordUsage` call that emits the event also sets it.
- If the tracker is over any cap and this session hasn't been ended for it yet, `recordCost` marks the session, emits `session_terminated(cap_exceeded)` and returns `true`. The caller then dispatches `cost_cap_exceeded` exactly as it does today, so the wrap-up line, `notify_oncall`, the audit row and the TwiML/side effects are the same.
- The "already ended" marker is a `WeakSet<VoiceSession>` in the processor closure, following the `sessionTimezones` pattern. Gather and Media Streams share the one processor on `TwilioGatherAdapter`, so a call can never be ended twice, on either transport or across both.
- The event path is kept. When a turn's own usage crosses the cap, the call still ends on that turn with the same `session_terminated` event.
- No change to cap values, cost math, pricing, or how classifier tokens are counted.

Files: `packages/api/src/ai/voice-turn/create-voice-turn-processor.ts` (logic) and `packages/api/src/ai/skills/session-cost-tracker.ts` (a doc comment on `isExceeded`, no code change).

## ASSUMPTIONS / decisions (easy to flip)

1. **No new tracker method.** `SessionCostTracker.isExceeded` already is the read-only, sticky level, so I didn't add a second one.
2. **The level is read at the same places the event path checks today:** the LLM-backed branches that call `recordCost` (classify, intent confirm, post-quote strict confirm). It is not read at the very top of every turn. A turn handled by another branch (ask_caller, disambiguation, approval dialogues, and so on) doesn't end the call on the cap, which matches the event path on main. As a result, the turn that ends the call makes one more classify/confirm LLM call, a few output tokens, before ending. A top-of-turn check would save that call, but it would touch both transports' turn functions and the ordering around the safety scan. I kept it out of this PR.
3. **The SMS consent-capture turn now only records usage.** It uses a new `recordTurnUsage`, which is `recordCost` without the decision. That site always ignored `recordCost`'s return: the consent answer must still be recorded or declined. With a one-end-per-session guard, calling the deciding `recordCost` there would take the end and the call would never end, which is this bug again. Now the next turn ends the call. There is a side effect when that turn's own confirm crosses the cap: `session_terminated(cap_exceeded)` is no longer emitted on the consent turn, where the call didn't end. It is emitted on the turn that actually ends it. Pinned by a test.
4. **A turn whose LLM result has no `tokenUsage` still reads the level.** On main, `recordCost(session, undefined)` returned `false` without looking. Now it returns `true` if the tracker is already over a cap and the session wasn't ended yet. Under the cap it is still `false`, and the existing test still passes.

## Question for Josh

**Should classifier tokens count against the per-session caps?** The caps are sized f
