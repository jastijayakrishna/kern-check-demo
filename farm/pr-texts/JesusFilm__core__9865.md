# feat(campaign): journey list empty state on the public page

Closes #9861

Adds the `noJourneys` Campaign String ("Journeys for this region are coming soon") and prints it under the Journey list heading when the list has no live journey card, on the landing page and on a Region Page.

- **API:** `noJourneys` added to the Prisma `CampaignStringKey` enum (additive `ALTER TYPE ... ADD VALUE` migration), the seed (`campaignStrings.ts`) and so `campaignLocale.ts`; translated through the `libs-journeys-ui` bundle like the other strings. Generated schema and codegen files regenerated.
- **Renderer:** `CampaignJourneyList` shows the string in place of the cards when `liveJourneyCards` is empty; with cards it shows the cards only. It renders only when the string has text, so a campaign created before this change just shows the heading as before.
- **Canvas:** the string is listed under the Journey list's "Campaign strings" and edits round-trip through `campaignStringUpdate`.
- **Tests/stories:** `CampaignJourneyList.spec.tsx`, `CanvasSection.spec.tsx`, string-count updates in the campaign API specs; stories for the empty state on the renderer (landing and region) and on the canvas.

Verification: touched specs in `libs/journeys/ui`, `apis/api-journeys` and `apps/journeys-admin` pass; `nx affected -t type-check` passes. `pnpm lint:changed` ran out of memory linting all of `apps/journeys-admin`, so I linted the changed admin files directly with a larger heap (clean).

🤖 Generated with [Claude Code](https://claude.com/claude-code)
