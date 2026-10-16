# fix: prevent publisherId from becoming "undefined" string

## Summary

After PR #245 was merged, this PR contains only the remaining fixes:

- **Fix `publisherId` becoming `"undefined"` string** in `components/nodes/NodeDetails.tsx` — when `publisherId` is undefined (e.g. accessing `/nodes/[nodeId]` directly), `String(undefined)` produced the literal string `"undefined"`. Now uses conditional logic instead.
- **Guard `NodeEditModal` render** on `publisherId` being defined
- **CI: run Next.js CI on all PRs** — remove branch filter so CI runs on PRs targeting any branch

The other fixes from the original PR (script injection, typo, unused vars) were already included in PR #245.
