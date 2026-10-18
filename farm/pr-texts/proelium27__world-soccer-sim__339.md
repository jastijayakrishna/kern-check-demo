# Promotion playoffs at every step of the pyramid

The promotion playoff was seated at the top link only. That was a deliberate call when it shipped, back when a country having a third division was itself new — but it means starting at the bottom is grinding out an automatic place with nothing else on offer, while the same club one tier up has a bracket to fall back on. England and Germany both hold real playoffs further down. `promotionPlayoffFields` now walks `promotionLinks` instead of a country's first two divisions, so the world plays **22 of these a season against 11**.

## The sim needed almost nothing

`computeCountrySwaps` and `playoffOutcomes` were already keyed by the link's **lower** competition, so each link looks up its own outcome independently, and every tie already drew its stream off `(lid, season, d2CompId, round, tie)` — distinct per link by construction. `seatField` is the old per-link body extracted; `PromotionPlayoff.tiers` widened `(1|2)[]` → `number[]` and now carries real `Competition.tier`s, so a D3-D2 German tie reads `[2, 3]`.

`d1CompId`/`d2CompId` keep their names and now mean upper/lower. They are persisted on every save's `seasonHistory`, and this is the same call `DIVISION_2_OFFSET` and `DIVISION_2_BUDGET_SCALE` already make about generalising past the tier they were named for. **No new field, no migration.**

## The one genuinely new hazard

A middle division is now spoken for at both ends at once. `swapLimitOf` already keeps its automatic slices apart, but a playoff reaches three clubs further into the table than the automatic places do — so in a tightly packed pyramid the same club can be an English entrant for promotion *and* sit in the slice being relegated below, and `applyCompetitionSwaps` would move him twice and silently keep whichever it wrote last.

**A playoff yields to a swap:** a field holding a club that any *other* link's plain automatic slice already moves is not seated at all, and that link settles its place on the table alone. The direction is forced rather than chosen — the automatic swap is not optional and the playoff is. Unreachable in the shipped world (the tightest country needs 6 clubs of a 12-club second tier); a test pins the hand-built case at `MIN_DIVISION_TEAMS` 8 against `MAX_PROMOTION_SPOTS` 6.

## Verification

- `worldIntegration` green: every division still exactly its own size after an offseason with 22 playoffs, and every playoff winner ends in the right division.
- `promotionPlayoffProbe`, 6 seasons / 132 finals, all checks pass: promoted == relegated at every link every season, and the headless replay reproduces what `simThrough` settled. Seed-win split is **38.3 / 23.3 / 21.7 / 16.7%** playing for a tier-1 place against **43.3 / 20.0 / 16.7 / 20.0%** for a tier-2 place, so the deeper bracket is the same kind of lottery as the top one. The probe reports that split per link tier now, for exactly that question.
- 25 playoff unit tests, typecheck and production build clean.

## Dynasty audit, both sides

`weakLeaguesAudit` at 20 seasons × 4 seeds, run against the merge base with the same script. **Every seed reads `ladder OK` on both sides, and every rung passes on the pooled four-seed mean.** Block spreads BIG4→Serbia **+9.42** (gate ≥4) and France→Serbia **+5.08** (gate ≥1).

**Solvency is a wash and both sides are red — the merge base already fails on 3 of 4 seeds.** The treatment is in deficit on one more seed (4/4) but with a smaller total shortfall (−£11.2M vs −£15.7M) and a much smaller worst case (−£6.8M vs −£11.4M). That is the pre-existing weak-league wage ratchet being re-rolled by a change that moves which club is promoted, not a new failure.

Per-seed `BROKEN` lines in the logs are the documented misuse of a mean gate on a single draw and all vanish pooled; the baseline has its own. Details and the numbers are in CLAUDE.md.

Manual, changelog and CLAUDE.md updated.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01A6fMUPXF8MqXNwEYvdjTbw
