# Run timelines as synchronous generators

## Why

The async runtime only advances when the event loop runs. Measured on v0.3.10 with three one-tick actions A→B→C (each `update` returns `false`):

- 6 synchronous `update()` calls in one loop (fixed-step sub-stepping, headless tests, benchmarks): `A A A A A A`. The finished action keeps being called and the timeline never advances.
- 6 calls with a macrotask between them: `A B C C C C`.

`timePassed` also used `setTimeout` (wall clock), so pausing, time scaling, slow frames and fast headless runs got out of sync.

Timelines are now plain synchronous generators (`function*`) stepped only by `update(state, delta)`. They are deterministic: the same sequence of deltas always produces the same behaviour. The A→B→C case now gives `A B C` across three updates.

## The step rule

Each `update` delivers one frame. A `TimelineRunner` hands the frame to the current action, which reports one of:

- `running`: it used the frame and continues.
- `finished`: it used the frame and is done. The timeline advances right away in the same update: the code between yields and the next action's `init` run now, and the next action's first update happens on the next frame.
- `skipped`: it was already done when the frame started (its `until` was met), so the frame passes to the next action within the same update. No frames are lost.

`parallel` steps each child once per frame in the given order. When a race is won, the other branches are cancelled through generator `return()`, so their `finally` blocks and `init` cleanups run synchronously. If more than 10,000 actions skip within one frame, the runner throws an error that names the likely cause (e.g. `while (true) yield* action({ until: () => true })`).

## Breaking changes and migration

- `async function*` → `function*`. `yield*`, `action`, `parallel`, `graph`, `switch_`, queues and sub-timelines read the same.
- The types are Generator-based: `NonReuseableTimeline<T, R> = Generator<TimelineYield<T>, R, unknown>`, and `TimelineYield` is the per-frame step function. `runTimelineAsync` and `abortSignalToPromise` are removed.
- `until` accepts a condition `(state, clock, actionTime) => boolean`, checked at the start of every frame, or a Promise. A Promise is observed through a flag, so the action notices it on the next frame at the earliest (at most one frame of latency). Use promises for external events and conditions for sequencing inside the simulation.
- `timePassed(n, unit)` counts simulation time (the sum of deltas) and returns a condition. `action({ until: timePassed(1, 'seconds') })` reads the same as before. `forever()` returns a condition too.
- Graph `whenUpdate` and `doWhile` take conditions that are checked at the start of the frame, with `actionTime` being the time before that frame. Docs that used `whenPromise: () => timePassed(...)` now use `whenUpdate: timePassed(...)`.
- `QueueTimeline.waitUntilNotEmpty()` returns a condition.
- `onError` is removed: errors propagate synchronously out of `update()`. In React they throw out of `useFrame`. An error thrown by an action's update is thrown into the generator at its `yield`, so a timeline can `try/catch` around `yield* action(...)`.
- `init` is synchronous only (`() => Cleanup | void`); returning a promise throws. Async setup waits first: `yield* action({ until: load() })`, then an action with a sync `init`.
- `SynchronousAbortController` / `SynchronousAbortSignal` are removed: the native `AbortController` already dispatches `abort` synchronously, so cleanups run before `abort()` returns.
- `scope` is removed: `try { yield* ... } finally { ... }` binds a resource to a timeline's lifetime, and the `finally` runs synchronously on cancellation.
- Removed deprecated APIs: `start`, `useTimeline`, `useTimelineGraph` (use `useRunTimeline(() => graph(...), deps)`) and graph `when`.
- `TimelineClock` gains `frame`, which `runTimeline` increments once per update. Code that calls `TimelineRunner.step` with its own clock must supply and increment it. `prevDelta` is typed `number` (it starts at `0`).

## Behaviour changes

- Momentum handoff between consecutive actions on the same target now works. Before, `transition` and `offset*` checked `memo.prev === null` against a `{}` memo, so the handoff never happened. For example, `velocity(1)` right after `velocity(10)` now starts at 10 u/s. The handoff is frame-based: a value is only taken over if it was stored by the same timeline in the immediately preceding update, with no wall clock involved. Eases ignore a `prevDelta` of `0`.
- `timePassed` tolerates floating-point error, so 0.1 s at 60 Hz takes 6 frames, not 7.
- The `parallel()` function with no timelines (e.g. all entries `false`) returns at once. An empty `ParallelTimeline` / `<Parallel>` waits until a child is attached.
- `unattach` on a running race no longer ends the race.
- `ParallelTimeline.attach` of an already-attached timeline throws.
- The loop that combines several `update` functions in one action is rewritten with no behaviour change: the first update that returns a boolean decides.

## Known limitations / follow-ups

- The loop guard cannot catch a generator that loops without ever yielding (inherent to synchronous generators).
- `velocity()` returns NaN when a frame has `delta = 0`. This is pre-existing and also on main; it should be a separate fix.

## Testing

New and rewritten vitest suites (42 tests), all synchronous except the promise cases:

- **Runner:** the A/B/C synchronous loop gives `A B C`; code after a finished action runs in the same update; skipped frames are handed on; the loop guard throws; errors propagate out of `update` (with cleanups) or are caught in the timeline; cancelling through a native `AbortController` (cleanups run before `abort()` returns), from inside an update and from inside the timeline; already-aborted signals; `abortable`.
- **Action:** `init` and cleanup order; `init` returning a promise throws; action time; `timePassed` table (seconds, milliseconds, float tolerance) in simulation time; a promise `until` is observed on the next update; a rejected promise throws.
- **Parallel:** race cancellation runs `finally` blocks and cleanups synchronously; `all`; `false` branches; nested cleanups; `doUntil` / `doWhile` frame-exact; an empty function form vs. an idling container; double `attach` throws; errors in children.
- **Graph:** `whenUpdate` hands the frame to the next state; `whenUpdate: timePassed` runs a state for exactly its duration; `whenPromise`; `finally`; `setState`. Also `switch_` and `QueueTimeline.waitUntilNotEmpty`.
- **Other:** `ReplacableTimeline` restart and cancel; frame-based `previous` handoff; eases with `prevDelta` 0.

Commands run: `tsc --noEmit` (both packages and the three examples), `pnpm -r check:eslint`, `pnpm -r check:prettier`, `pnpm test`, `pnpm -F './packages/**/*' build`, `pnpm docs:test`. The overview page was regenerated with `scripts/generate-overview.mjs` and formatted with prettier.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
