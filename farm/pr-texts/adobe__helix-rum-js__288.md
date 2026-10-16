# Fix micro.js global variable scope conflicts

## Summary
- Fix micro.js variables leaking into global scope and potentially conflicting with other scripts
- Add test case to verify the fix prevents global variable conflicts
- Wrap micro.js in IIFE to isolate variables within function scope

## Background
Discussion on Slack: https://cq-dev.slack.com/archives/C07198KKQ07/p1752734381472169?thread_ts=1752729369.989249&cid=C07198KKQ07

The micro.js loader was declaring variables (`c`, `d`, `q`, `v`, `w`, `r`, `n`, `a`) in the global scope, which could conflict with other scripts on the page that use the same variable names.

## Changes
1. **Test case**: Added `global-conflict.test.html` that demonstrates the issue by pre-declaring conflicting global variables
2. **Fix**: Wrapped micro.js code in an IIFE `(function() { ... })()` to isolate variables within the function scope
3. **Verification**: All tests pass, including the new conflict test

## Test plan
- [x] Created failing test case that demonstrates global variable conflicts
- [x] Implemented IIFE wrapper to isolate variables
- [x] Verified all existing tests still pass
- [x] Verified new global conflict test passes
- [x] Confirmed RUM functionality still works correctly

🤖 Generated with [Claude Code](https://claude.ai/code)
