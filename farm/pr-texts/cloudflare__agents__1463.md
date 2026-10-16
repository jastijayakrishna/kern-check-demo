# fix(think): wrap stream-resume ACK fallback in sendIfOpen

## Summary

Follow-up to #1376. That PR hardened `agents/chat` and `@cloudflare/ai-chat` against the closed-WebSocket replay race but intentionally left `@cloudflare/think` for a separate PR. This is that PR.

`ResumableStream.replayCompletedChunksByRequestId` now returns `false` both when no completed stream is found *and* when a `sendIfOpen` call fails because the socket closed mid-replay. The matching fallback in `packages/ai-chat/src/index.ts` was updated to use `sendIfOpen`, but the identical pattern in `packages/think/src/think.ts:_handleStreamResumeAck` still used a bare `connection.send()` — so on the close-mid-replay path it would throw `TypeError: WebSocket send() after close` up through `onMessage`, which is exactly the failure mode #1376 set out to prevent.

This PR mirrors the `sendIfOpen` helper from `@cloudflare/ai-chat` into `@cloudflare/think` and routes the fallback `done: true` send through it.

## Review & Testing Checklist for Human

- [ ] Confirm copying `sendIfOpen` / `isWebSocketClosedSendError` into `think.ts` is preferred over exporting a shared helper from `agents/chat` (the same duplication already exists in `@cloudflare/ai-chat` and `agents/chat/resumable-stream.ts`).
- [ ] Sanity check the changeset entry — `@cloudflare/think` patch — matches the release process you'd expect for this kind of resilience fix.

### Notes

- No behaviour change on the happy path: `sendIfOpen` only swallows `TypeError: "WebSocket send() after close"` and re-throws everything else.
- Local verification: `npm run check`, `npm run lint`, and `npx nx run @cloudflare/think:test` (289 tests) all pass.


Link to Devin session: https://app.devin.ai/sessions/303193c332f24e08b4c8525adb58e285
Requested by: @whoiskatrin
<!-- devin-review-badge-begin -->

---

<a href="https://app.devin.ai/review/cloudflare/agents/pull/1463" target="_blank">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://static.devin.ai/assets/gh-open-in-devin-review-dark.svg?v=1">
    <img src="https://static.devin.ai/assets/gh-open-in-devin-review-light.svg?v=1" alt="Open in Devin Review">
  </picture>
</a>
<!-- devin-review-badge-end -->
