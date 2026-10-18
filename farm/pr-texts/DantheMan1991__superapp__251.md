# Production slice 1a: the carcass, and the honest way to subtract a condemnation

Production slice 1a — the carcass stage. Slice 1 split in two when it came to be built; 1b (processing path, eligibility stamping, the exemption counter, and the sheet as a document) is next, and the reason for the order is below.

## One honest ratio became two

Slice 0 could give one number — packaged over live — and said plainly why: telling **dressing percentage** (live → hanging) from **cutting yield** (hanging → packaged) needs the carcass recorded as a stage of its own, and those are the two ratios the design says a butcher actually argues about. `production_run_carcasses` is that stage. Both ratios are folded in `core/carcass.ts` and stored nowhere, which is the rule this pack was built on.

## Where a condemnation finally goes

Slice 0 refused to model one, and its note is what designed this: a `condemned_head` count would make the head reconcile while leaving the condemned animal's live weight in the denominator, and *nothing short of per-animal weights can take it out*. So `live_lb` sits on the carcass row and there is exactly one adjustment:

> **Sum only the animals that PASSED, on both sides of the ratio.**

The condemned animals are then in neither number. Nothing is averaged, nothing is corrected. That works only when the plant weighed the carcasses — and when it did not, the app **declines to adjust and says so**: `includesCondemned` is true, the denominator is the farm's own trailer weight with everything that left the yard in it, and the screen names the gap. A real condemnation reading as a bad kill forever is the failure that flag exists to prevent.

## Decisions

- **Two live weights are allowed to disagree, and are never summed.** The input's `weight_lb` is the trailer ticket; the carcass's `live_lb` is the plant's scale hours later, and shrink separates them by 3–5% for a real reason this profile already recorded. The fold *chooses* — the plant's when it covers every passed carcass, the farm's otherwise — and prints which. This is `land`'s declared-versus-measured acreage rule arriving somewhere with no geometry in it.
- **The overall yield's denominator did not move.** Slice 0 chose *everything that went in* so a condemnation reads as a visibly low yield rather than a normal one with a hidden correction. That survived being revisited — a softened headline is how a real loss stops being noticed. The sheet adds the explanation that was missing beside it, not a correction to it.
- **One line is one disposition.** "100 birds, 3 condemned" is two rows, which is what keeps `hanging_lb` meaning one thing. A condemned line carries no hanging weight — CHECKed in the database, refused in words by ops. A partial condemnation is deliberately not a third state: the carcass passed, and the quarter that never came off it is a byproduct that failed to materialise (slice 3).
- **The cause is OPTIONAL**, the opposite of what `inventory` decided for an adjustment's reason. The difference is who knows it: a farm adjusting its own stock knows why; a farm transcribing a plant's sheet is reading someone else's handwriting. Unstated causes are grouped and counted, never dropped, so the causes always add to the count beside them.
- **A finished run accepts a kill sheet** — the only write on this pack a complete run does not refuse. A carcass row posts nothing (no quantity, no cost, no movement) and the design says the sheet arrives days after the run from a party who is not this farm. An ops test asserts the landed cost is identical before and after.
- **`SHEET_INCOMPLETE`** catches the case that would otherwise read over 100% — all the boxes over some of the carcasses. It reconciles against head read off the input's own ledger row, through the count dimension's base, so five dozen is sixty.
- **`killSheet` is a declared, renameable label** in `src/packs/index.ts` — the one place `production` says something industry-shaped out loud. Recorded as such rather than hidden behind a euphemism.

## Why 1a came before the extraction


