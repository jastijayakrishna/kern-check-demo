# fix(search-bar): keep caret in filter on operator pick; blank value stays unarmed (LFE-10501)

## TL;DR

Two autocomplete papercuts in the events search bar: picking a numeric/date **operator** then pressing Enter jumped the caret **out** of the filter block, and typing a **space between empty quotes** silently armed a random observed value for commit. Both fixed; the composer's pick logic is now a unit-tested pure function.

## Why (LFE-10501)

- **A — operator pick + Enter escapes the block.** On numeric/datetime fields the bar suggests operators (`>`, `>=`, …). Picking one landed `latency:> ` with the caret **after a trailing space, outside the block** — so the next keystroke typed the number *outside* the filter instead of building `latency:>500`.
- **B — space in empty quotes auto-selects a value.** With `-name:""` (or `-traceName:""`) and the caret between the quotes, pressing **space** flipped the value list from a plain, browsable list into an **armed, committable** one: a lone space matched every observed value *containing* a space, so Enter committed an unwanted value (e.g. `-name:"Agent workflow"`).

## What

- **A.** An operator pick now counts as *inviting more input* (like a `field:` key or an open `tags:(` group): it keeps the caret in the block and does not append a trailing space / mark the filter complete. AND/NOT already carried their own trailing space, so only the value-stage comparisons change.
- **B.** An empty **or whitespace-only** value is treated as "no value yet" — plain list, nothing active/armed, no match-op refinements. A value with real content plus surrounding spaces (`"foo "`) still counts as typed.
- Extracted the composer's pure pick text/caret computation into `applyPick` and added client coverage for both defects (the ~1.3k-LOC contenteditable controller had none for this path).

## Result

Verified live in the browser on the v4 observations table:

- `latency:` → pick `>` → caret stays at `latency:>|` → type `500` → `latency:>500` → Enter → `latency > 500` applied.
- `-name:""` caret between quotes → 0 armed; press space → `-name:" "`, still 0 armed; Enter does **not** insert an observed value.
- Normal typing unaffected: `level:ERR` still ranks + arms `ERROR` for Enter.

<details>
<summary>Mechanism &amp; tests</summary>

- **A** lived in the pick classifier: an operator insert ends with no `:`/space/`(`, so `invitesMoreInput` was false and `completesFilterAtEnd` appended a space + extended `replaceTo` to end-of-draft, placing the caret outside the token. Fix: add `option.kind === "operator"` to `invitesMoreInput`.
- **B** lived in value planning: `stripValueQuotes('" "')` → `" "`, which `rankFilter` matched against every value containing a space and `autoHighlight` then armed. Fix: normalize a whitespace-only typed value to `""` at the source in `planInputCompletions`, so every downstream empty-value path (list, match-ops, autoHighlight) applies uniformly.
- Tests: `completions.clienttest.ts` — `applyPick` caret assertions for numeric/datetime/score operators (plus AND/NOT and value-completes-at-end guards) and a `planInputCompletions` case for space-in-empty-quotes (plus a real-prefix-still-arms guard). All 185 search-bar client tests pass; lint + typecheck clean.

</details>

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- greptile_comment -->

<details open><summary><h3>Greptile Summary</h3></summary>

This PR fixes two autocomplete bugs in the search bar (LFE-10501): picking a comparison operator (`>`, `>=`, etc.) was jumping the caret outside the filter block due to a missing `operator` guard in the `invitesMoreInput` classification, and typing a space between empty quotes was silently arming an observed value for commit because whitespace-only typed text was not normalized to empty.

- **Bug A (operator pick)**: `applyPick` now treats `option.kind === "operator"` as `invitesMoreInput = true`, preventing the trailing space + `completesFilterAtEnd` path that was placing the caret after the space and outside the token.
- **Bug B (space in empty quotes)**: 
