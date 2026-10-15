# Workbench for every session: folderless sessions get Subagents + Background

## Summary

A DM session started without picking a folder previously had no Workbench at all — no ↗ into Focus, no panel toggle — so subagents and background jobs were invisible and **Stop** was unreachable. Per the 2026-10-06 decision, the Workbench now exists for **every** session: folder-bound tabs (Changes/Files/PR/Terminal/Preview) still require a folder (D-#19 per tab), while engine tabs (Subagents/Background/Plan) render whenever their capability is declared.

- `workbench.tsx`: new `folderless = work == null && isDM` discriminator gates folder-bound tabs. `bgOn` also covers `onStopJob != null` (capability declared) with zero jobs. New `onAllowed` prop reports the settled tab set (`null` while probing) so the caller can hide the toggle when nothing renders.
- `focus-view.tsx`: `wbAvailable` = `host != null && (static possibility || reported tabs || wbOpen)` — a folder session can always ask the host; a folderless session needs an engine tab (jobs / declared `background_jobs` / helpers / plan / `?tab=subagents`); a channel thread keeps mock tabs. `dm.tsx` now passes `host` unconditionally (accessors take `cwd` per call).
- `workbench_open` (AC-7): `WorkbenchOpenTarget` gains `{tab: 'subagents'|'background'|'plan'}` — the only shape a folderless session accepts; the relay returns `conflict` for `file/diff/pr/url` targets when `conversation.cwd` is unset; the phone card maps engine tabs to its Subagents/Background/Plan sheets.
- D-#114 rewritten in place in `docs/DECISIONS.md`; prototype `dm-builder` gained a folderless thread (helpers + running watcher) to demo the two engine tabs.

## Tier
Normal

## Verification
- **Red → green**: new spec `e2e/ac-543-workbench-every-session.spec.ts` — on main it fails at "toggle renders" (folderless session has no Workbench); on this branch all 3 tests pass.
- `e2e/ac-114` AC-6 leg rewritten for the new rule — green.
- Unit: `session-events.test.ts` (AC-7: `tab` target fans out, folder targets → `conflict`), `gateway.test.ts` (`tab` targets forward + updated exactly-one-of message) — green.
- `bun run verify:fast` green (biome / schema:check + regen / typecheck / vitest / test:nonts / build:prototype / build:harness / check:mobile-bundle).

## AC checklist
- [x] **AC-1** folderless session gets ↗ + Workbench toggle; only Subagents + Background render (Plan when a turn has one); no empty folder tabs — e2e AC-1..3 test.
- [x] **AC-2** Background lists running/finished jobs with working Stop; Subagents rows show steps + report; live during and after the turn — e2e asserts running rows mid-turn and after settle.
- [x] **AC-3** "N subagents · Open" link lands on Focus → Subagents (`?tab=subagents`) — e2e panel round-trip.
- [x] **AC-4** folder session unchanged — e2e AC-4 test asserts all tabs render; full ac-114/ac-179 suites re-run.
- [x] **AC-5** nothing to show → toggle hidden — e2e AC-5 test (folderless + caps hidden via `LILOS_HIDE_CAPS`).
- [x] **AC-6** D-#114 rewritten in place; old rule under `Not:`.
- [x] **AC-7** `workbench_open` `{tab}` target works folderless; folder targets return `conflict` naming the fix — relay + gateway unit tests.

## Screenshots (1288x700, light / dark)

![Subagents — light](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmdfaENGNnNUNmpaVUYyenpvTC9jNTc0NzE4Zi0xN2RkLTQ1YTItOTkxNS04NjYyNGMzMTkwNTEiLCJpYXQiOjE3OTEyODQ4MDMsImV4cCI6MTc5MTg4OTYwMywib3JnX2lkIjoib3JnX2hDRjZzVDZqWlVGMnp6b0wiLCJmaWxlbmFtZSI6InN1YmFnZW50cy1saWdodC5wbmcifQ.DHa3_RpLM6HhGzWHBeAvp6KPfIwqpyZr0hY7OyOFyV4)
![Subagents — dark](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmdfaENGNnNUNmpaVUYyenpvTC8yOTVkYTljNS0xODNlLTQ3MGMtYjExMi03MTBjZTc0YTg3OWEiLCJpYXQiOjE3OTEyODQ4MDMsImV4cCI6MTc5MTg4OTYwMywib3JnX2lkIjoib3JnX2hDRjZzVDZqWlVGMnp6b0wiLCJmaWxlbmFtZSI6InN1YmFnZW50cy1kYXJrLnBuZyJ9.u6m_5mL8Bf0KfEUyPolwLan2IE9i-UzbxJ7p6YemOPY)
![Background — light](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmdfaENGNnNUNmpaVUYyenpvTC81OTIxNTc1Ni1kZjY4LTQxNTAtYTkzMi01MjNjMmI5YWE5NTMiLCJpYXQiOjE3OTEyODQ4MDMsImV4cCI6MTc5MTg4OTYwMywib3JnX2lkIjoib3JnX2hDRjZzVDZqWlVGMnp6b0wiLCJmaWxlbmFtZSI6ImJhY2tncm91bmQtbGlnaHQucG5nIn0.ZDZrTtchNioQeDAMaQ_dXY5UB9QfpoK2XBYbPTsKTsI)
![Background — dark](https://app.devin.ai/api/presigned_proxy?token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjpudWxsLCJidWNrZXRfbmFtZSI6ImRldmluYXR0YWNobWVudHMiLCJidWNrZXRfa2V5IjoiYXR0YWNobWVudHNfcHJpdmF0ZS9vcmdfaENGNnNUNmpaVUYyenpvTC81OThjZmE2Yy03MmMzLTRlZWItYmFmNS0zZmNjNWU5N2IwYTEiLCJpYXQiOjE3OTEyODQ4MDMsImV4cCI6MTc5MTg4OTYwMywib3JnX2lkIjoib3JnX2hDRjZzVDZqWlVGMnp6b0wiLCJmaWxlbmFtZSI6ImJhY2tncm91bmQtZGFyay5wbmcifQ.Q9-O1225o08Q3KOq7_BTESUZeeZEHcq6pPQmiiiOfg8)

## How to try
Prototype `dm-builder` now contains a folderless thread ("Folderless: helpers + a watcher") — open its Focus to see the Workbench with only Subagents + Background. In the real app, start a DM session with "No folder · just chat" and run a turn with subagents or a background job.

Closes #543

Link to Devin session: https://app.devin.ai/sessions/211b70e0e98e461ead23f3b4494c293a
Open in Devin Desktop: https://app.devin.ai/desktop/session/211b70e0e98e461ead23f3b4494c293a?variant=devin
