# feat(templates): add Next.js templates (JavaScript + TypeScript)

## Summary

Adds two templates — **`nextjs`** (JavaScript) and **`nextjs-ts`** (TypeScript) — that scaffold a [Next.js](https://nextjs.org) App Router app running on Harper via [`@harperfast/nextjs`](https://github.com/HarperFast/nextjs). Because the app runs *inside* Harper, server actions and server components read and write tables directly through the injected `tables` global — no separate API server and no network round-trip.

They slot in as a new **Next.js** framework family in the interactive picker and `--template` flag.

## What the templates are

A **bare starter** at the same altitude as the existing `vanilla`/`react`/`vue` templates — not a full app. The only Harper touch is a **counter persisted in a `Count` table**: a server component reads it, and a `<form action>` server action increments it. That shows the one thing unique to Next-on-Harper (server-side `tables` access) while staying minimal and safe — single known-key record (no scans), non-destructive (no delete), no user input (no validation surface).

```
schema.graphql            # a single Count table
app/page.(tsx|js)         # server component: reads the count, renders a form-action button
app/actions.(ts|js)       # getCount / increment via the `tables` global
app/layout.(tsx|js)       # minimal root layout
config.yaml               # graphqlSchema + @harperfast/nextjs (prebuilt: true)
next.config.mjs           # withHarper({})
harper.d.ts               # (TS) ambient types for the `tables` global
```

Catalog wiring: `lib/constants/templates.js` + `.d.ts`, `frameworks.js` (new family + color), `templates.test.js`, `package.json` `files`, and the root README.

## Key decisions (a few are non-obvious — details below)

- **Use the injected `tables` global; do _not_ `import 'harper'` in server code.** A top-level `import 'harper'` breaks the production build (Turbopack can't resolve it, and even under webpack it opens the DB during Next's build-time page-data collection). This matches the plugin's own `next-16` fixture.
- **Deploy prebuilt (`prebuilt: true` + build-first scripts).** On a multi-threaded cluster the plugin's on-startup build races across worker threads and 404s (see below); shipping a prebuilt `.next` avoids it. Verified on a stage cluster.
- **Schema-only config** (`graphqlSchema` + the plugin). The plugin owns HTTP routing, so there's no `static`/`rest` handler.
- **`studio: false`.** No Studio template package is built/published for these (new optional catalog flag → derived `studioTemplateNames`). Studio's edit-in-place model also doesn't fit Next.js (verified — see below).

## Validated on a real stage cluster

- **Deploy without a build → 404s** (multi-thread build race).
- **Prebuilt deploy → serves**; the counter reads *and* writes live (confirmed in-browser).
- **Editing a file in the Studio editor + Restart → no effect** for a prebuilt app (and a rebuild would just re-trigger the race).

Root cause filed upstream as **HarperFast/nextjs#52** (concurrent `next build` across worker threads → `ENOENT` on `.next/BUILD_ID`), with `@harperfast/vite`'s `withBuildLock` as the fix to port. Also filed **#51** (Turbopack can't resolve `import 'harper'`) and a repro on **#37** (build vs. RocksDB lock).

## CI coverage

Both variants are in the `integration.yaml` matrix across **npm / yarn / pnpm** (scaffold → install → lint → format → build → runtime smoke). This caught real package-manager issues the npm-only path hid:

- `typescript` must be a devDependency even in the JS template (`eslint-config-next` → `typescript-eslint` requires it; npm hoists it, yarn/pnpm don't).
- pnpm 11 needs `allowBuilds` in `pnpm-workspace.yaml` (it removed `onlyBuiltDependencies`) or `pnpm install` fails on Next's native build-script deps.
- `run test` is now conditional (these templates ship no unit tests; existing templates unchanged).

A dedicated `template.tests/nextSmoke.js` boots the app under Harper (multi-threaded) and asserts it serves `/` and renders the Harper-backed counter — since the Next.js apps route through the plugin and have no REST resource surface for the existing `runtimeSmoke.js`.

## Follow-ups (not blocking)

- Once **#52** lands (plugin coordinates the multi-thread build), drop `prebuilt: true` and let the server build on deploy — simplifying the scripts.
- Revisit `studio: true` if/when the plugin works in Studio's deploy-only model; first-time publish perms + npm provenance for the two studio packages are also prerequisites.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
