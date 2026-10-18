# fix(app-blocks): tighten canonical manifest schema to match the validator (buildCommand allowlist + outputDir traversal) + drift guard

## What

Tightens the canonical published App Blocks manifest schema `public/schemas/app-block/v1.json` so it matches the imperative server validator (`src/server/services/block-manifest-validator.service.ts`) on the two config-as-code fields:

- **`buildCommand`** — `maxLength` 256 → **128**, and adds the allowlist `pattern` `^(?:(?:npm|pnpm|yarn) run [a-zA-Z0-9:_-]+|(?:npx )?vite build)$` (npm/pnpm/yarn `run <script>`, `vite build`, or `npx vite build`).
- **`outputDir`** — replaces the loose `^[^/].*` with an `allOf` of four `not`-pattern gates rejecting a leading `/`, backslash separators, a `..` path-traversal segment, and a Windows drive prefix.

Adds a drift-guard test `src/server/services/__tests__/build-command-outputdir.schema-drift.test.ts` that locks the schema to the validator's now-exported consts (`BUILD_COMMAND_RE`, `BUILD_COMMAND_MAX_LENGTH`) and asserts behavioral parity: for a table of buildCommand and outputDir values, the schema's verdict (property pattern/maxLength) equals the validator's field verdict. The two consts in the validator are now `export`ed (purely additive, no logic change).

## Why

This schema is not just documentation — the Go CLI (`civitai/cli`) and editor validation compile and evaluate it (santhosh-tekuri/jsonschema, RE2) to validate manifests client-side. The prior looseness meant `civitai app validate` could green-light `buildCommand`/`outputDir` values that the server later rejects at submit time. This change is superset-safe: it only **adds** constraints the runtime validator already enforces, so nothing that validated on the server can newly fail.

The one intentional divergence: the validator also rejects a NUL byte in `outputDir`; that impossible-in-a-manifest-string case is omitted from the schema for RE2 regex portability. The drift test documents this.

## ⚠️ Sequencing

**Merge this FIRST.** The SDK (`civitai-app-starters`) and the Go CLI (`civitai/cli`) byte-mirror this schema. Their companion re-vendor PRs must merge only **after** this change deploys to the live `https://civitai.com/schemas/app-block/v1.json` (served from the release branch) — until then their check-canonical-schema guards compare the mirror against the still-old live URL and would fail.

## Test

Targeted vitest run (drift guard + existing validator suite) — both green:

```
✓ build-command-outputdir.schema-drift.test.ts (30 tests)
✓ block-manifest-validator.service.test.ts (119 tests)
Test Files 2 passed (2) · Tests 149 passed (149)
```

🤖 Generated with [Claude Code](https://claude.com/claude-code)

