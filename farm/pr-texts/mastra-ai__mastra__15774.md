# fix(memory): preserve OM response message boundaries

## Description

Preserves loaded memory assistant messages as merge boundaries so Observational Memory cannot append fresh agent output onto previously persisted assistant output when a thread is rerun or a long-running loop continues.

Changes in this PR:
- `MessageMerger` now blocks normal assistant `response` → `memory` merges when the incoming response is a new message.
- Same-id response updates are still allowed so canonical streaming/tool-result updates can update the message they belong to.
- Agent-network append behavior is preserved via the existing `_agentNetworkAppend` escape hatch.
- Existing OM turn/step persistence and sealed-message filtering semantics are left unchanged.

This means the fix is the source-boundary guard itself: reruns and long-running loop continuations produce new response messages instead of mutating messages loaded from memory.

## Related Issue(s)

Slack report: OM duplicate DB entries when rerunning an agent on the same thread without a new user message.

Discord screenshot report: long-running Codex/Superset loop produced duplicate message IDs during persisted loop output.

## Type of Change

- [x] Bug fix (non-breaking change that fixes an issue)
- [ ] New feature (non-breaking change that adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to change)
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Performance improvement
- [x] Test update

## Checklist

- [x] I have made corresponding changes to the documentation (if applicable)
- [x] I have added tests that prove my fix is effective or that my feature works
- [x] I have addressed all Coderabbit comments on this PR

## Verification

- `pnpm exec vitest run packages/core/src/agent/message-list/tests/message-list.test.ts -t "handles upgrading from tool-invocation|merges tool-invocation upgrade|inserts step-start|upgrades only matching|drops text not present|merges incremental streaming" --reporter=dot`
- `pnpm exec vitest run packages/core/src/agent/message-list/tests/message-list.test.ts --reporter=dot`
- `pnpm exec vitest run packages/core/src/agent/message-list/tests/message-list-sealed.test.ts --reporter=dot`
- `pnpm exec vitest run packages/memory/src/processors/observational-memory/__tests__/observational-memory.test.ts -t "should not duplicate sealed-for-buffering messages during per-step save" --reporter=dot`
- `pnpm --filter @mastra/core check`
- `pnpm --filter @mastra/memory check`
- `pnpm --filter @mastra/core lint`
- `pnpm --filter @mastra/memory lint`
- `cd packages/memory/integration-tests && pnpm vitest run src/with-libsql-storage.test.ts --reporter=dot --bail 1 -t "Observational Memory persisted ordering"`
- `git diff --check`

## CI Status

44 passed, 0 failed, 0 pending.

Link to Devin session: https://app.devin.ai/sessions/5698cdbae2424f148bc5410353764edf
Requested by: @TylerBarnes
<!-- devin-review-badge-begin -->

---

<a href="https://app.devin.ai/review/mastra-ai/mastra/pull/15774" target="_blank">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://static.devin.ai/assets/gh-open-in-devin-review-dark.svg?v=1">
    <img src="https://static.devin.ai/assets/gh-open-in-devin-review-light.svg?v=1" alt="Open in Devin Review">
  </picture>
</a>
<!-- devin-review-badge-end -->
