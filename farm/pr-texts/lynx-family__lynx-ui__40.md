# feat(lazy-component): add `unmountOnExit` alias and deprecate `unloadable`

### Motivation
- The prop name `unloadable` is ambiguous about the exact behavior (it reads like an adjective rather than an action triggered on leaving viewport), so a clearer name is needed while preserving backward compatibility.

### Description
- Add a new `unmountOnExit?: boolean` prop to `LazyComponent` and keep `unloadable?: boolean` marked as `@deprecated` in the types (`packages/lynx-ui-lazy-component/src/types/index.docs.ts`).
- Update runtime logic to prefer `unmountOnExit` and fall back to `unloadable` via `const shouldUnmountOnExit = unmountOnExit ?? unloadable`, and use `shouldUnmountOnExit` in the `disexposure` listener and render branches (`packages/lynx-ui-lazy-component/src/index.tsx`).
- Update documentation and examples to use `unmountOnExit` and note that `unloadable` is deprecated (`packages/lynx-ui-lazy-component/SKILL.md`).
- Add a changeset for the package (`.changeset/calm-badgers-teach.md`).

### Testing
- Ran `pnpm install` to ensure workspace deps were present and up to date, which completed successfully.
- Attempted `pnpm --filter @lynx-js/lynx-ui-lazy-component build`, which initially failed due to missing declarations from `@lynx-js/lynx-ui-common` when built in isolation (expected in a monorepo build order).
- Ran `pnpm --filter @lynx-js/lynx-ui-common --filter @lynx-js/lynx-ui-lazy-component build`, which succeeded and produced declaration files for both packages.

------
[Codex Task](https://chatgpt.com/codex/tasks/task_e_69b7df83c1c48331a9ed8a29734fb7ea)

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Added `unmountOnExit` prop to LazyComponent for configuring component behavior.

* **Documentation**
  * Updated documentation to recommend the new `unmountOnExit` prop; the `unloadable` option is now deprecated but remains supported for backward compatibility.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->
