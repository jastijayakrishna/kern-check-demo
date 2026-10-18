# Move the strong tier to gemini-3.7-flash

Prompted by an in-console notice that 3.5 Flash is going away.

**The notice is not a real deprecation.** Google's deprecation page lists `gemini-3.5-flash` with *"No shutdown date announced"* — it's an upgrade nudge, not a shutdown. No deadline here.

**Switching anyway, because it's cheaper:** $0.75/$3.75 per 1M in/out vs 3.5-flash's $1.50/$9.00. Half the input cost, 2.4x less output, on a project billing a real card. 3.7 is also built for agentic workflows and multi-step execution — exactly the tutor's tool loop. Promotional rate runs to 31 Dec 2026.

**Light tier unchanged.** There is no 3.7 Flash-Lite, and `flash-lite` is the second step of *both* chains in `buildModelChain`, so it must stay a model that exists.

## Risk

3.7 supports thinking levels low/medium/high, defaulting to medium — **no "minimal"**. So unlike 3.5 it may ignore the `thinkingBudget: 0` passed by tutor.js / explainer.js / simplify.js. Hidden thinking would then spend the same budget as the visible answer — the exact truncation those call sites exist to prevent.

Most exposed: `summarize` (1400 cap) and `tutor` (1200). `explainer` has 6000 and ample room.

Output budgets deliberately left alone so this moves one variable and any regression is unambiguous.

**Rollback needs no deploy:** set `GEMINI_MODEL_STRONG=gemini-3.5-flash` in Vercel and the chain reverts on the next request.

624 tests passing, lint clean, build clean.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_012AEqFkKY3HF3wn9KCHGPUe
