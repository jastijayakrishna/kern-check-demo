# fix: hero ranking bar text no longer matches the bars

## Summary
- In the hero router cards, the band-tone `RankingBar` labels/amounts/track drew from `--primary-foreground`, remapped by `register-ink` to the register colour — text matched the bars
- The rankings column now re-points `--primary-foreground` to the neutral `--foreground` in light (labels dark grey, amounts at /75, track a grey tint); the bar fills stay register-coloured (`chart-2`)
- Dark restates `register-ink`'s own value (`--background`), so the dark scheme is unchanged

## Test plan
- [x] 66 hero tests pass
- [x] tsc clean, Prettier clean

🤖 Generated with [Claude Code](https://claude.com/claude-code)
