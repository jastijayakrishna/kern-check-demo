# feat(delivery): show the time an order came in, on the shop's own clock

The Ordered column gave the date alone, and the date alone cannot answer the question this page now turns on. The warehouse cutoff is **noon**, so whether an order goes in tonight's file or tomorrow's depends entirely on a number that was not on screen.

So the time sits beside the date, smaller and grey:

```
19 Aug 2026 (12:52)
```

## Local, not UTC

Two orders minutes apart either side of noon belong in different files, and an order placed 23:30 in Oslo is 21:30Z the same day. Print the wrong one and the row contradicts both the cutoff rule and its own Waiting figure.

There is a test asserting the payload does **not** carry the UTC time.

## The field

`placedOn` becomes `placedAtLocal` and carries the full wall clock rather than a bare day, so the name says what it holds. Still fixed-width, so lexical comparison is still chronological comparison, and the Ordered sort now separates two orders from the same day instead of calling them equal.

## One test-quality fix along the way

The route test now pins its fixture shop to `Europe/Oslo`. Every date assertion in that file was previously reading whatever the workspace `Setting` row happened to hold, which is not something a test should depend on.

## Gates

Full suite **229 files, 2488 tests, 0 failures**; tsc clean; eslint clean; `next build` succeeds; both browser tests pass.

Note on provenance: the checkout moved onto another agent's branch mid-task (the fifteen-minute-sync hazard), so this was committed there and cherry-picked onto a branch from `origin/main`. The commit carries only these four files; their in-flight design doc is untouched and not in this PR.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
