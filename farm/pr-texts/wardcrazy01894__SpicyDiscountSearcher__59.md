# Measure the Avis and Hertz containers instead of claiming them

National's container was fixed by going and looking at the page. Hertz's and Avis's never were — and both turned out to be worse than National's.

## What was wrong

Their narrow selectors do not merely lose the document-order race to `main`. They match nothing at all:

| vendor | selector | matches on the live results page |
|---|---|---|
| hertz | `[data-testid="vehicle-list"]` | no |
| hertz | `.vehicle-list` | no |
| avis | `[data-testid="vehicle-results"]` | no |
| avis | `.car-results` | no |

Measured 2026-08-11 against a TPA round trip with a real CDP/AWD.

## What they are now

A measured bare `main`, for both:

- **Hertz** — 4.3k of a 50.3k-character body, holding 70 of the page's 71 price nodes. The one it excludes is the marketing line "Like-new cars for under $20,000".
- **Avis** — 4.7k, holding all 50 vehicle prices, every cheapest one a genuine rate.

The dead selectors are deleted rather than reordered. A selector that matches nothing is not a preference; it is a false claim about the page, and it is what made these entries look checked for as long as they did.

Nothing narrower is available. Hertz styles with emotion, so its cards carry generated class names and per-card numeric ids (`#1_5`), and no element inside `main` with a stable handle holds more than four prices. Avis does have a tighter `[data-testid="aem-container"]` (3.3k, same 50 prices), deliberately unused: that is Adobe Experience Manager's generic wrapper rather than a vehicle list, so it can point at a marketing box on some other page.

## One number that was never an offer

Hertz renders `Price range$42-$90` above its cards. The lower bound is derived from the results, so it sits at or below every real rate on the page — **$42 against a cheapest genuine $54/day**.

`isRangeLine` suppresses it. Same shape as `isFeeLine` (lead phrase, then ask what is left, so "Rate range $89/day" survives as a real rate), and the same inheritance — which this needs more, because the words and the amount are always in different elements: `Price range<span>$42-$90</span>`. Suppressing only the label would leave the `$42` leaf emitting.

**It changes no answer today, and the tests are written around that.** Hertz also prints "$226 est. total" per card, `total` outranks `unknown` in `BASIS_PREFERENCE`, and the bare `$42` classifies `unknown` — so the only thing between that filter bound and the headline price is one wording on one vendor's card. The case worth pinning is therefore the one with the totals removed, where `$42` becomes the page's price. Checked to fail:

- guard stubbed out → `expected 42 to be 54` (no-totals case) **and** `expected [42, 90, 54, 57, 226] to not include 42`
- inheritance narrowed back to `fee-line` only → the second still fails

The today-shaped test alone passes with the guard deleted, which is why both are there.

## Also worth knowing

Scoping Avis matters more than its ratio suggests. It is a Next.js app, so `document.body.textContent` runs to 464k characters of mostly inline RSC flight payload, dense with `$` sigils — and body is exactly what `extract` falls back to when no container matches. The 80-character cap in `priceSites` is what keeps that out today, since the payload is one huge script node.

`npm run typecheck`, `eslint`, `prettier --check` and the full suite (520) are green.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

