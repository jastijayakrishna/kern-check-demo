# fix(delivery): the warehouse works weekends, so Saturday gets its own file

#39 rolled a weekend dispatch forward to Monday, assuming no End-of-Day export comes off the warehouse on a Saturday. It does. The client confirmed the same day: they run seven days.

## What changes

| Order placed | Was | Now |
|---|---|---|
| Friday 14:00 | Monday 18:00 file | **Saturday** 18:00 file |
| Saturday 09:00 | Monday 18:00 file | **Saturday** 18:00 file |
| Sunday 20:00 | Monday 18:00 file | Monday 18:00 file (unchanged) |
| Friday 09:00 | Friday 18:00 file | Friday 18:00 file (unchanged) |

Three days late flagging a genuinely missing parcel is three days nobody was chasing it.

## Why the tests did not catch it

All six rows the client tabled are Wednesday to Friday, so every one passed either way. The weekend tests were written from my own reasoning about warehouses rather than from anything he said, which is exactly how an assumption gets locked in by a green suite. Asking would have cost one line.

## One thing kept apart on purpose

This is **not** the rule `deadlineFor` uses, and the two should not be made to agree. The delivery promise counts business days because a carrier does not deliver on a Sunday. The warehouse does work one. Two different questions, correctly answered differently, and now said so in the code so the next person does not "fix" one to match the other.

## Gates

Full suite **229 files, 2485 tests, 0 failures**; tsc clean; eslint clean; `next build` succeeds; both browser tests re-run and pass, since this changes the rule the whole feature turns on.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
