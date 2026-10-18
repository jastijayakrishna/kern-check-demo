# feat(app-blocks): W13 owner listing controls — unpublish/republish, moderation history, surfaced edit (P3)

## W13 App Blocks — owner listing controls (Phase 3)

Owner-facing post-approval controls on **/apps/my-submissions** for **off-site (external-link)** listings, wiring the already-merged Phase 1 owner procs (`unpublishOwnListing` / `republishOwnListing` / `listMyListingModerationEvents`). Everything stays **dark** behind the existing `app-blocks-author` / `appListings` gates already on the page. **No migration.**

### What's here
- **Unpublish (live → hidden).** A live listing gets a confirm-gated **Unpublish** action (`unpublishOwnListing`) — hides the app from the store immediately, no re-review. Reason optional.
- **Republish vs moderator takedown (the load-bearing distinction).** A removed listing shows **Republish** *only* when its most-recent moderation event is the owner's own `owner-unpublish`. A listing a **moderator** removed (delist/purge) instead shows a **"Removed by a moderator"** state with **no republish button** — the server forbids an owner self-restoring a takedown, so the UI must never offer a button that would 403. Eligibility is read from the listing's last moderation-event action (surfaced in the list query), not a per-row history fetch; the server guard remains authoritative (a race surfaces as a mutation error).
- **Moderation-history modal** ("why was this hidden / un-approved?"). Renders the listing's moderation-event timeline via `listMyListingModerationEvents` — action + date + verbatim reason, newest-first, owner-scoped.
- **Surfaced edit.** The existing shadow-revision **Edit** entry point (`/apps/submit?edit=<id>`) is preserved and hardened to hide on a removed listing (edit is forbidden there server-side). No backend change.

### How republish eligibility is determined
`listMySubmissions`' projection is extended (additively, PII-safe) with:
- the listing's **true lifecycle status** (`AppListing.status`) — distinct from the publish-**request** status, which stays `approved` after an owner-hide / mod-delist, so the list can't otherwise tell a live listing from a hidden one; and
- **`lastModerationAction`** — a single batched last-event query over the removed listings on the page (mirrors the existing `hasPendingRevision` second query). This drives the owner-hidden-vs-mod-removed branch without an N+1 per-row fetch.

### Scope
Owner unpublish/republish + moderation-history + surfaced-edit are **off-site only** — the Phase 1 procs are offsite-scoped (on-site app-block listings manage via the block flow, which has a different edit path and no owner-takedown surface). Removed listings keep their existing status-section placement; the per-row badge + actions reflect the true listing state. The shared owner table config (`submissionsTable.ts` / `submissionsTableUi.tsx`) is untouched.

### Tests
- **Blocking unit project:** a pure owner-control view model (`offsiteOwnerControls`) pinning the status/last-event → state matrix and the unpublish/republish capability predicates (the browser-mode component suite is report-only).
- **Browser-mode component tests** (`OffsiteSubmissionsList`): live listing shows Unpublish and the confirm gate fires `unpublishOwnListing` with the right listing id (+ optional reason); an owner-hidden listing shows Republish → fires `republishOwnListing`; a mod-removed listing shows the "Removed by a moderator" state and **no** republish button; the history modal renders the timeline with verbatim reasons; the Edit link points at `/apps/submit?edit=<id>`. Existing section/filter/edit tests stay green.
- **Service tests:** the `lastModerationAction` projection (owner-unpublish ⇒ eligible, delist ⇒ forbidden, live ⇒ no events queried / null).

Ready for the audit gate.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

