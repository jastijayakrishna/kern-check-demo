# chore: replace eslint with oxlint

## Why

The Dependabot TypeScript 7 bump (#128) has been failing CI since it opened. The cause is not the bump — it's ESLint:

```
peer typescript@">=4.8.4 <6.1.0" from typescript-eslint@8.65.0
Conflicting peer dependency: typescript@6.0.3
```

`typescript-eslint` reads type information by importing from `typescript` and calling into the compiler. TypeScript 7 is the Go-native port, and it has no stable programmatic compiler API until **TS 7.1** — so typescript-eslint [closed the TS 7 support request as "not planned"](https://github.com/typescript-eslint/typescript-eslint/issues/12518). Latest stable (`8.65.0`) and the canary (`8.65.1-alpha.19`, published 2026-07-30) both still cap at `<6.1.0`. This is months out, not weeks.

`oxlint` has **no `typescript` dependency at all** — both its peers (`vite-plus`, `oxlint-tsgolint`) are optional — so it never constrains the compiler version. It's already the linter in `sunday-spin-frontend` and `music-discovery-admin`, so this also brings the repo in line with that pattern.

## What changed

The old config extended `tseslint.configs.recommended` — the **non**-type-checked preset — so no type information was ever in use. Plain oxlint covers the whole config; the `oxlint-tsgolint` add-on isn't needed.

| Before | After |
|---|---|
| `js.configs.recommended` | built-in `eslint` rules |
| `tseslint.configs.recommended` | `typescript` plugin |
| `reactHooks.configs.flat.recommended` | `react-hooks/rules-of-hooks`, `react-hooks/exhaustive-deps` |
| `reactRefresh.configs.vite` | `react/only-export-components` (`allowConstantExport`) |

- Six devDeps removed (`eslint`, `@eslint/js`, `typescript-eslint`, `eslint-plugin-react-hooks`, `eslint-plugin-react-refresh`, `globals`), one added (`oxlint`).
- `eslint.config.js` deleted, `.oxlintrc.json` added.
- `exhaustive-deps` pinned to `"error"` — it's on by default in oxlint but only as a warning, and it was an error under the react-hooks preset. Pinning it avoids a silent severity downgrade.
- The disable comment in `AuthContext.tsx` moves from `react-refresh/only-export-components` to oxlint's canonical `react/only-export-components`. oxlint does honor the old name via a compat alias, but relying on a plugin name that's no longer installed is fragile.
- CI `Lint` step and `task lint` both switched to `oxlint`.

## Verification

- `oxlint` — 0 warnings, 0 errors across 72 files (39ms, vs multi-second ESLint runs)
- `vitest run` — 147 tests passed, 21 files
- `tsc -b --force` — clean

Confirmed oxlint isn't silently skipping files: control cases with a conditionally-called `useState`, an unused variable, and a `useEffect` missing a dependency were each caught.

**Separately verified `tsc -b --force` is clean under TypeScript 7.0.2** in an isolated checkout (with a deliberate type error as a control, to confirm the check was live). So #128 should go green once this lands — no source changes appear to be needed for TS 7 itself.

## Follow-ups (not in this PR)

- Rebase #128 and merge it.
- `tvbf-frontend` and `upcoming-movies-frontend` are both on typescript-eslint + TS 6.0.3 and will hit this identical wall when their TS 7 bumps arrive.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
