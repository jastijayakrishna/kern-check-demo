# fix(parity): extract the 11 missing RC expectations and gate the omission in CI

## What & why

`node tools/parity/extract-expected.mjs --check` reported 11 `RC.*` keys as drifted. **They had not drifted — they had never been extracted.**

PR #795 (2026-08-17) wired 11 new customer targets in `app-targets.mjs` and listed each in `rendered-conformance.pending.json` with an honest blocker, but never ran the extractor for them:

`RC.await_accept` · `RC.cart_empty` · `RC.item_removed` · `RC.list_error` · `RC.list_loading` · `RC.menu_closed` · `RC.no_rider` · `RC.pay_confirmed` · `RC.refunded` · `RC.rejected` · `RC.track_prep`

`--check` renders every wired mobile target and diffs it against the committed JSON. With no file on disk, `previous` is `null`, which can never equal a fresh render — so **a missing expectation prints exactly like a stale one** (`≠`). Nothing caught it because `--check` was not wired into CI at all.

**The premise correction worth stating plainly:** the other 56 committed expectations reproduce byte-for-byte, so no expectation was stale and nothing was being validated against a stale fixture. All 11 are *pending*, so the conformance suite skips them; the two asserted RC keys — `RC.home` and `RC.orders_empty` — were never in question. The defect was an unrun extractor and a check that wasn't running, not drift.

### The two holes, both closed

**1. The coverage ledger exempted pending keys from having an expectation file at all** (`if (key in PENDING_KEYS) continue`). Pending suspends the *assertion*, never the *extraction* — the mock's own truth is what a pending entry's blocker is measured against. `rendered-conformance.test.tsx` now adds three browser-free (therefore **blocking**) tests:

- every wired+fixtured target has a committed expectation, pending included;
- `expected/index.json` equals the directory listing (catches a hand-added/deleted file);
- no expectation outlives its wired target (catches a retired/renamed screen's leftover JSON).

**2. `--check` now runs in CI**, as the last step of `parity-render`. It stays **non-blocking**: it needs Chromium, and browser rendering is environment-sensitive — the same reason that job already carries `continue-on-error`, and the reason `extract-expected.mjs`'s own header says a browser guardrail cannot be the blocking gate. Last in the job on purpose: a job-level `continue-on-error` still skips steps *after* a failing one, so running it after the artifact upload means drift never costs the PR its screenshot evidence. It writes its verdict — and the drifted key names — to the job summary.

So "it can't recur" is enforced by the blocking half; the browser half supplies the deeper content-drift signal, visibly, without gating merges.

Docs updated: `docs/SCREENSHOT-LANE.md` (a which-half-runs-where table + how to read a `≠`), `docs/PIXEL-PARITY-TRACKER.md`, the extractor header, and the pending ledger's stale conform/not-conform counts (was "7 conform, 32 do not"; now 24 of 67).

## Risk & rollout

- **User-facing?** no — parity tooling, CI config, tests and docs only. No app or design source changes.
- **DB migration?** no
- **Wire-contract change?** no
- **Mobile:** n/a — the only `apps/mobile` change is a test file.

`packages/design/**` is untouched, so the reverse-drift freeze does not apply.

## Rollback plan

Revert the commit. It adds data files, test cases, one CI step and docs; nothing is consumed at runtime and no deployed surface changes. Reverting only restores the previous (unenforced) state.

## Checklist

- [x] `pnpm typecheck && pnpm build && pnpm test` green locally
- [x] New behavior has a test that would have caught its absence
- [x] Migration (if any) passes the online-safe guard; enums stay in lockstep with `@lynia/shared` — n/a
- [x] Docs updated where behavior/status changed (`docs/`, runbooks)

### Verification

| Check | Result |
|---|---|
| `extract-expected.mjs --check` | **67/67 reproduce exactly** (was 56/67, with 11 reported `≠`) |
| `pnpm --filter @lynia/mobile test` | 185 suites / **1495 passed** |
| mobile
