# feat(refine): an independent grader judges MECE fit, blind to the count

Fixes #224.

## What changed

The refine loop had one model both **propose** a filter set and **grade** whether it was MECE with the described target, while `pickBest` picked the highest count among the sets it flagged clean. The only thing protecting fidelity was a boolean the beneficiary emitted about its own proposal.

- **The judgement is now an independent `chatComplete` call per iteration.** It receives `{name, description, filters, matched-company sample}` and returns the two booleans plus reasons, which land on the trace row exactly where the self-grade used to. Verdict only: no reply channel to the proposer, no memory of prior verdicts, no loop until agreement. It adds calls per iteration, never iterations — `MAX_REAL_ATTEMPTS` (6) and `MAX_INVALID_RETRIES` (3) are unchanged.
- **The grader never sees the count.** Off-target is judged from the company sample, leaves-unreached from filter semantics. `maximize volume` stays in the proposer's prompt and in `pickBest`, where it is legitimately free.
- **The grader's rejection reason is threaded into the next proposer message**, with the companies it saw. Context, not negotiation.
- **The dry-run pulls 10 people instead of 1** so the grader has real company names. Zero Apollo credits either way. `POST /audiences/{id}/dry-run` (count only) stays on `per_page=1`.
- **Both roles run on `provider: "zai"` / `model: "glm-flash"` / `disableThinking: true`.** The grader's fixed shape is enforced server-side via `responseSchema`; the sparse filter object the proposer emits stays on plain JSON mode plus the Zod guard.
- **`revisions` is deleted** from the decision schema, `RefineIteration` and `applyRevisions`.
- No fallback anywhere: an unparsable verdict throws, like every other chat-service call in this file.

## Behaviour change, on purpose

`pickBest` still returns null when nothing is graded MECE, and `refineAudience` still throws. That path was nearly dead under a self-grader; with an honest grader it will fire, and a bad segment will vanish from human-service's `Promise.allSettled` batch instead of producing a false audience. No fallback was added to keep segments alive.

## Verification

Full suite green (343 passed, 32 skipped). New/updated tests cover each AC:

- the verdict on a row comes from a call that did not author it (a self-graded-clean set at 20x the volume is still excluded)
- the grader's input contains no count
- the rejection reason and the matched companies appear in the next proposer message
- `revisions` sent by a proposer is inert, and the word appears in neither prompt
- the Swiss drugstore replay fails loud rather than confirming a `Switzerland` + retail set
- the Zurich bio-shop replay picks the 19-count set carrying the sector tags and the pharmacy exclusion over the 137-count one
- a grader verdict that does not parse fails loud

No request/response shape change on `POST /audiences/suggest-from-segment`, no migration. `CLAUDE.md`'s refine-loop section is rewritten in the same commit.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

