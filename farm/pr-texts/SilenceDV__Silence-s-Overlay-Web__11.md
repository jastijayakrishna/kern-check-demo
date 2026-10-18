# Fix imported projects not being autosaved

### Motivation
- Imported JSON projects replaced the editor state but were not marked dirty, so the autosave pipeline never persisted them.
- Allow explicit control when replacing the in-memory project so imports and other programmatic replacements can opt into saving immediately.

### Description
- Add an optional `dirty?: boolean` flag to the `replace-project` `EditorAction` and accept it in the reducer to set `saveStatus` to `"dirty"` when requested.
- Update the `useEditorState` API to surface `replaceProject(project, dirty = false)` so callers can mark replacements dirty.
- Mark JSON imports as dirty in `components/editor/OverlayEditor.tsx` by calling `api.replaceProject(imported, true)` after a successful import so the existing autosave pipeline picks them up.
- Add a regression test in `tests/editorState.test.tsx` asserting that a programmatic `replaceProject(..., true)` sets `saveStatus` to `"dirty"`.

### Testing
- Ran type checking with `npm run typecheck` which completed without errors.
- Ran lint with `npm run lint` which completed successfully.
- Ran the test suite with `npm test` / `vitest run`, and all tests passed (`28 tests, 7 files` passed).
- Built a production bundle with `npm run build` which completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a67592bd3ec8321a6792244753ec46c)
