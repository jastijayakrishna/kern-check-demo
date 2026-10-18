# fix: day-granularity fills lose realized P&L when buys outnumber sells

## Problem

The #495 same-stamp ordering processes ALL buys before ALL sells within a day-granularity run. On a day whose buys outnumber sells (completed round trips plus a position held into the close), the reconstructed position never returns to flat, so the day's realized round trips merge into a single OPEN trade at the blended average — and their realized P&L silently disappears from the Journal day.

Real case (SHOP, 2026-08-05): 73 shares bought across 9 fills, 48 sold, 25 held. The app showed one OPEN trade of 25 @ \$147.00 (exactly the 73-buy blended average) and the day totaled **-\$110** instead of ~**-\$258** reconstructable from the same fills.

## Fix

Replace buys-first ordering with FIFO quantity matching per same-stamp run:

1. Close any carried position first (oldest lots exit first — matches how broker statements attribute realized P&L).
2. Pair `min(buys, sells)` shares — opening side up to the match, whole closing side — splitting a boundary fill with fee prorated by quantity, so the completed round trip emits as a CLOSED trade.
3. Only the unmatched tail stays open (SHOP's final 25 @ 146.88, CVS's 121 @ 99.63).

Side semantics are unchanged from #495: flat starts default LONG unless the description marks a short sale (side stays editable in the Journal), and time-granular brokers are untouched.

## Tests

New `test/snaptrade-transform.test.ts` (7 tests) reconstructed from the real TOS account statement: the SHOP day, the full 2026-08-05 session (realized ≈ -\$257.45), boundary-fill splitting with prorated fees, overnight-carry FIFO close, explicit short sale, the PUSA sell-listed-first regression, and time-granular short reconstruction. Full suite: 228 passed.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
