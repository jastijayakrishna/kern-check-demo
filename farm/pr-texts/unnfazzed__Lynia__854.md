# fix(mobile): a boot step that throws must not kill the launch (MOB-BOOT-04) + RCA

## What & why

Internal-track builds **#31** (`a80e1456`, v0.43.0) and **#32** (`f89ce9a7`, v0.45.1) install and then die on every cold start — *"LyniaGo keeps stopping"*. This carries the RCA (`docs/COLD-START-CRASH-RCA-2026-08-21.md`, ledger `MOB-BOOT-04`) and the fix for the part that turns a fault into a dead app.

**Owner evidence narrowed it decisively:** *"I see the green splash screen but it crashes after that."* The splash is painted by the Activity theme and cannot appear unless `Application.onCreate` already completed — so `SoLoader`, `DefaultNewArchitectureEntryPoint.load()` and `libappmodules.so` all succeeded. The native entry-point candidate is **refuted**. What remains is a fatal during React instance creation or JS bundle evaluation, and instance creation was independently refuted on R8 grounds (`proguard-android.txt` still emits `-dontoptimize` on AGP 8.6.0).

### The structural defect — this is ours, not a vendor's

expo-router evaluates `app/_layout.tsx` **eagerly** while building the route tree (`getRoutes()` calls `loadRoute()` for every `_layout`), and the `Try` boundary that catches render errors for the whole app is built *from* that load — so it cannot catch it. `Sentry.wrap` is not a boundary; `registerRootComponent` adds one only in dev. **A synchronous throw anywhere in that module graph is a process kill, not an error screen.**

So this PR fixes the *fatality*, not one guess at the *fault*. A dozen statements could be the one that throws; guarding the block covers all of them.

- **`src/telemetry/sentry.ts`** — the SDK is no longer a top-level import. Its entry re-exports `./tracing` and `./replay/CustomMask`, which between them make three unguarded module-scope `UIManager.hasViewManagerConfig()` calls. Under Paper that resolved to `PaperUIManager`, which wrapped the native lookup in a `try/catch` that logged and returned `false`. Under the New Architecture it resolves to `BridgelessUIManager` → `unstable_hasComponent`, which **throws**, with no catch on either side. The same three lines that could not crash #30 are fatal in #31. Now `require`d lazily behind a guard — the pattern `analytics.tsx` already uses for PostHog — with `init`, `wrap`, `captureException` and `addBreadcrumb` guarded too. Crash-handler timing is unchanged; only the failure behaves differently. A build with no DSN never evaluates the SDK at all.
- **`app/_layout.tsx`** — every module-scope boot call (`initSentry`, `preventAutoHideAsync`, `setOptions`, `prewarmFonts`, `prewarmBootReads`) runs through a `bootStep` guard that reports via `captureException` and continues. None is a correctness precondition: fonts fall back to the system face, prewarm's consumers call it again from their own effects, the splash hides on first paint regardless. **A degraded boot beats no boot.**

**Review caught a real hole in the first version of that fix, worth calling out** because it is the same class of bug: `bootStep` hands the caught error to `captureException`, so an *armed* Sentry whose own `captureException` throws escaped the catch and killed the launch anyway — the guard undone by its own error handler. Now guarded at both levels, which protect different things: the seam guards every caller (`addBreadcrumb` is documented "safe to call unconditionally" and callers don't wrap it), and `bootStep` guards its own reporting call because a contract that depends on a collaborator's internals is not a contract. `nativeCrash` is deliberately left unguarded — it is the LR20 exit test, and swallowing a failure there would report a working crash pipeline to the one person trying to find out whether it works.

### Honest scope

This does **not** fix the underlying native fault. If the throwing statement is the Sentry probe, the app boots and loses crash reporting. If it is something else in the same graph, the app boots and loses that step. It buys a working, diagnosable app — not a diagnosis. The stack trace from Play Console vitals still names the c
