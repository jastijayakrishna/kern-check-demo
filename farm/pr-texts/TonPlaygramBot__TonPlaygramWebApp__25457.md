# Restore resolveFlagLabel in PoolRoyale to fix ReferenceError crash

### Motivation

- Pool Royale was crashing at runtime with `ReferenceError: resolveFlagLabel is not defined` when resolving player/AI flag labels, preventing safe return to the lobby.

### Description

- Add a `resolveFlagLabel` `useCallback` to `webapp/src/pages/Games/PoolRoyale.jsx` that converts regional flag emoji into a readable region string using `Intl.DisplayNames` when available.
- The function safely handles missing or non-regional inputs, returns `'Flag'` when no input is provided, and falls back to returning the original emoji on error. 
- The helper is defined before `playerFlagLabel` and `aiFlagLabel` usages so those hooks no longer reference an undefined symbol.

### Testing

- Ran `git diff --check` and no problems were reported. 
- Ran `npm run lint -- --no-ignore src/pages/Games/PoolRoyale.jsx` and the lint run completed without errors. 
- Ran `npm run build` (Vite production build) and the build completed successfully.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a91f10c8af0832992259b822897efd9)
