# fix(css): support namespace CSS Module imports

## Summary
- rewrite static namespace imports of CSS Modules to Vite's default locals export
- preserve Next.js's CommonJS CSS Module compatibility semantics for package styles
- cover the hybrid App + Pages production graph used by the failing fixture

## Next.js parity
Fixes both failures from `test/e2e/app-dir/scss/nm-module/nm-module.test.ts` in deploy-suite run 28143992598.

Next.js intentionally configures CSS Modules with `esModule: false` for backwards compatibility, so `import * as classes from "example/index.module.scss"` exposes the locals object directly. Vite exposes that object as the default export; without this compatibility rewrite the namespace access is undefined and the stylesheet is tree-shaken.

References:
- https://github.com/vercel/next.js/blob/v16.2.6/test/e2e/app-dir/scss/nm-module/nm-module.test.ts
- https://github.com/vercel/next.js/blob/v16.2.6/packages/next/src/build/webpack/config/blocks/css/loaders/modules.ts

## Validation
- `vp test run tests/css-module-imports.test.ts tests/scss-composes.test.ts` — 9/9
- focused `vp check` on touched files
- exact Next.js v16.2.6 deploy suite, concurrency 1 — 2/2

Excludes cacheComponents, PPR, resume, and fallback-shell work.

