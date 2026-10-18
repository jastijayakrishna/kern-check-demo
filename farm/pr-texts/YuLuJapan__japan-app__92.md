# Export: the day plan runs the whole trip, and the feature goes behind export-trip

Follow-up to #91, which shipped the export. Two commits.

---

## 1 · The day plan runs the whole trip, and says which city each day is in

The day-by-day plan came out as a flat list of only the days that carried an activity, with no stop attached. Two things were wrong with that:

- **No city per day.** A printed Full copy read `6 Oct 2026 · 20:00 Ramen Bar` and left the reader working out which city they were in. The app's own day-by-day screen names the city above every day (`coveringSteps` / `dayZones` in `src/lib/schedule.ts`); the export dropped it.
- **Empty days vanished.** A day nobody had typed into wasn't in the file at all — including the day you move between stops. That is the worse half: the gaps are exactly what someone reading a printed plan plans into, and hiding them makes the trip look fuller than it is.

The flat shape was what `data-model.md` §2 specified, so this was built to the design doc without checking it against what the app already shows. The doc is corrected here too.

**The change**

- `ExportDay` gains **`zones`** — the city or cities the day touches, in journey order. **Two of them is a moving day**, because a stop's last day and the next stop's first day are the same date. Empty for a day no stop covers, which is a real gap in the journey and is shown as one rather than guessed at.
- **`days` now runs `start_date` to `end_date`.** A day with nothing planned is listed with an empty `items` array. Any day carrying an item from outside the trip's window is included too — the range rule in `lib/trip-dates.ts` makes that impossible today, and silently dropping a stranded activity would be worse than printing a day off the end.
- **`stats.day_count` is unchanged in meaning** — days carrying at least one item — so it stays the answer to "how much of this is planned" now that `days.length` is the trip's length.
- All three readable writers render it from the same outline: the city under each day's heading, an honest `Nothing planned.` rather than a missing day, and a **Where** column plus a row per empty day in the XLSX, so sorting the sheet is not what reveals a gap.

**One thing worth knowing.** The moving day reads **`Tokyo to Kyoto`**, not `Tokyo → Kyoto`, and that is a constraint rather than a style choice: the PDF uses jsPDF's core Helvetica with no embedded font — the research R2 decision that keeps the precached chunk small — and its WinAnsi encoding has no `U+2192`, so an arrow would have printed as a wrong glyph. I wrote the arrow first and the PDF test caught it. There is now a guard asserting that the wording the export chooses **for itself** stays inside that encoding; trip content is the traveller's business and deliberately out of its scope.

---

## 2 · The feature goes behind `export-trip`, defaulting off

This reverses the plan's "not flagged" decision, at the owner's request. The plan argued a flag means the button is absent on a new device's first load, since flags land after first paint. **That cost is real and is accepted** — the board's rule is the rule, and the argument against it would exempt every read-only feature, while what the flag buys is the risk this feature does carry: a 415 KB PDF engine running on whatever browser the traveller has.

Follows the `files-rename` precedent exactly:

- **Gates the entry points, not the endpoint** — the trip-home link, the `/trips/:tripId/export` route (so a bookmark is closed too, not only the link) and the payload prefetch. The API stays live: a flag is a rollout control rather than an access control, and gating the route would only add a way for a correctly-authorised request to fail.
- **Defaults off**, so the code carries the flag before PostHog does and deleting it there can never take a screen down.
- **The prefetch follows the flag** rather than running regardless — otherwise that is two requests per trip-home mount, for every account, on behalf of a screen nobody can open. When the flag arrives late, the hook re-runs and warms 
