# fix: three things that were left behind, one of them not as planned

The three integrity gaps found while restructuring admin. **One of them is not fixed the way the plan said**, and that is the substance of this PR.

## 1. The overview picker read a key that does not exist

`OverviewMetricsSetting` asked `app_settings` for `overview_formulas`, which **0048 deleted**. Dead rather than visibly broken: no key, so `resolveFormulas` got `undefined` and nothing extra was offered.

**The plan said to repoint it at `member_formulas`. That is wrong.** 0048's own header says why:

> A new key rather than reusing `overview_formulas`, because the same text means something different now — reusing it would have made an alliance-wide expression silently become a member one.

A formula runs on a **member** now and lands as a column on the roster. `OverviewPanel` already followed through — it hardcodes an empty formula list with that reasoning written out. Repointing the picker would have let an admin tick a tile, save it, and watch the overview draw nothing: strictly worse than the dead read, and the exact conflation 0048 existed to undo.

So the picker now matches the panel — catalogue metrics only — and a test pins it, because the wrong repair is the obvious one.

## 2. `alliance_names` had no reader

`apply_alliance_summary` has filled it since 0008. The player page has shown `player_names` since it existed; the alliance side was simply never built.

A table rather than the player page's badges, because there are three facts. **An alliance can keep its name and change only its tag**, so rows are filtered on both halves — filtering on the name alone would drop exactly that rename, which is the one people are most likely to be searching for.

## 3. `arena_matches` — recorded, not acted on

Nothing in `services/` or `apps/` writes it; only `legacy/` reads it. The `al.battle.rank.info` shape again. Whether to drop it depends on whether production has rows, which cannot be counted from this Mac, so it goes into `docs/handover.md` as a check with both answer branches.

Worth knowing before anyone deletes it: **three pgTAP files use it as a convenient snapshot table** (`01_conventions`, `05_notifications`, `33_arena_member_only`). Moving them is most of the work, and finding that out at deletion time would be the unpleasant way.

## Verification

`pnpm check && pnpm typecheck && pnpm test && pnpm build` pass; 221 tests, 2 new.

Both screens rendered from the real components against the real stylesheet. The alliance history shows the tag-only rename surviving the filter and a tagless capture reading `—`; the picker was rendered in jsdom (it needs effects) and offers every catalogue metric with no `formula:` id anywhere in the markup.

No SQL in this PR.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
