# Lift the whole rating scale +11 so it reads like EA FC

A big-four top flight generated **50 / 64.5 / 81** (min/mean/max) against EA FC's Premier League at roughly **62 / 76 / 91**, so your best player was a 74 and read as mediocre to anyone who has played the licensed games. It now generates **61 / 75.5 / 92**.

## This is a relabel, not a rebalance

A uniform additive shift is an affine change of units, and the game is invariant to one. Three legs, all verified rather than argued:

- **The match sim cannot see it.** Composites z-normalise within each competition, so a constant added to everyone moves the mean, leaves the sd, and leaves every z-score.
- **Both money curves are differences from a floor.** Wages are `(ovr - WAGE_OVR_FLOOR)^3`; value is `(ovr - VALUATION_OVR_FLOOR)^n + (ovr - VALUATION_ELITE_THRESHOLD)^2`. Shift those floors with the ratings and every wage and fee is identical to the pound.
- **Everything else that reads `ovr` reads a GAP** — the familiarity penalties, `SECONDARY_POSITION_CUTOFF`, `slotValue`, the country ladder's 0.94-per-offset-point, Power Rankings' Elo-per-point, the scouting fog's half-widths. I checked every shifted constant's call site: each is consumed as `(ovr - CONSTANT)`, which is *why* moving both sides changes nothing.

So the change is one constant, the constants that name a **position** on the scale (each written `<calibrated value> + OVR_SCALE_SHIFT`, keeping the original visible), and a save migration. Widths and weights deliberately do not move. **No dynasty audit is needed, and that property is the point.**

## Measured

`scripts/ovrScaleProbe.ts` fingerprints every player's ovr/potential/wage/value plus a scoreline hash; `scripts/ovrScaleMatchProbe.ts` reports the distributional half, because a hash is all-or-nothing. Setting `OVR_SCALE_SHIFT = 0` reproduces the merge base exactly, so the A/B is one edit.

| | before | after |
|---|---|---|
| English D1 mean | 64.53 | 75.48 |
| Wages differing | — | 0.72% |
| Values differing | — | 7.09% |
| goals/match | 3.1414 | 3.1372 |
| home-win rate | .4191 | .4220 |
| champion points | 78.25 | 78.75 |

Every competition moved +10.83 to +11.00.

## It is not bit-identical, and that is the rating clamps

97.78% of players shift exactly +11; the rest by +10/+9/+8/+7. Those are weak-league players whose ratings were underflowing into `RATING_MIN`, and a shift lifts them **off** it (ratings pinned at 1: **7,291 -> 1,531**), so they gain less than 11. That changes the spread a competition normalises against, which is why the `touchStats` scoreline hash is rebased. The football does not move — see the table. The un-clamping is a small improvement: it is the same youth underflow `YOUTH_BASE_FLOOR` exists to fight.

## Judgement calls

- **Applied to `rollRating`'s output, not to the generation bases.** `base` feeds the country and division ladders and `academyBase` feeds `YOUTH_BASE_FLOOR`'s softplus, a nonlinearity anchored at absolute zero — shifting the bases would move which academies saturate on it.
- **The `ABS` tier is left on its absolute floor.** Cross-referencing `GEN_OFFSETS` against `OVR_WEIGHTS`, every ABS-marked skill carries zero ovr weight at its position, so this moves no player's rating. It is also the more EA-like reading.
- **`GENERATIONAL_DAMPING_END` could not take the shift**, being 95 against a `RATING_MAX` of 99. Capped, so the rarest legend peaks in the mid-to-high 90s against a field topping out ~91 rather than ~95 against ~80. Reaches about one player every 30 seasons.
- **A shift cannot narrow the range.** The game spans 5->81 against EA's ~47->91, so the top flights land on EA and the deep tiers stay below anything EA models. Closing that needs a compression, which breaks all three invariance legs and is a genuine rebalance.

## Migration is mandatory, not cosmetic

An unlifted save fields 65-rated players against an 81-rated Division 2 ceiling (nobody is ever swept), a 91-rated protected-star bar (nobody is ever protected) and a wage floor 11 points below its own squa
