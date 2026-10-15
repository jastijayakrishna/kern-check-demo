# fix: ConsoleLogger.warn() severity + add rate-limit sleep span

## Description

Fixes two bugs surfaced in a community thread investigating high latency (~67s wall-clock) in a 10-step agent:

1. **`ConsoleLogger.warn()` called `console.info()` instead of `console.warn()`** — warn-level logs were misclassified as info/stdout, making rate-limit warnings invisible in log backends filtering by severity.

2. **Rate-limit sleep had no OTel span** — the hardcoded 10s `delay()` when `x-ratelimit-remaining-tokens < 2000` only emitted a warn log (which was invisible per bug #1). Added a `rate-limit-sleep` child span with `{ remainingTokens, delayMs }` metadata so the sleep is visible in traces.

3. **Fixed lockfile resolution** — `agent-sdks/openai` had a stale `eslint@10.3.0` lockfile entry after a merge; updated to `10.4.1`.

### Changes

- `packages/_internal-core/src/logger/index.ts`: `console.info()` → `console.warn()` in `ConsoleLogger.warn()`
- `packages/core/src/llm/model/model.ts`: Added `rate-limit-sleep` span in both `__text` and `__stream` paths
- `packages/core/src/llm/model/model.loop.ts`: Added `rate-limit-sleep` span in agentic loop path
- `packages/core/src/logger/console-logger.test.ts`: Updated 3 tests to assert `console.warn`
- `packages/core/src/llm/model/model.test.ts`: New test verifying span creation with correct name/metadata when rate-limit fires
- `observability/sentry/src/tracing.test.ts`: Updated test that was codifying the same `console.info` bug
- `pnpm-lock.yaml`: Fixed stale `eslint@10.3.0` → `10.4.1` for `agent-sdks/openai`

## Related issue(s)

Community-reported latency investigation (Slack thread). No GitHub issue.

## Type of change

- [x] Bug fix (non-breaking change that fixes an issue)
- [x] Test update

## Checklist

- [x] I have linked the related issue(s) in the description above
- [x] I have made corresponding changes to the documentation (if applicable)
- [x] I have added tests that prove my fix is effective or that my feature works
- [ ] I have addressed all Coderabbit comments on this PR

Link to Devin session: https://app.devin.ai/sessions/ce59a3645593455aa14f4397eda972d7
Requested by: @roaminro

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## ELI5

This PR fixes two observability problems: warning messages were being sent to the wrong console stream, and a repeated 10-second pause used for rate-limiting was invisible in traces—both are now fixed so logs and traces accurately show warnings and delay time.

---

## Overview

This PR includes two fixes from a latency investigation:

1. ConsoleLogger.warn() now calls console.warn() (previously console.info()), so warn-level logs are classified correctly by log backends.
2. The hardcoded 10s rate-limit backpressure sleep (triggered when x-ratelimit-remaining-tokens < 2000) is now wrapped in a "rate-limit-sleep" OpenTelemetry child span with attributes remainingTokens and delayMs and the warn log now includes remainingTokens.

---

## Changes

- packages/_internal-core/src/logger/index.ts
  - ConsoleLogger.warn() uses console.warn() instead of console.info().

- packages/core/src/llm/model/model.ts
  - In MastraLLMV1.__text and __stream: create a "rate-limit-sleep" child span around the 10s sleep, record remainingTokens and delayMs, end the span after sleep, and include remainingTokens in the warn message.

- packages/core/src/llm/model/model.loop.ts
  - In MastraLLMVNext.stream (onStepFinish): add the same "rate-limit-sleep" child span and warn message including remainingTokens.

- Tests
  - packages/core/src/logger/console-logger.test.ts: updated assertions to expect console.warn for warn-level logs.
  - observability/sentry/src/tracing.test.ts: updated to spy on console.warn for DSN-missing warning.
  - packages/core/src/llm/model/model.test.ts: added regression test verifying creation and lifecycle of the rate-limit-sleep span (attributes remainingTokens and delayMs), the warn log, and that the span ends after the 10s fake-timer sleep.

- Documentation/changesets
  - .changeset/* files updated to document the ConsoleLogger fix and rate-limit span instrumentation.

---

## Impact

- Warn-level logs will be routed and classified correctly by logging backends.
- Rate-limit backpressure delays are now visible in distributed traces as "rate-limit-sleep" spans containing remainingTokens and delayMs, aiding latency investigations where repeated 10s sleeps caused unaccounted trace time.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
