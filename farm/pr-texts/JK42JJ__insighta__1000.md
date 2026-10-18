# feat(note): loop-2 references render — 참고 자료 + 보강 자료 (P-REF-DUAL) (CP504 §4.5.1)

Final Track-A piece (P-REF-RENDER). Renders loop-2 enrich data (#998) in the note: `chapter.research[]` → per-chapter **보강 자료** block (fact [ref_id]); `book.references[]` → bottom **참고 자료** section. Atom vid/ts stays inline (video half) + references[] (web half) = **P-REF-DUAL**. Additive FE types; **no section for normal/legacy books** (enrich data absent → render no-op). Test: renders both when present, none when absent. FE tsc 0 / vitest 413 / build 0. flag-off (prod inert).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
