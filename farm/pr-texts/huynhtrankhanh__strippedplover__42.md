# Support Plover UI command events

### Motivation

- The headless engine cannot open UI for `{PLOVER:ADD_TRANSLATION}` and `{PLOVER:LOOKUP}` so hosts need a way to be notified when these commands are triggered.
- Tests and host integrations need an API to receive protocol events emitted by the engine.

### Description

- Handle `{PLOVER:ADD_TRANSLATION}` and `{PLOVER:LOOKUP}` in `handleEngineCommand` and emit a `plover_command` event with the command name and any trailing arguments preserved via `emitPloverCommandEvent`.
- Add `setEventSink(sink: ((event: Record<string, unknown>) => void) | null)` to allow tests and host integrations to intercept emitted events.
- Document the new `plover_command` event and its `arguments` field in `PROTOCOL.md` so hosts know the payload shape.
- Add a unit test in `src/engine.dictionary.test.ts` to verify `ADD_TRANSLATION` and `LOOKUP` produce the expected `plover_command` events.

### Testing

- Ran `npm test` and all test files passed (tests: 56 passed, 1 skipped). 
- Ran `npm run build` which completed successfully. 
- Verified repository checks with `git diff --check` returned no issues.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a61727c9310832e8038dfd968bb50fc)
