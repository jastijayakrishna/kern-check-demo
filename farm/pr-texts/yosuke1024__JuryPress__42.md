# Dotted technical tokens are not sentence boundaries

## Problem

With the attribution rule gone, `CLAIM_STATEMENT_UNMATCHED` is the pipeline's blocking failure — and two shapes that appear constantly in open-source reviews trigger it. Yesterday's run (`season-2-manual-29667424637`, "Leaves") failed because one sentence was split into three:

```
Support for standard .gitignore and .ignore patterns ensures the tool integrates naturally...
  → "Support for standard ."
  → "gitignore and ."
  → "ignore patterns ensures the tool integrates naturally with developer workflows."
```

The model annotates one sentence; it matches none of the three fragments.

The attested-token mask structurally cannot cover either shape:

- it protects only dots **interior** to a token (`for (let i = start + 1; i < end - 1; i++)`), so a dotfile's **leading** dot was never protected — even when the evidence named the file;
- it requires **attestation**, which a review stating a file is **absent** can never have. `season-2-2026-07-18-daily` failed on exactly this: "no `SECURITY.md` ... is present" — a file that does not exist appears in no evidence.

## Change

Two lexical rules, both decided without evidence:

**A — dotfile leading dot.** A dot preceded by whitespace and followed *immediately* by an alphanumeric (`" .gitignore"`). Safe because no English sentence can end that way: a terminator follows a word character, never a space. Requiring no space *after* the dot means `"one . two"` still splits.

**B — known repository filenames.** A dot interior to a **closed list of whole filenames** (`README.md`, `SECURITY.md`, `package.json`, `Cargo.toml`, `go.mod`, `pyproject.toml`, …).

A generic `word.extension` pattern was written first and **rejected**: it protected `evilpackage.json` riding on an attested `package.json` — breaking a deliberate fail-closed property that an existing test guards — and it would have let a boundary hide behind an invented extension (`"the claim is false.json the tool is safe"`). Matching whole known names keeps every one of those splitting.

Hostnames still require attestation: nothing about `freeCodeCamp.org` is lexically decidable, and that stays exactly as it was.

## Verification against the stored records

| record | before | after |
|---|---|---|
| **manual-29667424637** (Leaves, yesterday's failure) | failed | **passed** (0 errors) |
| **2026-07-18-daily** (SECURITY.md) | failed | **passed** (0 errors) |
| manual-29626451493 *(published)* | passed | **passed** |
| manual-29633364803 *(published)* | passed | **passed** |
| request-36 | failed | still fails — unrelated annotation mismatch, no dotted token |

## Tests

New `tests/unit/dotted-token-segmentation.test.ts` pins both halves: the shapes that must stay one statement (including the two production failures verbatim), and the anti-evasion boundary that must not move — normal sentence boundaries, no-space smuggling (`passed.it`), unknown extensions, `evilpackage.json`, `package.json-evil`, and `false.json` all still split. The losslessness invariant is asserted via the codebase's own `assertLosslessSegmentation`.

Two baseline tests moved to the new line rather than to new numbers alone: the strict-scan over-split demo now uses a hostname (the case that genuinely still needs attestation), and the freeCodeCamp mismatch count drops 18 → 3, the remaining 3 being hostname mismatches.

Local: `typecheck` ✅ / `test:unit` **607 passed** ✅ / `test:e2e` 25 passed ✅

🤖 Generated with [Claude Code](https://claude.com/claude-code)
