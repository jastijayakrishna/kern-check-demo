# feat(refine): degrade to the best attempt instead of returning nothing, on deepseek-pro

## Why

human-service is moving `/orgs/audiences/suggest` to request exactly ONE audience instead of a set. This refine loop stops being one of six parallel builds and becomes the only thing standing between a user and their audience, so its output quality and its worst case both matter more than they did this morning.

## 1. Never return nothing — degrade to the best attempt

`pickBest()` returned null when no iteration was judged MECE, and `refineAudience` threw. With one audience per request that is an error screen where the customer's audience should be.

`pickFallback()` now takes the highest count among every set that validated and matched at least one person, the result carries `degraded: true`, and `POST /audiences/suggest-from-segment` returns that flag. An audience the customer can look at and reject beats an empty screen; "the model was not satisfied with any set" is a quality signal, not an error.

Fail loud still applies to real errors — chat-service unreachable, Apollo unreachable, missing config, and a filter set that matches nobody (`count > 0` gates the fallback too) all still throw.

## 2. Log the refine trace on failure

`audience-refine.ts` had zero `console.` statements and discarded the trace when it threw. When #225 started rejecting every filter set in production, there was no way to tell an over-strict judgement from a broken call — the failure was unfalsifiable in place and the only option was a revert.

`logRefineTrace` now emits ONE structured `console.warn` whenever the loop ends without a cleanly-judged set, degraded path included: per iteration, the filters, count, action, both verdict flags with their reasons, validation errors and revisions. Nothing on the happy path.

## 3. The model — A/B: `deepseek-pro` vs `glm-pro`

Ran the real loop (real chat-service, real free Apollo dry-runs) end to end from inside `distribute-apollo-service-1`, same three segment descriptions, one build per provider, nothing else different.

| | `deepseek`/`deepseek-pro` | `zai`/`glm-pro` |
|---|---|---|
| Swiss drugstores + health-food (excl. pharmacies) | clean, **124** — German titles (Geschäftsführer, Einkäufer, Filialleiter) + German sector tags (Drogerie, Bioladen, Reformhaus, Naturkost) + `q_not_organization_keyword_tags: [pharmacy, Apotheke]` + `person_not_titles: [Apotheker]` | **DEGRADED**, 5,861 — its own note on the winning set: *"the 'retail' keyword tag was far too broad — it alone likely accounts for most of the 5861"* |
| Chiropractic/wellness clinics US, 11–50 | clean, **21,373** — titles + `11,50` + chiropractic/wellness/clinic tags | clean, **207,497** — dropped to generic leadership titles (CEO, President, Principal) and graded it MECE; this is the #224 leniency shape at 10x the volume |
| HR heads Singapore mid-market | clean, **603** | **DEGRADED**, 3,841 — confirmed a set it had just flagged `leavesTargetUnreached: true` |
| Wall clock (3 segments) | 31s / 23s / 23s | 70s / 35s / 63s |
| Clean runs | **3 / 3** | 1 / 3 |

`glm-pro` failed in exactly the way #225 failed: it kept a verdict flag true on the very set it then confirmed, so nothing was selectable. Under the old contract those two segments would have thrown; under this PR they degrade, which is the change doing its job in the wild. `deepseek-pro` graded honestly, explored genuinely different encodings (industry enum vs keyword tags vs department taxonomy) and produced the tighter, more faithful sets.

Winner: `deepseek`/`deepseek-pro`, thinking ON — `disableThinking` is gone. Judgement quality is the whole point of the upgrade, and thinking-off on the previous model (`google`/`flash`) is a documented contributor to the leniency in #224.

## Not in this PR

The independent grader from #225 is NOT re-landed; it stays deferred in #224. No count floor, target band or minimum-size heuristic. No request-shape change; `degraded` is additive and no existing response field moved.

## Tests

38 files / 341 passed, 3 + 32 skipped. New coverage: the
