# Address review feedback: extract modules, clean up imports

## Summary

Follow-up to #90514 addressing review feedback from @lukesandberg:

- **Extract webpack layer helpers to `webpack-layer.ts`**: Moves `shouldUseReactServerCondition` and `isWebpackAppPagesLayer` out of the large `utils.ts` into their own module, reducing transitive dependencies pulled into `swc/options.ts` (reverts the revert from the previous PR)
- **Restore top-level import of `throwTurbopackInternalError`**: The lazy `require()` in `swc/index.ts` was unnecessary since `createProject` is always called — restores the simpler top-level import
- **Remove dead `getSupportedBrowsers` re-export from `utils.ts`**: All importers already import directly from `get-supported-browsers.ts`, so the re-export was unused
- **Extract `formatIssue` and `isRelevantWarning` to `format-issue.ts`**: Moves these functions (and their private helpers) out of the large `turbopack/utils.ts` into a dedicated module, so `print-build-errors.ts` doesn't pull in all of `turbopack/utils`

## Test plan

- `pnpm --filter=next types` passes
- Unit tests for `formatIssue` pass (`utils.test.ts` updated to import from new module)
- NFT test expectations updated for the changed module graph
