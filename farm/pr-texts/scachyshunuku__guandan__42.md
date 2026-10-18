# Stretch history panel to match game table height

## Summary
- The game History panel was capped at `max-h-64` and sized only to its own content, so it looked short next to the taller game table area.
- Removed `lg:items-start` on the grid so the history `aside` stretches to match `main`'s height, and made the history list scroll within that space instead of self-capping.

## Test plan
- [ ] Visually confirm the History panel now extends to the bottom of the game table in a real game (not tested in this session — no dev server run).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
