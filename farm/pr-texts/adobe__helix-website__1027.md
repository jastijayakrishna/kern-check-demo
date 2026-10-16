# fix(oversight): bump rum-distiller to 1.22.1 and format error estimates

## Summary
- Bump @adobe/rum-distiller from 1.20.8 to 1.22.1
- Apply `toLocaleString()` to the ± error estimate tooltip display so large numbers have proper thousand separators (e.g., "1,234,567 ±12,345" instead of "1234567 ±12345")

## Test plan
- [ ] Verify the RUM explorer loads correctly at the preview URL
- [ ] Hover over numbers with large values to confirm the tooltip shows formatted numbers with thousand separators

Preview: https://claude-1--helix-website--adobe.aem.page/tools/oversight/explorer.html

🤖 Generated with [Claude Code](https://claude.com/claude-code)
