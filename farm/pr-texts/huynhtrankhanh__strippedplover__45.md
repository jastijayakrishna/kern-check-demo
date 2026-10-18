# Emit plover:configure for {PLOVER:CONFIGURE} translations

### Motivation
- Allow dictionary translations to request a host-driven configure action the same way `{PLOVER:ADD_TRANSLATION}` and `{PLOVER:LOOKUP}` already do, so hosts can handle `{PLOVER:CONFIGURE:...}` requests.

### Description
- Add `configure` to the engine's host-handled command set by updating `StrippedPlover.EVENT_COMMANDS` in `src/engine.ts` so `{PLOVER:CONFIGURE:...}` emits a `plover:configure` event.
- Extend unit tests in `src/engine.dictionary.test.ts` to assert `CONFIGURE:machine` produces `{ event: 'plover:configure', command: 'configure', argument: 'machine' }` alongside existing events.
- Extend the STDIO end-to-end test in `src/e2e/stdio.e2e.test.ts` to include a `{PLOVER:CONFIGURE:machine}` translation and verify the asynchronous STDOUT event and response ordering.
- Document the new host-handled command in `README.md` and `PROTOCOL.md`, including an example `plover:configure` event payload.

### Testing
- Ran the targeted test suite with `npm test -- --run src/engine.dictionary.test.ts src/e2e/stdio.e2e.test.ts` and the command completed with all tests passing.  
- The modified unit and e2e tests exercised the new `plover:configure` emission and succeeded.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a617aea32d8832e922af53df84a10e0)
