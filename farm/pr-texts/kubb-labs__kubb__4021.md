# feat(studio): report peer dependency versions

### Motivation

- Report which plugin packages and versions are actually installed (and which are missing) when a generation finishes so Studio can display resolved dependency information.
- Use package resolution of configured plugin package names and expose the results as peer-style dependency data instead of the previously described resolved-dependency approach.

### Description

- Extend the Studio protocol so the `kubb:generation:end` payload includes `peerDependencies: Record<string,string>` and `missingDependencies: Array<string>`.
- Add resolution logic in `packages/studio/src/ws.ts` that deduplicates plugin names, resolves each plugin's `package.json` via `require.resolve`, reads the `version`, and aggregates missing entries when resolution fails.
- Include the resolved `peerDependencies` and `missingDependencies` in the `agent:data` message emitted for `kubb:generation:end` and update the WebSocket stream behavior accordingly.
- Add a unit test in `packages/studio/src/ws.test.ts` that asserts installed-version reporting and missing-package detection, and add a `.changeset` to release `@kubb/studio` as a minor version.

### Testing

- Ran repository pre-checks (`git diff --check`) and staged the modified files for commit, then committed the changes successfully.
- Added a Vitest unit that covers the new reporting behavior in `packages/studio/src/ws.test.ts`, but the test was not executed in this environment.
- Attempted to run `pnpm --filter @kubb/studio test` and typecheck, but the environment could not download the required `pnpm` binary so tests and typecheck did not run here.
- Created a changeset (`.changeset/tidy-ants-report.md`) to publish the change to npm as a minor release for `@kubb/studio`.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6aa5c0c48cdc83239fde65f691dd4a29)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Generation results now display installed plugin versions.
  * Missing plugin dependencies are identified and reported in generation results.
  * Generation-end event data now includes dependency information for integrations.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
