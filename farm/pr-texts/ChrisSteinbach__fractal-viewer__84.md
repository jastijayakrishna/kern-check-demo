# Flame GPU: fall back to the main-thread GPU host when the worker GPU fails, and stick (fr-e07, fr-8ck); mobile-throughput instrumentation (fr-ul2)

Flame-GPU robustness + diagnostics, one branch, commit-per-item. Evolved from real Firefox-desktop testing (see the fr-8ck commit).

## fr-e07 + fr-8ck — Fall back to the main-thread GPU host when the worker GPU fails, then stick
**Problem (Firefox desktop, 24 GB card):** Firefox now exposes worker WebGPU, so the flame render runs worker-hosted — but the worker's WebGPU context fails ~2s in with `Not enough memory left` (a Firefox worker-allocation bug, *not* real VRAM: the backend already requests the adapter's max limits, and the main-thread GPU renders the same histogram fine). It surfaces as a **mid-render** snapshot failure, so the render silently dropped to CPU.

**Fix:**
- **`flame-worker-core.ts`**: route all six GPU-failure sites — the two create-time factories **and `runChunk`'s four mid-render catches** — through one `failGpuBackendToCpu` helper that ratchets `gpuFailed`, logs, and emits a new advisory `gpuUnavailable` event **once** (on the false→true transition). So a *mid-render* GPU failure now signals the host, not just a create failure.
- **`main.ts`**: on `gpuUnavailable` from a **worker**-hosted session with main-thread WebGPU (fine-pointer + `navigator.gpu`, no `?flamehost=worker` pin), escalate to the main-thread GPU host **and remember it** (`preferLocalHost`, sticky for the page session) — so only the *first* render eats the wasted worker attempt; the rest go straight to the working GPU. Chrome, where the worker GPU works and never fails, keeps the off-main-thread worker path untouched. An already-local session ignores its own signal → CPU stays the final fallback.
- Hardened the worker host's `terminate()` to detach handlers, so a stale queued worker message can't disturb the freshly-escalated local session.
- **Tests**: `gpuUnavailable` fires once on create failure, on a mid-render **accumulate** failure, and on a mid-render **snapshot** failure (the Firefox-OOM shape) — each still restarting on CPU; not on GPU success; once across a ratcheted restart.

## fr-ul2 — Instrument mobile flame throughput (accumulate vs readback vs scheduling gap)
A phone soak saw the production flame GPU path sustain **~50x less** than the `/gpu-bench/` raw-kernel number on the same Mali adapter. The bench's denominator is `sum(accumulate())` alone — no readback, no inter-chunk gap. Added opt-in per-chunk instrumentation to find where the wall time goes.
- **`flame-perf.ts`**: pure, tested `FlamePerfMeter` emitting a windowed `accumulate / readback / gap / other` split plus the bench-comparable pure-accumulate rate.
- **`flame-worker-core.ts`** / **`main.ts`**: driven from `runChunk` behind an `instrument` start flag wired to a `?flameperf` URL param. **Every added clock read is guarded**, so a non-instrumented run is timing-identical.
- Finding: the progressive redisplay already uses the on-device `snapshotDisplay` (display-res readback), not a full 126 MiB `snapshot()` per tick — that only happens on the final frame. Confirming the real split needs an on-device `?flameperf` soak (tracked on the bead); no behavioral fix shipped unmeasured.

## Verification
- `npm test` (lint + 1257 tests), `npm run build`, `npm run smoke` — all green.
- The escalation's per-session behavior (which host, sticky preference) lives in `main.ts` glue and needs a real browser to confirm end-to-end; requesting a Firefox-desktop + phone check from the reporter.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

