# Implement 003: export the trip

One server-side projection, four client-side writers.

GET /api/trips/:tripId/export?detail=share|full returns a projected payload;
the device turns it into a file. Rendering stays on the device deliberately —
that is what makes an export work with no signal.

The feature is server/src/lib/export-view.ts and the field-policy tables in
it: Record<keyof Place, ExportLevel> and one per entity, so adding a column to
Place is a compile error until someone decides whether it travels (FR-010,
FR-011). That guard is only real with a typecheck in the test path, so
`npm run typecheck` is now a script and part of the gate.

The caller's TripView is applied *before* the field policy (FR-008). Reversed,
a hidden stay would be cut down to a name and an address and then exported.
A hidden stay takes its tips and its day-plan link with it; stats.included_stays
is the only place the response admits a view was applied.

Neither version carries the flight, the shopping list, the documents or any
member name (FR-004a) — for an owner too. They have no policy entry at all,
and the trip title is derived without the member-name fallback.

- Two new DataStore reads (listAllPlaces / listAllTips) bring assembling a
  payload from ~60 queries to five, pinned in ordering.test.ts against the
  per-parent reads and asserted at 3x real trip size.
- src/export/outline.ts is the document before it is a file; PDF, DOCX and
  XLSX all render it, so a format cannot widen what is included (FR-014).
  Only the JSON backup reads the payload, and it is the only writer that
  emits identifiers.
- PDF via jspdf + jspdf-autotable, two-pass so the contents listing and
  "Page n of m" are right; DOCX/XLSX via fflate and the OOXML parts
  themselves, chosen on precache weight and on spec 007's reading
  requirement (research R3).
- Everything under src/export/ is dynamically imported and precached, which
  is the offline guarantee; jsPDF's unreachable html2canvas/canvg/dompurify
  chunks are kept out of the manifest.
- Two labelled actions, never a toggle (FR-005). The share/save sheet is a
  second tap, which is what keeps iOS Safari's Web Share working (R7).
- Background prefetch of both levels on trip home (R4, SC-004).
- trip_exported declared before its call site; failures speak (FR-020).

Contract merged into specs/001-japan-trip-app/contracts/api.md.

Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01BAt6drkgS38DBc2nSpRCsk
