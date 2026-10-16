# feat(nuxt,vite,webpack): add `'nosource'` sourcemap option

### 🔗 Linked issue

resolves #23547

### 📚 Description

Adds `'nosource'` as a value for `sourcemap.client` and `sourcemap.server`. It generates sourcemaps that keep file names and line mappings but leave out the original source code (`sourcesContent`), so maps can be published without exposing the source.

```ts
export default defineNuxtConfig({
  sourcemap: { client: 'nosource' },
})
```

As suggested in the issue, this is implemented with the bundler option:

- **Vite (client + SSR):** `build.sourcemap: true` plus `rolldownOptions.output.sourcemapExcludeSources: true`. An explicit `vite.build.sourcemap` still takes precedence, as before.
- **Nitro:** `rollupConfig.output.sourcemapExcludeSources` when `sourcemap.server` is `'nosource'`.
- **webpack / rspack:** the `nosources-` devtool variants (`nosources-source-map` in production, `eval-nosources-cheap-module-source-map` for the client in dev, `nosources-cheap-module-source-map` for the server in dev).

Everything else reads the option as a boolean, so `'nosource'` behaves like `true` there.

**Verification:** I built the playground with `sourcemap: { client: 'nosource', server: 'nosource' }` and inspected `.output/public`:

| | `.map` files | maps with `sourcesContent` | JS referencing a map |
|---|---|---|---|
| `client: true` | 3 | 3 | 3 |
| `client: 'nosource'` | 3 | 0 | 3 |

Nitro already strips `sourcesContent` from server maps by default, so there's no visible server difference in the playground. The server option is set so `'nosource'` is respected consistently.

**Tests:** `packages/vite/test/sourcemap-options.test.ts` covers the Vite client and SSR config for `true`, `false`, `'hidden'` and `'nosource'`.

**Note:** it can't be combined with `'hidden'` yet. If that's wanted, a `'hidden-nosource'` value could follow webpack's naming.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
