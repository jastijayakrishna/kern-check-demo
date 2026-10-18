# fix(fastify-api-reference): bundle frontend assets

`@scalar/fastify-api-reference` read its 3.4MB standalone script from disk at runtime, using a path relative to `import.meta.url`. That works in dev and from `node_modules`, but breaks the moment a consumer bundles their Fastify app (e.g. into a Docker image) — the asset is no longer next to the compiled plugin and the read throws.

This swaps the `tsc + copy:standalone` build for a Vite/Rolldown library build (matching the `nextjs` integration) that **inlines the standalone script into the output at build time**. The result is a self-contained, bundler-safe plugin.

- `getJavaScriptFile()` now returns a build-time-inlined string instead of doing `fs.readFileSync`
- `vite.config.ts`: lib build with a small plugin that inlines `@scalar/api-reference`'s `standalone.js`; `vite-plugin-dts` emits types
- dropped `copy:standalone`/`shx` and the now-dead `tsconfig.build.json`

## Verification

Bundled a Fastify app that registers the plugin into a single relocated file with esbuild (a Docker-style build) and ran it from a directory with no `node_modules`:

- HTML route → `200`
- JS route → `200 application/javascript`, 3,576,806 bytes (the full inlined standalone)

All 46 package tests pass; type-check, Biome, and knip are clean.

## Ticket

Closes #3566

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Medium Risk**
> Changes the published artifact and build path for a ~3.5MB inlined asset; runtime behavior for consumers who bundle the app should improve, but build order and package size/output shape shift.
> 
> **Overview**
> **`@scalar/fastify-api-reference`** no longer ships a copied `standalone.js` beside the plugin or reads it from disk in published builds. The build pipeline is now **Vite lib build → TypeScript declarations only**, replacing the old **`tsc` + `copy:standalone`** flow.
> 
> At **`vite build`**, a custom plugin replaces **`getJavaScriptFile`** with a module that returns the **`@scalar/api-reference`** standalone script as an inlined string (via **`?raw`**). Dev and tests still use the source implementation, which resolves the standalone file through **`@scalar/api-reference`** and reads it with **`fs`**.
> 
> **`tsconfig.build.json`** now uses **`emitDeclarationOnly`** so JS comes from Vite while types stay on **`tsc`**. Rolldown keeps package dependencies and **`node:`** builtins external; only the standalone asset is embedded in **`dist/index.js`**.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit 6c9edcba42e4b869244d2310935c4a58a63e70db. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
