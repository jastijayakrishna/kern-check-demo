# feat(tsl)!: useRenderPipeline is owned by the component that configures it

`useRenderPipeline` gets an owner. The component that configures the pipeline owns it and frees it when it unmounts, instead of the pipeline living until someone calls `reset()`.

## Why

Before this change the pipeline was a singleton on the store with no owner:

- Unmounting an effect component left the effect rendering.
- `reset()` nulled the store but never called `RenderPipeline.dispose()`, and Canvas unmount never touched the pipeline. Pipelines leaked either way.
- Read-only calls (`useRenderPipeline()`) went through the same effect and could create the pipeline.
- A mount-time effect armed a rebuild, so every StrictMode mount and every Fast Refresh ran the callbacks twice and built a second scene pass. The docs said HMR skipped them.
- Callbacks read `store.getState()` from a layout effect, so callbacks reading a uniform the component's **parent** registers got `undefined` (React runs a child's layout effects before its parent's) and compiled `* null` into the shader. #4022 fixed the same ordering for readers in the component body; this fixes it for the callbacks.

## What changes (breaking)

- **Owners and readers.** A call with `mainCB`/`setupCB` owns a pipeline and scene pass of its own. A call without callbacks only reads; it never creates, keeps alive or frees anything. `reset()`, `rebuild()` and `clearPasses()` called from a reader act on the pipeline that is rendering.
- **Unmount frees.** The owner's pipeline and scene pass are released one task after cleanup, and the canvas goes back to `renderer.render()`. A StrictMode or Fast Refresh remount reclaims it first, so the graph is reused rather than rebuilt.
- **Stacking.** With two mounted owners, the most recently mounted one renders and a one-time dev warning names the overlap. When it unmounts, the previous owner takes over again with its own graph. Swapping `<Bloom />` for `<Blur />` in one commit works without a warning.
- **`{ persist: true }`** (third argument) keeps an effect rendering after its component unmounts, until another component configures the pipeline, `reset()`, or canvas unmount. A new owner frees unmounted persisted owners (deferred a task, so a persisted owner that is only re-running its effect in the same commit is not mistaken for unmounted). Canvas unmount frees every pipeline on the canvas through the TSL root extension's `dispose`.
- **Callback state matches the other TSL hooks.** Callbacks get the same `CreatorState` as `useNodes` creators, with staged entries included, and their reads are tracked as in `useLocalNodes`. A read resource that appears, is replaced or is removed re-runs them on the same scene pass; registrations they did not read change nothing.
- **Hot updates.** Every hot update in the app re-runs the callbacks on the same pipeline and scene pass, after the fresh resource generation has registered. A Fast Refresh reset of the owning component builds a new pipeline and frees the old one. `<Canvas hmr={false}>` turns this off.
- Each callback run registers its passes from scratch.

Not in scope: passes returned from callbacks are still not disposed by the hook (#3864).

## Example

`WebGPUMotionBlur` reads `blurAmount` from the callback state (registered by its parent, `Experience`) instead of a reader in the component body, and gains an `effect` toggle that mounts and unmounts the pipeline component.

## Docs

`render-pipeline.mdx` (ownership, `persist`, reading resources, HMR), `hmr.mdx`, the migration guide, the changelog, and the JSDoc on the hook and its types were audited against the behaviour above.

## Also in this PR: `state.gl` notice for apps that never read it

Separate commit (9a7640f3), in fiber core. @pmndrs/scheduler spreads root state into each frame state, which reads the `gl` getter. `isInternalRendererAccess` excuses that read by matching `'@pmndrs/scheduler'` / `'Scheduler.tickRoot'` in the caller frame, but Vite's dev server pre-bundles the package as `@pmndrs_scheduler.js` and renames the class `_Scheduler2`, so neither matched and every WebGPU app under Vite logged the deprecation on its first frame. The scheduler now registers each root with `stateForScheduler(state)`, a copy memoised per state object whose `gl` reads silently. Frame states keep `gl`; a deliberate read (drei's `OrbitControls` does `useThree((s) => s.gl)`) still warns.

## Tests

- New `packages/tsl/tests/useRenderPipeline-ownership.test.tsx` (17 cases): readers, unmount release, StrictMode reuse, stacking and hand-back, one-commit swap, `persist` (reader `reset()`, Fast Refresh reset, freed by a new owner, not freed while re-running its effect in the same commit), canvas unmount, hot update, `reset()` then a hot update, reader `rebuild()`, a parent-registered uniform, a late-registered uniform re-running on the same scene pass, and an unrelated registration causing no re-run.
- `packages/fiber/tests/gl-deprecation.test.tsx`: the scheduler's view carries `gl` without logging even when the stack check can't excuse the caller, with a control that the store's own state does log.
- `pnpm vitest run --dir packages/tsl`: 250 passed. `--dir packages/fiber`: 754 passed. `pnpm typecheck`, `pnpm build`, `pnpm verify-treeshake` and `pnpm verify-types` pass; ESLint and Prettier clean on the touched files.
- Browser (Chrome, real WebGPU device, Vite dev server) on this branch: `WebGPUMotionBlur` first load with the parent-registered uniform, the blur slider updating live, the effect toggle off and on, and a hot edit inside `mainCB` with the skinned Xbot. No errors; the old SkinningNode corruption did not reproduce. Before 9a7640f3 the console showed the `state.gl` notice from `_Scheduler2.tickRoot`; after it, the only notice is drei's `OrbitControls` reading `gl`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
