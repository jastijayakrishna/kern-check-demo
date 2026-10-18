# Reframe README + demo around AI-native, all-in-one positioning

## Why

The README opened with "a modern, high-performance feed reader" and the site tagline was literally "A modern feed reader" — generic phrasing that says nothing about what's actually distinctive. This reframes the public-facing copy around the real differentiators.

## Positioning

Lead with three pillars (in this order):
1. **AI-native, not AI-bolted-on** — MCP tool surface for AI assistants, on-demand Claude summaries, TTS narration with synced highlighting
2. **Everything in one place** — feeds + email newsletters + read-later, with unusually wide save support (extensions, bookmarklet, Discord bot, PWA share, MCP/API, file uploads; enhanced extraction for arXiv/GitHub/Google Docs/LessWrong)
3. **Obsessively fast** — real-time updates patched directly into the list (no refetch/jank), zero-round-trip client navigation, backend tuned for sub-100ms loads on cheap cloud hosts

Plus: all the standard features done well, and free/open-source/self-hostable.

## Changes

- **README**: new intro + "What makes it different" section; feature list cleaned up and reordered.
- **Demo `welcome.ts`**: rewritten around the same pillars (kept specific perf numbers out of the welcome copy).
- **New demo article `Obsessive Performance`** (Reading Experience section): documents direct SSE cache patching, `staleTime: Infinity`, client-side routing, optimistic updates, single-index timeline queries, persisted sanitized content, and feed dedup. Every claim was verified against the code by an Opus subagent (all 8 accurate); the summary was generated with the real production summarization prompt.
- **Site taglines** (`app/layout.tsx`, `demo/layout.tsx`) replaced.
- **Stale content**: dropped "ML-powered scoring" references (feature removed in #953) from demo tag/subscription descriptions.

## Notes

- **JSON Feed**: confirmed still fully supported (wired into `streaming/parser.ts`), so the demo JSON Feed page stays.
- Not touched in this pass (flagged for follow-up): `mcp-server.ts` still lists a removed `set_entry_score` tool and describes MCP as stdio/local-only (it now supports remote OAuth); `real-time.ts` describes "cache invalidations" where the actual invariant is direct patching; `open-source.ts` still lists "TF-IDF + Ridge Regression for article scoring."

`pnpm typecheck` passes; prettier/eslint clean via pre-commit.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
