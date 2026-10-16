# fix(core): require NoSerialize marker brand

### Motivation
- A recent change made the `NoSerialize<T>` phantom brand optional, allowing plain objects to be structurally assignable to `NoSerialize<T>` and removing a useful static guard that prevents accidental serialization of intended server-only state.
- At runtime Qwik only skips serialization for values recorded via `noSerialize()` (WeakSet) or carrying `NoSerializeSymbol`, so the weakened type could cause sensitive data to be leaked in SSR/q-data.

### Description
- Restore the required brand by changing the type alias to `export type NoSerialize<T> = (T & { __no_serialize__: true }) | undefined;` in `packages/qwik/src/core/shared/serdes/verify.ts` so plain `T` is not assignable without an explicit branded value.
- Add a focused type/regression unit test in `packages/qwik/src/core/shared/serdes/verify.unit.ts` that accepts `noSerialize()` output but uses `// @ts-expect-error` to assert a plain object assignment is rejected.
- Regenerate and update the public API/docs outputs (`packages/qwik/src/core/qwik.core.api.md`, `packages/docs/src/routes/api/qwik/*`, `packages/docs/src/routes/api/qwik/api.json`) to reflect the restored required brand.
- Add a patch changeset `.changeset/strong-noserialize-brand.md` describing the fix for `@qwik.dev/core`.

### Testing
- Ran `pnpm build.core.dev` and the dev build completed successfully after fixing the temporary test type issue.
- Ran the focused unit suite `pnpm vitest run packages/qwik/src/core/shared/serdes/verify.unit.ts` and all tests in that file passed.
- Ran `pnpm tsc.check` and the TypeScript check completed with no errors.
- Ran `pnpm api.update` to regenerate API docs and the update completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a5a3570b37c83319d98352894266a30)
