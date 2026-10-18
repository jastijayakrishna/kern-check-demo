# perf(chrome): the app shell stops shipping to routes that render none of it

Third fix from the "site feels slow again" RCA — and the one I had to attempt twice.

## The waste

`AppBar` (1,233 lines) and `Sidebar` (1,460 lines) plus three overlays shipped to every **chromeless** route — `/login`, `/signup`, the public credential pages, the assessment runner — because `AppChrome` imported them statically. Those routes render `<>{children}</>` and none of it.

## Why the obvious fix is wrong

Making `ChromeShell` itself `dynamic()` — my first attempt — delays `ChromeProvider` by a tick, so `MainLayout` renders its full non-nested layout and then collapses:

```
whole-shell dynamic : Tests 2 failed | 41 passed   (142s)
origin/main         : Tests 43 passed              (35s)
this PR             : Tests 43 passed              (8.2s)
```

It's also the shape that forced the **#1148 production revert**, where the `Box` geometry went with it and no ancestor was a scroll container any more — content past the viewport became unreachable.

## The narrower split

**`ChromeProvider` and every `Box` stay synchronous and static.** Only the five visual leaves are lazy, and they keep server rendering (the `next/dynamic` default), so the markup still arrives in the document and nothing flashes in. What changes is that a route which never renders `ChromeShell` never requests their chunks.

`DRAWER_WIDTH` moves to its own module. `AppChrome` needs only the number — to size the content column around the drawer — but importing it from `Sidebar.tsx` dragged all 1,460 lines back in and defeated the whole split. `Sidebar` re-exports it, so its six existing importers are untouched.

## Tests pin it in both directions

Both directions have already gone wrong here, so both are guarded — verified by reverting each:

| revert | fails |
|---|---|
| static `AppBar` import | "`./AppBar` is behind a dynamic import" |
| lazy `ChromeProvider` | "ChromeProvider is a static import" |

Plus an assertion that `overflow: "auto"` and `DRAWER_WIDTH` are still declared inline — the #1148 geometry.

## Verification

- `npx vitest run` — **874 passed** (62 files)
- `npx tsc --noEmit` — clean apart from the two pre-existing `tutorAutoContinue.test.ts` errors
- jobs-board suite, the one the first attempt broke: 43 passed in 8.2s

I'll measure the deployed `/login` chunk list after this lands — the baseline is 29 chunks / 1,713 KB decoded on agileology — rather than quote a local build number.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
