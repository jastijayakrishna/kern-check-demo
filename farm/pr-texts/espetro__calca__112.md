# fix(canvas): render a failure card for failed/empty frames

## Summary

Generations that failed (rejected frame, stream error, or a model returning empty output — the white boxes in the report) were written as tiny gray text inside the frame iframe (`<div style="padding:32px;color:#666">⚠ …`). At canvas zoom that renders as an unexplained white box — users can't tell anything failed.

Iterations now carry `status: "error"` and `DesignFrame` renders a real failure card instead: ⚠ icon + "Failed to generate" + "Check Settings or try again" (localized via `frameErrorTitle`/`frameErrorHint` passed through `CalcaCanvasContext` → node data → `DesignFrame`). The RF node is sized to the card (140px), and error frames no longer persist as zombies — `html: ""` fails the `it.html && !isLoading` persistence filter.

- `packages/pipeline` `errorFrame` → `html: ""` (client marks the iteration failed)
- `use-workflow-stream` all 3 error paths → `status: "error", html: ""`
- `DesignFrame` `isError` also covers legacy placeholder cards already in storage and empty-html frames without the flag — older sessions get the new card too.

## Related Issues

User report: "some generations are shown as just a white box — the user can't tell what's going on."

## Type of Change

- [x] Bug fix

## Checklist

- [x] `bun run validate:quick` green (manifests, typecheck, lint, format)

## License Acknowledgment

I have read and agree to the CLA; contributions are original; relicensing rights granted.

Link to Devin session: https://app.devin.ai/sessions/27b62ea1e5564bd0bc5b1a7b3d925bb7
Open in Devin Desktop: https://app.devin.ai/desktop/session/27b62ea1e5564bd0bc5b1a7b3d925bb7?variant=devin
Requested by: @espetro
