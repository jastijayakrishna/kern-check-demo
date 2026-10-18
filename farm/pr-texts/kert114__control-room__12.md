# Re-apply repository cleanup (Part 3) on top of merged security PR

## Summary

Re-applies #10 (Part 3 cleanup), which was reverted in #11 to unblock the merge of #9. This is `git revert 833e8d2` with the single conflict in `src/app/(app)/refunds/page.tsx` resolved: the "Switch to variant B" `<Link>` block is removed and the `TruncationNotice` from #9 is kept.

Content is otherwise identical to #10: delete `src/app/(app)/refunds/compare/` and its four references, delete `prototypes/`, `assets/*.png`, `design-directions.md`, `.agents/skills/verify-fintech-tool/` (+ the `AGENTS.md`/`README.md` lines), and move the eight refunds presentational components into `src/modules/refunds/ui/` with import updates only.

Verified on this branch: `pnpm lint`, `pnpm typecheck`, `pnpm test` (160 passed), `pnpm build`, and `pnpm test:e2e` (65 passed, 1 skipped) against a migrated and seeded database.

Link to Devin session: https://app.devin.ai/sessions/443802f814954c098a0825916cf012b4
Open in Devin Desktop: https://app.devin.ai/desktop/session/443802f814954c098a0825916cf012b4?variant=devin
Requested by: @kert114
