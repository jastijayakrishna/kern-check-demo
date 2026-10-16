# Update generated API code from staging

## Summary
Regenerates the API client from the staging OpenAPI schema (`yarn generate-types staging` + `PUBLIC_TERRAWARE_API=https://staging.terraware.io yarn generate-queries`).

API changes:
- **New endpoint** `POST /api/v1/tracking/sites/{id}/completeSurvivalRateCalculation` (`maxWaitSeconds` query param) → new `useCompleteSurvivalRateCalculationMutation` in `plantingSites.ts`.
- **New endpoint** `POST /api/v1/tracking/draftSites/boundaryFile` (`parseDraftPlantingSiteBoundary`) plus `ParseDraftPlantingSiteBoundaryResponsePayload`, `BoundaryFileProblemPayload`, `GeometryFileErrorCode` in `generated-schema.ts` (`draftPlantingSites.ts` already had these).
- **New field** `pending: boolean` on `ObservationResultsPayload`, `ObservationStratumResultsPayload`, `ObservationSubstratumResultsPayload`, `ObservationMonitoringPlotResultsPayload` in `generated-schema.ts`.
- `UploadPlotMediaRequestPayload.isOriginal` now defaults to `true` (doc changed accordingly); `substratumName` doc wording changed.

Removed `rtk-codegen.config.ts` entries (staging has no matching endpoints):
- `./src/queries/generated/clock.ts` (`/api/v1/seedbank/clock`)

The `GeometryCollection` type in `src/queries/generated/` (`draftPlantingSites.ts`, `observations.ts`) was intentionally kept at its existing definition and position; the generator would otherwise have changed it to `geometries: object[]`.

Checks:
- `yarn ts`: passes
- `npx prettier --check rtk-codegen.config.ts src/api/types/generated-schema.ts src/queries/generated`: passes

Link to Devin session: https://app.devin.ai/sessions/c27cf9b21cac4434b60e4e7eb5a6a630
Open in Devin Desktop: https://app.devin.ai/desktop/session/c27cf9b21cac4434b60e4e7eb5a6a630?variant=devin
Requested by: @sgrimm
