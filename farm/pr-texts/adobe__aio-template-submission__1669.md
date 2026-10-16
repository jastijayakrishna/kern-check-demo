# fix: replace axios with native fetch and update Node.js engine to ^24

## Summary
- Removes the `axios` dependency in favor of the built-in `fetch` API (available natively in Node.js 18+)
- Updates the `engines.node` requirement in `package.json` to `^24` to align with the recent Node.js 24 GitHub Actions update (#1657)

## Test plan
- [x] Verify `checkUrlAvailability` still works correctly with native `fetch`
- [x] Confirm no other usages of `axios` remain in the codebase
- [x] Run existing test suite to confirm no regressions

🤖 Generated with [Claude Code](https://claude.com/claude-code)
