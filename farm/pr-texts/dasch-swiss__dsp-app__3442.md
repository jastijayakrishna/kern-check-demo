# fix(calendar): make Gregorian toJDN/fromJDN inverses before 1582

Resolves [DEV-7264](https://linear.app/dasch/issue/DEV-7264/gregorian-tojdnfromjdn-are-not-inverses-before-15-oct-1582).

## The bug

`gregorianToJDN` branches on the calendar reform — dates before 15 Oct 1582 are encoded with the Julian rule — but `gregorianFromJDN` applied the Gregorian `alpha` correction **unconditionally**. One function encoded as Julian, the other decoded as Gregorian.

| Date | JDN | Round-tripped | Drift |
|---|---|---|---|
| `1969-07-20` | 2440423 | `1969-07-20` | OK |
| `1582-10-15` | 2299161 | `1582-10-15` | OK |
| `1582-10-04` | 2299160 | `1582-10-14` | **+10** |
| `1492-10-12` | 2266296 | `1492-10-21` | **+9** |
| `1215-06-15` | 2165002 | `1215-06-22` | **+7** |
| `-0043-03-15` | 1705426 | `-0043-03-13` | **−2** |

Neither function was wrong alone — 12 Oct 1492 Julian genuinely *is* 21 Oct 1492 Gregorian. They disagreed about which calendar the JDN meant.

## The fix

Give `fromJDN` the boundary `toJDN` already had, and name it in both places so they can't drift apart again: `GREGORIAN_START_YYYYMMDD` (date form) and `GREGORIAN_START_JDN` (JDN form).

## Verification

**Exhaustive:** 870,001 consecutive JDNs (~450 BCE → 2020 CE) round-trip with **zero failures**.

The only dates that don't survive are **5–14 October 1582** — days that never existed, since the reform skipped them. Mapping those forward is correct, and there's now an explicit test pinning that so it isn't mistaken for a regression later.

**Mutation-tested:** reverting the fix fails **7** of the new tests; restoring it returns all 292 green.

- `calendar`: 283 → **292 tests pass**
- `date-picker` 187, `resource-editor` 150 — unchanged
- Lint clean

## Two existing assertions were wrong

Corrected, not accommodated:

- **`fromJDN(1721426)`** was labelled "January 1, 1 CE" — but `toJDN(1 Jan 1 CE)` returns **1721424**. The spec's own JDN was off by two, and it passed only because `fromJDN` decoded with the wrong rule. Now uses 1721424, and the result matches `JulianCalendar` exactly.
- **`fromJDN(1721059)`** expected era `BCE` for year 0. Era follows the sign of the astronomical year per `createDate`'s documented default (`year >= 0 ? 'CE' : 'BCE'`), so year 0 is CE by that rule. The case now uses a genuinely negative year to exercise the BCE branch.

## No user-visible change today

Worth stating plainly: **no rendered code path performs a `fromJDN` after a `toJDN`.** The three production callers — `addCalendarDays`, `today()`, and `convertCalendar` — all sit on `CalendarDateAdapter`, which is globally registered but consumed only by `DateInputComponent` / `DateRangeInputComponent`, neither of which is referenced anywhere. The one real `mat-datepicker` overrides it with `CustomDateAdapter` (`NativeDateAdapter`, no JDN).

The date editor doesn't convert either — switching calendar only relabels (`app-date-picker.component.ts:473`), keeping the typed year/month/day verbatim.

So this fixes the primitive so future callers don't inherit the defect, rather than repairing live data. The corrected call-site trace is recorded on DEV-7264, which was re-scoped from High to Medium on that basis.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
