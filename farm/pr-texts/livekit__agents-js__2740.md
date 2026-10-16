# fix(inference): send keyterms to speechmatics/linden-1

## Summary
- enable session keyterms for `speechmatics/linden-1` using Speechmatics `additional_vocab`
- preserve user vocabulary metadata and avoid duplicate session terms
- correct Speechmatics option documentation for fields supported by the agent endpoint

Port of livekit/agents#7853. This depends on `livekit/agent-gateway#1592` being deployed for the gateway to forward Linden vocabulary; before that deployment the change is harmless but has no effect.

<details>
<summary>Source diff coverage</summary>

- `livekit-agents/livekit/agents/inference/stt.py`: **adapted** to `agents/src/inference/stt.ts`. Removed the TypeScript counterpart of the explicit Linden keyterm exclusion and updated the same `additional_vocab` and `transcript_filtering_config` descriptions using target naming and types.
- `tests/test_inference_stt_connection.py`: **adapted** to `agents/src/inference/stt.test.ts`, where agents-js co-locates inference STT connection tests. The ported WebSocket test verifies Linden advertises keyterm support, preserves user `sounds_like`, deduplicates `gnocchi`, and sends `LiveKit` through `session.create`.
- No source files were omitted. The target already had the required keyterm merge and WebSocket infrastructure.

</details>

## Validation
- `pnpm test agents` (188 files, 3637 passed, 5 skipped)
- `pnpm build:agents`
- `pnpm lint`
- `pnpm format:check`
- `pnpm --filter @livekit/agents typecheck`
- `pnpm --filter @livekit/agents api:check`

---

Ported from https://github.com/livekit/agents/pull/7853

<details>
<summary>Original PR description</summary>

## Summary
- `_keyterms_key_for_model` returned `None` for `speechmatics/linden-1`, so `inference.STT` reported `keyterms=False` for it and AgentSession's session keyterms never reached it. Speechmatics' Agent STT endpoint (`/v2/agent`, which serves `linden-1`) accepts `additional_vocab`, so `linden-1` now takes keyterms under that key like `speechmatics/enhanced` and `standard`.
- `SpeechmaticsOptions` no longer labels `additional_vocab` and `transcript_filtering_config` as "RT only". `/v2/agent` accepts both. A live `StartRecognition` probe on 2026-10-15 still refuses `max_delay`, `max_delay_mode`, `enable_entities`, `audio_filtering_config` and `end_of_utterance_silence_trigger`, so those keep the label.

**Merge after livekit/agent-gateway#1592 is deployed to production.** Until then the gateway drops `additional_vocab` for `linden-1` with an Info log, so this change is harmless before the deploy but does nothing either. After the deploy, a keyterm change mid-session makes the gateway reconnect upstream, the same as on the RT models. The stream already defers that to end of speech.

## Test plan
- [x] `test_linden_session_keyterms_reach_session_create`: user `additional_vocab` entries keep their `sounds_like`, and session keyterms are appended without duplicates in `session.create`. It fails on `main` (`capabilities.keyterms` is False).
- [x] `pytest tests/test_inference_stt_*.py`: 130 passed
- [x] `ruff check`, `ruff format --check`, `mypy -p livekit.agents`

🤖 Generated with [Claude Code](https://claude.com/claude-code)
</details>
