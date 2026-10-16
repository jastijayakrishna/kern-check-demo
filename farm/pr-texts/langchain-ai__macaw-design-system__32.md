# feat: add component parity fixes

## Problem

LineChart cannot annotate events, badges cannot display a muted suffix, and secondary buttons and Engine marks use outdated presentation.

## Solution

- Add labeled vertical event markers to LineChart, with band-scale alignment, plot clipping, and correctly measured labels that flip away from the right edge.
- Add an accessible muted suffix to Badge.
- Use the subtle border consistently for secondary buttons in dark mode.
- Correct the orientation of the Engine logo and badge marks.
- Document the new options in Storybook and add an Unreleased CHANGELOG entry.

## Test Plan

- [x] LineChart and Badge component tests pass (54 tests).
- [ ] Review the new LineChart marker, Badge suffix, and Logo stories in Storybook.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
