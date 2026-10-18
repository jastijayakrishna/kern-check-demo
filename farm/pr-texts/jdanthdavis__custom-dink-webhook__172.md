# Format TCG recap deltas with thousands separators

## Summary

`buildTcgWeeklyChangeSection` was rendering raw numbers (`3948949`) instead of matching the rest of `tcgHandler.js`'s existing `toLocaleString('en-US')` convention used everywhere else in this file. Caught by reviewing the actual production Discord output.

## Test plan

- [x] `npm test` — new test asserts comma formatting on a large delta; existing tests unaffected (only values ≥1000 change output)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
