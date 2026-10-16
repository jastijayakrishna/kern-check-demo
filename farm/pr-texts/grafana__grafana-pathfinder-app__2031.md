# feat(kiosk): make the exit button label configurable

## Summary

Change the kiosk exit button from “Back to Grafana” to “Skip this and show all options”. Catalog authors can override the visible label and accessible name through the top-level `exitButtonLabel` JSON field in legacy and structured catalogs.

## What to look at

- Catalog loading validates and trims the optional label to 1–200 characters. Invalid labels use the existing catalog fallback flow.
- The overlay renders the label as plain text and preserves click, Escape, focus, and telemetry behavior.
- The authoring documentation and exported JSON schema include the new field; existing browser tests use the new default label.

## Why

Use the requested skip wording by default and let each kiosk catalog customize its exit copy through JSON.

## How to verify

1. Open a kiosk without `exitButtonLabel` and confirm the button reads “Skip this and show all options”. Click it and confirm the kiosk closes.
2. Add `"exitButtonLabel": "Explore all options"` to a legacy or structured catalog. Confirm that text appears as the button label and accessible name, and Escape still closes the kiosk.
3. Supply an empty, whitespace-only, non-string, or overlong label and confirm the kiosk uses its existing catalog fallback flow.
4. Supply a label containing HTML markup and confirm it appears as literal text.

## Validation performed

59 focused tests passed across the kiosk overlay, catalog loader, and kiosk schema. TypeScript checks, targeted ESLint, CLI build, formatting, and diff checks passed. Browser tests were updated but not run; the full pre-merge gate was not run locally.

## Breaking changes

Existing catalogs require no changes. Deploy renderer support before adding `exitButtonLabel` to structured catalogs: older renderers reject unknown top-level fields. The default accessible button name changes, so consumers querying the old name need to update.

## Reversibility

Reverting restores the old default label. Remove `exitButtonLabel` from structured catalogs before rolling back to a renderer that rejects this field.

🤖 Generated with Codex
