# feat(cloud): STT verbose_json word/segment timestamps in /v1/voice/stt DTO (#14806)

Second slice of #14806 (transcript time anchors): the cloud STT route now returns word/segment timestamps so cloud-transcribed audio can feed the transcript-fragment anchor pipeline (PR #15836) and the PII audio-redaction span math (#14807).

## What changed

- `packages/cloud/api/v1/voice/stt/route.ts` (whisper lane): sends `response_format=verbose_json` + `timestamp_granularities[]=word` + `timestamp_granularities[]=segment` (OpenAI-spec fields), and returns `segments[]` / `words[]` as `{text, startMs, endMs}` next to `transcript`. A server that ignores the fields still returns `text` — the existing DTO contract is unchanged (keys are simply absent).
- Whisper 200-boundary hardening (J3): a 200 whose body is unparseable JSON, a non-object, or missing the required `text` string is translated to a structured 502 — never a healthy-empty transcript.
- New pure parser `whisper-timestamps.ts` (unit-testable without the route's billing/service graph, same pattern as `whisper-model.ts`): seconds→ms conversion, strict per-entry validation (non-empty text, finite non-negative start/end, `end >= start`), malformed entries **dropped and logged, never coerced**; all-malformed or missing arrays yield **absent** DTO keys, never fabricated zeros/empties.
- `route.test.ts` (renamed from `route.whisper.test.ts` — it now covers the whole route): drives the REAL Hono handler end to end with only auth/billing/provider modules mocked at the module boundary. Covers the shared upload-validation gates (non-multipart, missing file, 25MB cap, declared-MIME allowlist, magic-number gate, spoofed-extension rejection), auth-failure mapping, the free whisper lane (timestamps DTO + the malformed-200 matrix), and the billed ElevenLabs lane (billing/reservation wiring, 402 insufficient credits, 429/402/503/500 error mapping with reservation refunds). A final describe, gated on `ELIZA_VOICE_LIVE_RAILWAY=1`, runs the same real route against the deployed Railway faster-whisper with real Kokoro-synthesized speech.
- TS under the cloud-api workers-types tsconfig: the test's `instanceof File` narrowing (TS2358 on the workers-types `FormDataEntryValue`) is replaced with a structural `isFilePart` guard, and bare `res.json()` expect sites are pinned to `unknown` via a `readJson` helper — no `any` casts, no ts-ignore.
- ElevenLabs SDK surface untouched (scribe timestamps are a follow-up if wanted).

## Review-blocker resolution

- Rebased onto current `origin/develop` (was ~100 commits behind); clean replay, no conflicts.
- The 6 typecheck errors in the route test are fixed structurally (see above); `bun run --cwd packages/cloud/api typecheck` exits 0.
- Changed-file coverage: `route.ts` **90.70%**, `whisper-timestamps.ts` **100%** (gate threshold 50%; replicated with the exact coverage-gate.yml command + awk — see gates.log below).

## Evidence

<!-- evidence-row:before-screenshots -->
- Before screenshots: N/A - backend-only additive DTO fields in `packages/cloud/api`; no rendered UI surface in this diff.
<!-- evidence-row:after-screenshots -->
- After screenshots: N/A - backend-only additive DTO fields in `packages/cloud/api`; no rendered UI surface in this diff.
<!-- evidence-row:walkthrough-video -->
- Walkthrough video: N/A - no user-facing UI flow; the exercised surface is a JSON API route, walked end to end in the live-run log below.
<!-- evidence-row:backend-logs -->
- Backend logs: structured `[Voice STT API] …` lines showing every lane firing (whisper multipart + timestamps DTO, malformed-200 502s, validation rejections, ElevenLabs billing/error mapping): [stt-route-tests-and-backend-logs.log](https://gist.githubusercontent.com/lalalune/7d9909564d6c54271d0b47a857c24f7d/raw/f62d6434e6ae52acd7bde0ee7257dcf8ff1006b3/stt-route-tests-and-backend-logs.log) — and the live run through the deployed Railway services: [stt-live-railway-run.log](https://gist.githubusercontent.com/lalalune/7d9909564d6c54271d0b47a857c24f7d/raw/a4d2174839087aec22c7eaf50c7db70e0b35836a/stt-
