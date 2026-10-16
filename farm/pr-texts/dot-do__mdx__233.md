# fix: add vitest.config.ts to packages with missing test configuration

# Fix missing vitest.config.ts files

This PR adds vitest.config.ts files to packages that were missing them, resolving the "No test files found" errors during test runs. The following packages have been fixed:

- @mdxe/test
- @mdxe/esbuild
- @mdxui/reveal
- @mdxui (root package)

## Testing

All tests now pass successfully when running `pnpm test` in each package directory. The configuration matches the standard pattern used in other packages in the monorepo.

## Link to Devin run
https://app.devin.ai/sessions/ec7d727cad7b4defae436ad66d61bdcb

Requested by: Nathan
