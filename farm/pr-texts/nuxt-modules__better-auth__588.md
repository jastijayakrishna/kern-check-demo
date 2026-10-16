# fix(types): augment Nitro 3 route rules through nitro/types

On Nuxt 5 (Nitro 3), an `auth` route rule in `nuxt.config.ts` fails typecheck with TS2353 once another module types its own rule on `nitro/types`. Nitro releases that re-export h3's `RouteRuleConfig` and `RouteRules` from `nitro/types` made the module augment those interfaces on h3/rules' resolved file path. When another declaration augments the same interfaces through `nitro/types` and loads first, TypeScript drops one of the two augmentations, and `auth` disappears from the type Nuxt checks `routeRules` against.

`selectNitro3RouteRulesTarget` now checks whether `nitro/types` exports `RouteRuleConfig` and `RouteRules`. If it does, the module augments them through `nitro/types`, the specifier Nitro documents for them. The augmentation still reaches code that imports from `h3/rules` directly, which was the reason for the file-path target in #490. Early Nitro 3 releases that declare `interface NitroRouteConfig` keep their `NitroRouteConfig`/`NitroRouteRules` target. Releases that alias the h3 types without re-exporting them keep the file-path target. Nitro 2 is unchanged.

The strict generated-declaration test has a new fixture where `nitro/types` re-exports the h3 interfaces and a second module augments `RouteRuleConfig` through `nitro/types`. It typechecks with that module loaded before and after ours, and checks that an invalid `auth` value is rejected. On main this fixture fails with TS2353. The test also resolves the temp dir with `realpathSync` so the path assertion passes on macOS, where `/var` is a symlink.

Validation:

- `pnpm exec vitest run test/nitro3-generated-declarations.test.ts test/module-compatibility.test.ts`: 21 passed. With only the `src/` change reverted, the new fixture fails on its `moduleName` assertion before it reaches the typecheck.
- `pnpm lint`: passed.
- `pnpm typecheck`: passed.
- `pnpm typecheck:runtime-server`: passed.
- `pnpm typecheck:playground`: passed.
- `pnpm prepack`: passed.
- `pnpm test`: 86 of 87 files passed, 635 tests passed and 52 skipped. `test/test-utils-e2e.test.ts` failed locally because the Playwright Chromium binary is not installed.
- Reproduction from the issue (`jd-solanki/reproductions@nuxt-better-auth-nuxt5-types--2026-10-13`, Nuxt nightly 5.0.0-2610111729, nitro 3.0.260903-beta) with this branch's packed tarball: `pnpm test` no longer reports the `nuxt.config.ts` TS2353 error. The only error left is the #578 `sendMail` error. With the #578 fix applied (`pnpm test:fix1`), the only error left is the #580 `user.role` error. A probe file checking `{ auth: 'user', robots: false }` against both `h3/rules` and `nitro/types`, with `@ts-expect-error` on invalid `auth` values, typechecks in `.nuxt/tsconfig.server.json` with the other module referenced before and after ours. In `.nuxt/tsconfig.node.json` the valid rule typechecks, but `auth` resolves to `any` there, so invalid values in `nuxt.config.ts` aren't rejected. That already happens on main: the type template imports the module's runtime types by an extensionless absolute path, which `nodenext` resolution can't resolve. It needs a separate follow-up.

Closes #579

🤖 Generated with [Claude Code](https://claude.com/claude-code)
