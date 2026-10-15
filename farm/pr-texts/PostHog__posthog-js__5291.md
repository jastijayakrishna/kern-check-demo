# feat(metrics): attach trace exemplars to flushed metric series

## Problem

- A metric recorded with `posthog.metrics` never links to a trace, even inside a sampled span. The Metrics UI has no exemplar to jump from a chart point to the request that produced it.
- Services that send metrics through the OpenTelemetry SDK get exemplars. The same services get none through `posthog.metrics`, so the gap is in the SDK.
- Companion change for Python: PostHog/posthog-python#1057.

## Changes

- A sample recorded inside a sampled span now stamps its series with an exemplar: the trace ID, the span ID, and the value.
- In posthog-node, a sample inside `posthog.withSpan` now carries that span's exemplar. The node client already exposes `getActiveSpan()`, so it satisfies the new optional `MetricsHost.getActiveSpan` with no wiring change.
- An unsampled span gives no exemplar. That span is never exported, so the link would point at a trace that does not exist.
- One exemplar per series per flush window, and the last sample wins. A window that a failed flush merges back keeps its exemplar.
- A data point without an exemplar keeps its exact previous wire shape.
- Wire shape matches the OTLP/JSON exemplar that PostHog ingest already parses: hex `traceId`/`spanId`, nanos as a decimal string.
- Browser: no change in behavior. The browser SDK has no active-span API yet, so its host does not implement `getActiveSpan`.

## Release info Sub-libraries affected

### Libraries affected

- [ ] All of them
- [ ] posthog-js (web)
- [ ] posthog-js-lite (web lite)
- [x] posthog-node
- [ ] posthog-react-native
- [ ] @posthog/react-native-plugin
- [ ] @posthog/react
- [ ] @posthog/ai
- [ ] @posthog/convex
- [ ] @posthog/next
- [ ] @posthog/nextjs-config
- [ ] @posthog/nuxt
- [ ] @posthog/openfeature-node-provider
- [ ] @posthog/openfeature-web-provider
- [ ] @posthog/rollup-plugin
- [ ] @posthog/webpack-plugin
- [x] @posthog/types
- [ ] @posthog/browser-common

## Checklist

- [x] Tests for new code
- [x] Accounted for the impact of any changes across different platforms
- [x] Accounted for backwards compatibility of any changes (no breaking changes!)
- [x] Took care not to unnecessarily increase the bundle size

### If releasing new changes

- [x] Ran `pnpm changeset` to generate a changeset file

## 🤖 Agent context

**Autonomy:** Human-driven (agent-assisted)

- Written by Claude Code (`claude-opus-5-5`) through the PostHog Slack app. Skills: `writing-pr-descriptions`.
- Core tests cover each metric type, the no-span, unsampled, missing-traceparent and throwing-host cases, and merge-back after a failed flush. A posthog-node test checks the `withSpan` path end to end through the client.
- Not checked: an end-to-end send to a live ingest.

---
*Created with [PostHog](https://posthog.com?ref=pr) from a [Slack thread](https://posthog.slack.com/archives/C0C5XKA8Z0W/p1791909724682709)*

🤖 Generated with [Claude Code](https://claude.com/claude-code)
