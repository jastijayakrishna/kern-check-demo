# Count the vendor chip the way the run counts it

Reported from a loaded extension:

> National has 5 codes that have been refused so won't be raced. So it is doing
> 14, though the check box next to National still says 19.

## The bug

The same disagreement as before — the chip promising what the run will not do —
arriving by a new door. `countCodesFor` was taught to match `buildCandidates`,
then the plan learned to skip refused codes and the count did not.

Refusals now live **inside** `countCodesFor` rather than being a subtraction each
caller has to remember, which is the lesson `codeReaches` records one function
above: when a counting rule lives in more than one place, the places drift.

## Why the chip is not just a smaller number

A bare "14" is its own confusion — a vendor you know has nineteen codes quietly
showing fourteen. So the chip shows what will race, and carries the difference in
its title:

> 19 codes, 5 refused by the vendor and no longer raced

The number that changes is the one the plan agrees with; the number that would
otherwise vanish is still there to find, and the standing note under the form
remains the clickable way to put them all back.

## Also

- The **company list** uses the same rule, and had to. Filtering the matches
  without filtering the labels is exactly how a company came to render with a
  blank vendor list once already.
- Chips and the company list are **re-rendered when the refusal set changes** —
  on clear, and when a run finishes. `refreshPlan` alone left them showing the
  reduced counts after the codes had been put back.

## Verification

495 tests. Two new ones pin the chip against the plan's own count and the
restore-on-clear path; both fail if the fix is reverted. Lint, typecheck,
prettier, build and `check-dist` clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
