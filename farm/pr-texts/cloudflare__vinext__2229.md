# fix(link): start viewport prefetches immediately

## Summary

- start viewport-triggered App Router prefetches immediately after intersection instead of waiting for an idle callback
- retain low network priority for viewport prefetches and high priority for hover/touch intent
- add a production fixture covering optimistic navigation to an unprefetched dynamic sibling while another sibling has been prefetched

## Next.js parity

- Pinned reference: `vercel/next.js@ee6e79b1792a4d401ddf2480f40a83549fe8e722` (`v16.2.6`)
- Test: https://github.com/vercel/next.js/blob/v16.2.6/test/e2e/app-dir/optimistic-routing/optimistic-routing.test.ts
- Scheduler source: https://github.com/vercel/next.js/blob/v16.2.6/packages/next/src/client/components/segment-cache/scheduler.ts

Next.js schedules viewport-discovered links promptly while retaining lower priority than explicit hover/touch intent. Vinext deferred viewport prefetch dispatch through `requestIdleCallback`, so links mounted during an interaction could miss the request window needed for optimistic routing.

## Targeted local validation

- `132` targeted Link/router unit tests passed
- `1` production Playwright optimistic-routing fixture passed with one worker
- focused format, lint, type, and diff checks passed
- no raw Next.js E2E or broad local suite was run

