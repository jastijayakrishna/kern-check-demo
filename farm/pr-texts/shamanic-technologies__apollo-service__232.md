# feat(refine): a strong model with a real budget, a sample of who it matched, and its own final answer

## Why

The refine loop had a rule for every failure we had ever hit, and the scaffolding became the problem. Same request, three production runs in one day: 2,640 people (correct — 19 German-speaking cantons enumerated), 161 (capped by an invented `organization_num_employees_ranges`), 1,222 (geography collapsed to bare `Switzerland`, covering the French- and Italian-speaking regions the request excluded). Each was produced by a loop that graded itself clean, or was overridden by code picking the biggest number.

## Deleted

- The MECE vocabulary and the invariant restated every round.
- The "maximize volume among the sets that hold the invariant" objective.
- `reachesOffTarget` / `leavesTargetUnreached` — the model both issued the verdict and benefited from it.
- `pickBest()` and its max-count-among-clean rule. Code arbitrating the winner is why a set the model disowned could still win.
- `MIN_ENCODINGS_BEFORE_CONFIRM` and the premature-confirm rejection.
- The accumulated patch instructions: the 0-count handling rule, "never drop the concept", the ban on inventing firmographic constraints, the frozen-count "wrong lever" rule.

## Replaced with

The model gets the description, the filter catalog, and a plain goal. Up to **10** real dry-run attempts; malformed output runs on its own separate retry budget. **Its final set is the result** — no code re-ranks, scores or overrides it. If the budget runs out before it answers, its most recent proposal stands.

Two things kept beyond that:
1. **One closing question** — `matchesRequest`, read AFTER the set is chosen, populating the existing `degraded` flag. An omitted answer or an exhausted budget is also degraded. It selects nothing; a test asserts a `matchesRequest: false` run returns that exact set unchanged.
2. **A degraded or failed run logs its full trace** — every attempt's filters, count, sample and reasoning, in one structured `console.warn`. Nothing on the happy path.

## Sample amendment (same PR)

`dryRunCount` threw away everything except `total_entries`. A count says how many, never who — and every failure above was invisible in a count and obvious in three rows. So each attempt now returns a live count **and** ~20 people (`dryRunSample`), rendered as `company — title — city, country`.

Drawn from up to 2 **random** pages, not the head: Apollo ranks results, so page 1 is biased in the direction that hides the bug (a 1,222-match set shows clean German-Swiss bio shops on page 1 while Romandie sits on page 40). Clamped to Apollo's 500-page cap. The teaser bills zero credits at any page size, so this stays free.

The sample is what **replaces** the deleted rules rather than sitting beside them: the model sees Procter & Gamble and Rolex in a "drugstores" audience, or a sample thinning out under an invented headcount clamp, and concludes for itself. No rule about headcount was re-added.

## Model

`anthropic` / `opus`, `responseFormat: "json"` with **no** `responseSchema`. The known blocker — a strict Anthropic schema needs every property required with `additionalProperties: false`, incompatible with the sparse filter object (a few of ~18 optional filters) — applies only to the `responseSchema` path. Plain `responseFormat: "json"` needs no schema: chat-service strips fences, parses, and 502s on unparsable output, and the Zod guards validate the shape. So `opus` shipped; no fallback to `google`/`pro` was needed. Reasoning left on (`disableThinking` is a no-op on Anthropic `/complete`, so it is not sent).

## Shape

`POST /audiences/suggest-from-segment` request/response unchanged; `openapi.json` regenerates byte-identical. `degraded` stays on the response.

## Verification

- `audience-refine.ts`: **841 deletions / 451 insertions** across the PR; the loop file alone drops from 565 to 384 lines including the new sampling code.
- Full suite green: **338 passed, 3 files skipped**. `tsc --noEmit` clean.
- Tests asserting the deleted rules were removed with them, and one test assert
