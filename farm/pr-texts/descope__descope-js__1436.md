# fix(react-sdk): clear isSessionLoading via setTimeout so it also fires in backgrounded tabs

## Related Issues
Fixes: https://github.com/descope/descope-js/issues/1433

## Description
#1395 deferred `setIsSessionLoading(false)` via `requestAnimationFrame` + `setTimeout(0)` so the clear lands in a render pass separate from `setIsSessionLoading(true)` (#1393). But rAF callbacks never run while the tab is hidden - e.g. a login page opened from an email magic link, or any load landing in a backgrounded tab - so the clear never executed. Since `fetchSession` is one-shot (`isSessionFetched` guard), nothing retried, and `useSession()` consumers hung on `isSessionLoading: true` forever.

The fix drops the rAF wrapper and keeps a plain `setTimeout(0)`:
- **still fixes #1393** - a macrotask is by definition a separate task, so the `true` update commits its own render before the `false` lands; consumers always observe the `true → false` transition even when `refresh()` short-circuits synchronously
- **fixes #1433** - `setTimeout` fires in hidden tabs (worst case ~1s background throttling), unlike rAF which is suspended entirely

`useSession` itself is untouched.

## Verification
- Reproduced the hang E2E with the [reporter's repro app](https://github.com/awilkowski-maxima/descope-repro) (production build, rAF suspended = backgrounded tab): both consumers stuck `isSessionLoading = true` before the fix, settle `false` after
- Foreground fresh-user path (the #1393 scenario, sync short-circuit): 6/6 clean boots with the fix
- New regression tests, verified against all three variants:

| variant | `defers the isSessionLoading clear to a separate macrotask` (#1393 guard) | `clears isSessionLoading even when requestAnimationFrame never fires` (#1433 guard) |
|---|---|---|
| rAF + setTimeout (old) | pass | **fail** |
| no deferral at all | **fail** | pass |
| setTimeout only (this PR) | pass | pass |

Full react-sdk suite: 81/81.

## Must
- [x] Tests
- [ ] Documentation (if applicable)

🤖 Generated with [Claude Code](https://claude.com/claude-code)
