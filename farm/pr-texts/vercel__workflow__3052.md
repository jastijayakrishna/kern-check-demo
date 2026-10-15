# Optimize `processImportSpecifier` by computing `shouldFollowImportsFromFile` once per file

### Description

`processImportSpecifier` was calling `shouldFollowImportsFromFile(filePath, forceFollowImports)` once for every import specifier in a file, even though the result only depends on `filePath` and `forceFollowImports`. Hoist that evaluation into `processFile` and pass the boolean result down:

- `processFile` now computes `shouldFollow` once before iterating specifiers.
- `processImportSpecifier` now accepts a `shouldFollow: boolean` argument instead of `forceFollowImports: boolean`.

```ts
// Before
await Promise.all(
  specifiers.map((specifier) =>
    processImportSpecifier(filePath, specifier, forceFollowImports)
  )
);

// After
const shouldFollow = await shouldFollowImportsFromFile(filePath, forceFollowImports);
// ...
await Promise.all(
  specifiers.map((specifier) =>
    processImportSpecifier(filePath, specifier, shouldFollow)
  )
);
```

### How did you test your changes?

- Ran the `@workflow/builders` test suite (`fast-discovery.test.ts` and related files pass).
- Verified the change with Biome lint/format on the modified file.

### PR Checklist - Required to merge

- [x] 📦 `pnpm changeset` was run to create a changelog for this PR
  - Use the correct semver bump type: `patch` for bug fixes, `minor` for new features, `major` for breaking changes.
  - Use `pnpm changeset --empty` if you are changing documentation or workbench apps
- [ ] 🔒 DCO sign-off passes (run `git commit --signoff` on your commits)
- [ ] 📝 Ping `@vercel/workflow` in a comment once the PR is ready, and above checklist is complete
