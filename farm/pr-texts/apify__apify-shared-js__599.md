# fix: remove obsolete @ts-expect-error for nullishDependencies

Lock file maintenance updated `mathjs`, which now properly types `nullishDependencies`. The `@ts-expect-error` directive became invalid, causing build failures.

## Changes

- Removed `@ts-expect-error` comment from `packages/actor-memory-expression/src/memory_calculator.ts`

The directive was originally added to suppress errors for an untyped mathjs export (see https://github.com/josdejong/mathjs/issues/3597). The updated dependency version resolved this upstream.

<!-- START COPILOT CODING AGENT TIPS -->
---

💬 We'd love your input! Share your thoughts on Copilot coding agent in our [2 minute survey](https://gh.io/copilot-coding-agent-survey).
