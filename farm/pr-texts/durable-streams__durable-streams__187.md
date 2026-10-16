# Durable-state tanstack db peer

Make `@tanstack/db` a peer dependency of `@durable-streams/state` to resolve TypeScript type incompatibility issues.

When `@durable-streams/state` and `@tanstack/react-db` both depend on `@tanstack/db`, TypeScript's nominal typing for private properties in `Collection` leads to type conflicts, even with the same `@tanstack/db` version. Making `@tanstack/db` a peer dependency ensures a single instance is used across the application, resolving these type mismatches.

---
<a href="https://cursor.com/background-agent?bcId=bc-ee760259-8597-49fa-840a-97724ce91b57"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-cursor-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-cursor-light.svg"><img alt="Open in Cursor" src="https://cursor.com/open-in-cursor.svg"></picture></a>&nbsp;<a href="https://cursor.com/agents?id=bc-ee760259-8597-49fa-840a-97724ce91b57"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/open-in-web-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/open-in-web-light.svg"><img alt="Open in Web" src="https://cursor.com/open-in-web.svg"></picture></a>

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **BREAKING**: `@tanstack/db` moved to a peer dependency for `@durable-streams/state` to ensure single-module TypeScript compatibility.
> 
> - Move `@tanstack/db` from `dependencies` to `peerDependencies` (add as `devDependency` for builds); bump to `^0.5.22` in dev and update lockfile
> - Add convenience re-exports from `@tanstack/db` in `src/index.ts` (e.g., `Collection`, `createCollection`, `eq`, `and`, `count`, etc.)
> - Update `README.md` installation to `pnpm add @durable-streams/state @tanstack/db` and note peer dependency requirement
> - Add changeset (`minor`) documenting the breaking peer dependency change and migration steps
> 
> <sup>Written by [Cursor Bugbot](https://cursor.com/dashboard?tab=bugbot) for commit da91e10fb841005e80ca344917663e35ed468081. This will update automatically on new commits. Configure [here](https://cursor.com/dashboard?tab=bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
