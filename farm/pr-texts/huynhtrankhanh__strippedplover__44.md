# Expose Plover add_translation and lookup events over STDIO

### Motivation
- Dictionary translations may request host-driven actions (`ADD_TRANSLATION` / `LOOKUP`) and the engine should expose only those host-handled events over the STDIO JSON-RPC stream so hosts can implement UI flows. 
- Keep other `{PLOVER:...}` commands as no-ops and avoid leaking extra internal events.

### Description
- Add a whitelist `EVENT_COMMANDS` containing `add_translation` and `lookup` and short-circuit handling in `handleEngineCommand` to emit events for those commands via a new `emitPloverCommandEvent` method in `src/engine.ts`.
- Emit events through the existing `eventSink` (default: write JSON to STDOUT) with the shape `{ event: "plover:<name>", command: "<name>", argument: "<raw-argument>" }`.
- Update `PROTOCOL.md` to document the two host-handled `{PLOVER:ADD_TRANSLATION:...}` and `{PLOVER:LOOKUP:...}` events and their JSON shapes.
- Update `README.md` feature list to mention the new Plover command events and remove the obsolete known-bug note.
- Add unit test `src/engine.dictionary.test.ts` that verifies only `add_translation` and `lookup` emit events and that unknown/unsupported commands do not.
- Add an e2e STDIO test `src/e2e/stdio.e2e.test.ts` to verify the events are emitted on the STDIO JSON line stream during translation.

### Testing
- Ran `npm test` (Vitest) which executed unit and e2e suites and completed successfully with all tests passing; overall result: `57 passed, 1 skipped` and all modified tests passed (including the new unit and e2e checks).
- The STDIO end-to-end tests confirming the emitted `plover:add_translation` and `plover:lookup` events passed.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a6175c062c8832e9457ae6ebdad501f)
