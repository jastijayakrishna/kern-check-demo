# chore: rename shipped bundle to match repo name

## Summary
- `dist/card.js` renamed to `dist/ha-yahoofinance-board-card.js` so resource URL is recognizable alongside other installed HA cards
- `hacs.json` filename and README install instructions updated

## Test plan
- [x] `npm run build` produces `dist/ha-yahoofinance-board-card.js`
- [x] `npm run test:coverage && npm run check:ci` pass

🤖 Generated with [Claude Code](https://claude.com/claude-code)
