# feat(json-renderer): share the field descriptor and widget rule pipeline

## Summary

Two things, both prerequisites for the rest of phase 2 of constructive-io/constructive-planning#1822.

**1. `@fbp/evaluator` floor.** `flow-to-blocks` allowed `^1.3.0`, and 1.3.0 is permanently uninstallable (it shipped `"@fbp/types": "workspace:*"`). Floor raised to `^1.5.0`, which also lets the temporary workarounds go: the `"@fbp/evaluator>@fbp/types"` override in `pnpm-workspace.yaml` and the matching override in the packed-consumer check.

**2. `form-resolver-core`.** The field → node rule pipeline lived inside `json-schema-to-blocks`, so `meta-to-blocks` (and later HITL task forms / function inputs) would each fork their own copy of decisions like "`format: uri` renders as a file picker". It now lives in `json-renderer/rules` as a source-neutral layer — still no React, no `@constructive-io/*`, and no Constructive widget names in the generic package:

```ts
interface FieldDescriptor<TType> {
  name; path; required;
  dataType?; format?; label?; description?;
  enumValues?; nullable?; readOnly?; defaultValue?;
  constraints?: NodeConstraints;
  hints: FieldHints<TType>;   // the x-ui shape, generalized
}

composeWidgetRules(defaults, rules?, replaceDefaults?)  // caller rules first
applyWidgetRules(descriptor, rules, fallbackType)       // first match wins
fieldNodeProps(descriptor)                              // shared field props
compareFieldOrder(a, b)                                 // hints.order, else source order
```

`json-schema-to-blocks` keeps every one of its exported names and now specializes rather than duplicates:

```diff
-export interface FieldContext { schema; name; path; required; type?; ui; resolve }
+export interface FieldContext extends FieldDescriptor<UINodeType> { schema; type?; ui; resolve }
-export interface WidgetRule { ... }
+export type WidgetRule = CoreWidgetRule<FieldContext, UINodeType, UINode>;
```

So a rule matches on `ctx.dataType`/`ctx.format`/`ctx.enumValues`/`ctx.constraints` when the decision is source-neutral (those rules will work verbatim against a `_meta` column), and still reaches into `ctx.schema` for genuinely schema-specific keywords like `multipleOf`. `ctx.ui` stays as an alias of `ctx.hints`, so existing app rules keep compiling.

No behavior change intended: the 23 existing conversion tests pass untouched (`x-ui`, required/disabled/readOnly, defaults and `const`, constraints, enums, recursion, variants, ordering, `$ref` cycles), plus 14 new tests for the generic helpers.

## Verification

`pnpm build`, `pnpm lint:types`, `pnpm test`, `pnpm check`, `pnpm pack:check` all green under Node 24 / pnpm 10.28.0 (installed directly, not through corepack — a corepack shim resolves `pnpm` per-directory, so `pack:check`'s throwaway consumers outside the workspace got pnpm 11 and failed on `ERR_PNPM_IGNORED_BUILDS: esbuild`). CI installs pnpm via `pnpm/action-setup`, so it is unaffected.


Link to Devin session: https://app.devin.ai/sessions/027937d092794c92a31c6ee49c513f59
Requested by: @pyramation
