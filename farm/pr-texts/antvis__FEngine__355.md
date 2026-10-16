# fix: upgrade TypeScript to 5.2 to resolve @types/node ffi.d.ts syntax errors

`@types/node` (transitive dependency) uses the `using`/`await using` explicit resource management syntax introduced in TypeScript 5.2. TypeScript 4.x cannot parse this syntax — even with `skipLibCheck: true` — causing 50 syntax errors and a build failure in `father build` / `gulp-typescript`.

## Change

- Bumped `typescript` in `devDependencies` from `^4.1.3` → `^5.2.0`

TypeScript 5.x is backward compatible with the existing source. `@typescript-eslint@5.x` (used for linting) supports TypeScript up to 5.4.x, so no ESLint changes are needed.
