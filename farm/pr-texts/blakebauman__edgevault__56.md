# fix(assistant): stop workers-ai-provider emitting every token twice

## The bug

The assistant streamed every token doubled — `HelloHello!! I'm I'm here here to to help help…`

The cause was **not** `agents` or `@cloudflare/ai-chat`. Those two got churned repeatedly chasing this, and each churn wedged `EdgeVaultAgent` DO state (hence the AGENT_GENERATION v2→v4 ladder).

A Workers AI stream chunk carries the same token in **both** `response` and `choices[0].delta.content`:

```
{"choices":[{"delta":{"content":"ABC"}}], … "response":"ABC", …}
{"choices":[{"delta":{"content":"DE"}}],  … "response":"DE",  …}
```

`workers-ai-provider` has two independent branches that each enqueue a `text-delta` from those fields, so every token is emitted twice under the same text id. Still unguarded upstream as of `4.0.0`, so this ships as a pnpm patch: prefer the OpenAI-shaped delta, fall back to `response` when absent.

## Why it looked like a console bug

Only the **deltas** double. `text-start`/`text-end` are guarded by `if (!textId)`, so the framing arrives exactly once:

```
start          ×1
start-step     ×1
text-start     ×1
text-delta ABC ×2   ←
text-delta DE  ×2   ←
text-end       ×1
```

That asymmetry also disproves the stream-resume replay theory recorded earlier — a buffer replay would duplicate the framing too, and no frame carried `continuation: true`.

## Evidence

- Recorded the console's WebSocket frames directly (wrapped `window.WebSocket`): deltas twice, framing once, single socket, no continuation flag → duplication is server-side, in the stream, not a render bug.
- Dumped **raw** Workers AI SSE from a scratch worker over `wrangler dev --remote`: exactly one chunk per token, both fields populated → rules out Workers AI duplicating chunks, which would have made this patch useless.

## Tests

`apps/api/test/assistant-stream.test.ts` pins the real chunk shape and fails with `'ABCABCDEDE'` if the patch stops applying. It also asserts genuinely repeated tokens survive (`"very very fast"`) — a dedupe-based fix would have eaten those, which is why this fixes the emission instead.

Verified: `pnpm check`, `pnpm typecheck`, `pnpm boundary`, api build, 89/89 api tests. Confirmed the patched code is present in the bundled worker.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
