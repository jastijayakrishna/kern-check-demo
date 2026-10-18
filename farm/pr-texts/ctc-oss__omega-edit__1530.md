# fix: show empty file state in data viewport

## Summary

Shows an explicit empty-file status after the data editor successfully opens a zero-byte file. The existing preparing/loading state remains unchanged, so the viewport no longer waits indefinitely while still distinguishing “not loaded yet” from “loaded with no data.” English and Spanish labels are included.

## Background

The preview grid currently uses an empty row set for both loading and valid zero-byte files, leaving empty files stuck on “Waiting for data.”

Closes #1528

## Changes

- derive a loaded-empty flag from the resolved file size in `EditorWorkspace`
- pass the flag into `PreviewGrid` while keeping its default waiting state
- add localized `Empty file` / `Archivo vacío` labels
- extend the compiled-entrypoint regression test to cover the new state wiring

## Testing

From `vscode-extension`:

- `npm run lint` — passed
- `npm run compile` — passed; Svelte check reported 0 errors and 0 warnings
- `npm run test:unit` — 10 passed
- `git diff --check` — passed

## Additional Notes

`PreviewGrid` remains behind the existing `preparingFile` branch until the first viewport response, so an initial `fileSize` of zero cannot be mistaken for a loaded empty file.
