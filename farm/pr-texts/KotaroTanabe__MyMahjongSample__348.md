# fix: halt round after tsumo win

## Summary
- ensure win results are recorded immediately to stop further draws after tsumo/ron
- add regression test for tsumo not advancing the round
- stabilize timer-based tests and extend slow AI test timeout

## Testing
- `npm run lint --if-present`
- `npm run type-check --if-present`
- `npm run build`
- `npm test`


------
https://chatgpt.com/codex/tasks/task_e_689898c97604832a921b13ca1fe7ae5d
