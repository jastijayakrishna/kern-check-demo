# Where a decision gets recorded

Slice 3d stage 1: `inventory_tax_treatments`, the resolution, and a screen.
[ADR 0013](docs/decisions/0013-inventory-tax-treatment.md) §A.2 and §A.5.

**Nothing on this page changes a report yet, and the page says so in its first
card** rather than implying otherwise.

> **Merge order:** this branches off `main`, not off #246. If #246 lands first
> there may be a small conflict in the inventory dossier's open items — both
> touch the bullet about the cash lens. Nothing else overlaps.

## The list is moments the ledger can date, not tax treatments

This is the design, not a limitation. A list of *treatments* would be a reading
of the regulations, maintained by people not qualified to read them, and every
gap in it would be invisible to everybody. A list of *dates* is checkable:

| Rule | Where the date comes from |
| --- | --- |
| `consumed` | the `issue` movement — **the default, and today's behaviour** |
| `billed` | `bills.bill_date` |
| `paid` | `bill_payments.payment_date`, through the allocation chain |
| `sold` | the movement a `retail_sale_lines` row names |
| `later_of_*` | max of two of the above, computed, stored nowhere |

If an election needs a moment that isn't on the list, the answer is another
observable event — never rounding to the nearest one that is.

## What's settable is narrower than what's listed, and the gap is enforced

`consumed` is the only rule the lens can apply, because it's the only one that
means "change nothing". `setTaxRule` refuses the rest with a message saying the
reports can't apply it yet; the screen shows them greyed as *"not built yet"*.

Showing them is deliberate. This page exists so an accountant's answer has
somewhere to go, and hiding the answers the software can't take would let
somebody conclude it never will.

## Three decisions worth reviewing

**Per `item_kind`, which already existed.** An earlier ADR draft made this one
setting for a whole business, in the same document that says merchandise held for
resale behaves differently from feed. Resolution is item kind → tenant default →
built-in, and **both fields come from one row** — resolving them independently
would let a category say "expense at payment" while the account came from a row
that never agreed to it.

**It's a record, not a preference**, so it carries `decided_by` and `decided_on`.
Free text, for the reason `inventory_counts.counted_by` is: the accountant has no
login here. Every row is badged with where its answer came from.

**Clearing is not setting it back to `consumed`.** "Nobody has decided" and
"somebody decided it's used-based" are different facts. Collapsing them would put
an accountant's name against a decision they never made.

## Driven

The page builds its rows from the categories the tenant **actually holds** — not
the suggested list. `item_kind` is an open taxonomy, so a page built from
suggestions would silently omit anything typed by hand. On the dev farm that's
feed, livestock, meat and medicine.

Recording feed, then the business default, flipped the other three to
`inherited`. The unbuilt rules show greyed and refuse the click. The edit dialog
pre-fills and grows a Remove button; the unrecorded one doesn't.

## Verification

- `npm run test:isolation` — 25 files, **422 tests** (up from 417), green
- `tests/inventory-ops.test.ts` 54, pure tax-rule suite 11
- Cold `tsc --noEmit`, `npm run lint`, `npm run build` — green
- Migrations `0182` (table + enum) and `0183` (RLS), applied to the dev branch

## Still not built

The lens. Stage 3d iii applies a rule other than `consumed`, and it's where the
two things reading `cash-basis.ts` turned up have to be solved: an entry has
**one control leg shared across mixed lines**, so keeping a capitalising line at
its accrual date means splitting that leg pro rata; and `cashBasisAdjustment`
**only runs for documents with a payment in the window**, so a bill never paid
never gets its line back at all. Both are in the dossier's open items.

🤖 Generated with [Claud
