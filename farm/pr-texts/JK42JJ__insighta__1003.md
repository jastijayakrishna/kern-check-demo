# fix(note): per-chapter video dedup — first embed, then timestamp pill (CP505 B)

**Diagnosis (가) confirmed (code+data):** §1⑤ content-clusters a cell's atoms with no per-video-spread constraint → a comprehensive video becomes N topics, each embedding the same video. Data: chapters with 2–12 videos available yet one video spanning 2–8 topics (387f5309 ch4 = 1 video / 8 topics / 11 videos). Flag-independent (topic-synthesis).

**B (immediate, render-only):** per chapter, a vid's first section keeps the full embed; later same-vid sections become a compact timestamp pill (a `t=` link → TimestampPlugin seeks the already-embedded player; repeats are the same chapter video at different timestamps). Topic text/atoms untouched; only the duplicate embed is replaced. Both narrative + legacy render. Test: same vid x3 sections → 1 embed + a t=192 pill. FE tsc 0 / vitest 417 / build 0. DDL none.

Root fix (A — §1⑤ over-decomposition) = separate follow-up. Prod-visible (flag-independent), revert-rollback. Ships before #1001 activation so the a/b/c/d eval is not polluted by repeats.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
