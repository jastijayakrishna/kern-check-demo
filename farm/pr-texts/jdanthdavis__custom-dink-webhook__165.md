# Add milestone messages for foil and unique card pull intervals

## Summary
- Foil pulls that land on a multiple of 50 owned now get a distinct milestone message: "has pulled their Nth foil by pulling a ..."
- Non-foil pulls that land on a multiple of 250 owned now get a parallel milestone message: "has pulled their Nth card by pulling a ..."
- Both fall back to the existing pull messages when not on an interval.

## Details
- Added `extractFoilOwnedCount` and `extractUniqueCardOwnedCount` to pull the raw owned counts (rather than the pre-formatted display strings) out of the raw content, so they can be checked with `% interval === 0`.
- `isFoilMilestone` requires `foil` to be true; `isCardMilestone` requires `foil` to be false (and, per existing gating, non-foil pulls already only reach this code for accepted rarities).
- `statsLine` is unchanged.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
