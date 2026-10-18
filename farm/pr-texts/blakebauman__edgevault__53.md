# fix(assistant): upgrade past the stream-resume path that duplicates tokens

The duplication is an **upstream bug**, not ours — and `@cloudflare/ai-chat` 0.8.6 says so in its own source, citing its issue #1733:

> The server sends `CF_AGENT_STREAM_RESUMING` for the same request from both `onConnect` and its `CF_AGENT_STREAM_RESUME_REQUEST` handler… the fallback path used to ACK both — **triggering a second full-buffer replay that duplicated streamed parts.**

That is precisely the symptom: one turn, two full copies, interleaved per token.

### Why 0.8.6 doesn't save us, and what actually changed

0.8.6 already carries the dedupe guard for #1733 and **still duplicates**, so the guard isn't sufficient. Rather than assume a newer version helps, I unpacked 0.9.4 and 0.10.1 and grepped their bundles:

| version | occurrences of `resum` (any casing) |
|---|---|
| 0.8.6 | `RESUME RESUMING Resume ResumeRef ResumeStream resumeStream resuming …` |
| **0.9.4** | **none** |
| **0.10.1** | **none** |

The entire stream-resume/replay mechanism was removed. Removing the path removes the bug — that's a mechanical reason to expect a fix, not a hopeful bump.

### The smallest step over that line

`@cloudflare/ai-chat` **0.8.6 → 0.9.4**, which keeps `ai ^6` and `@ai-sdk/react ^3.0.204` exactly as they are — no AI SDK movement at all. 0.9.4 requires `agents >=0.17.1`, so `agents` goes **0.16.2 → 0.17.4**, well short of the 0.20.1 that wedged the DOs this morning.

`AGENT_GENERATION` goes **v2 → v3** in the same change. `agents` is moving again, so instead of risking DOs holding 0.16.2-format state, we route away from them. This is exactly what that lever was added for.

### Verification

`biome ci`, `boundary`, `typecheck`, `test`, `build`, `install --frozen-lockfile` all green.

**Not verified:** whether the duplication actually stops. The reasoning is mechanical and the code path is provably absent from the new bundle, but only a rendered reply on staging settles it. If it still doubles after this, the cause is somewhere I haven't looked and I'll say so rather than trying a third version.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
