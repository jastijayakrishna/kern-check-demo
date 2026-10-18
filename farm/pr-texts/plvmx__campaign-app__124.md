# fix: remove optional Mobile field from Add Campaign dialogs

## Summary
Removes the "Mobile (Optional)" manual input from the Add Campaign UIs:
- `CampaignCreateForm` — the "Add Campaign" dialog on the main feed (`/app`)
- `CampaignForm` — used on the "Create Campaign" page (`/capture`)

Regular users never saw this field to begin with (it's auto-filled silently from their profile); this only removes the admin/state-reporter-visible manual entry point. The underlying `mobile` value, its auto-fill logic, and the submit payload are unchanged — only the visible input is gone.

**Not touched, on purpose:**
- `InlineEditForm` — this is the campaign *edit* UI, not an Add Campaign dialog.
- `CampaignForm`'s other usage on `/record-results` ("Record Campaign Results") — that page uses the form to search for an *existing* campaign, not create one.

## Test plan
- [x] `npx tsc --noEmit` — clean
- [x] `npm run lint` — 0 errors (pre-existing warnings only, none from this change)
- [x] `npm test` — 275/275 passing
- [x] `npm run build` — succeeds
- Purely a UI-removal with no new logic branches, so no regression test applies (per the visual/copy-change exemption in the testing policy).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
