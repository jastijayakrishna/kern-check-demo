# Build studio workspaces in a child process, not in the harness

## The symptom

A production studio sandbox (`ta-01KZ1P7FTBNM4Z3YWATYKBJ3KS`) was sitting at **1.66 GB RSS**. Comparing it against the rest of the live fleet made it a clear outlier:

| sandbox | uptime | harness RSS | threads | bundles in /tmp |
|---|---|---|---|---|
| **target** | 22 min | **1,656 MB** | **52** | **2** |
| sibling | 12 min | 344 MB | 11 | 1 |
| sibling | 12 min | 262 MB | 7 | 0 |
| sibling | 8 min | 261 MB | 7 | 0 |
| sibling | 6 min | 259 MB | 7 | 0 |

Idle warm harness ≈ 258 MB / 7 threads. The 52 threads is a fingerprint: importing the build toolchain alone takes a fresh Node process from 7 to 36 threads, so that harness had run `test_agent`.

## Root cause

Reproduced in a live sandbox by driving the real toolchain through three build cycles:

| stage | RSS | V8 heapUsed | threads |
|---|---|---|---|
| boot | 125 MB | 4 MB | 7 |
| toolchain imported | 208 MB | 21 MB | 36 |
| **build 1 (worker)** | **1,697 MB** | 83 MB | 56 |
| build 2 | 2,051 MB | 151 MB | 56 |
| build 3 | 2,230 MB | 111 MB | 56 |
| after `global.gc()` | 2,176 MB | **51 MB** | 56 |

At 2,176 MB RSS, V8's heap is 51 MB and `external` 23 MB — **~2.1 GB is native memory** held by Rolldown, Vite 8's Rust/napi bundler. `global.gc()` recovers 75 MB; `MALLOC_ARENA_MAX=2` recovers 35 MB, ruling out glibc arena fragmentation. Process exit is the only thing that reclaims it, and the harness is long-lived and reused across `test_agent` calls — so each build's peak became the process floor.

Two gVisor details compound it, neither fixable from inside the guest: `/proc/cpuinfo` reports the host's **17 CPUs** while the sandbox has **1** CPU of affinity (Rolldown's Rust pool sizes for 17), and `os.totalmem()` reports 242 GB, from which V8 derives a 4,288 MB heap limit. Production sets neither `SANDBOX_MEMORY_LIMIT_MB` nor `SANDBOX_CPU_LIMIT`, so `memory.max` is 242 GB and nothing ever applies back-pressure.

## The fix

`test_agent` built **in-process**; Publish already spawned the literal `aai deploy` CLI as a child. This makes the two agree — the bundler now runs in a one-shot child (`studio-build-child.ts`), artifacts returning through a scratch dir rather than 8 MB of escaped JSON on stdout.

Two constraints worth knowing:

- **The child is the harness entry re-spawned with `--build-workspace`**, not a sibling script, because the guest deliberately ships ONE artifact (tsdown's `inlineDynamicImports`; the Modal image bakes exactly `/opt/aai/harness.mjs`). A second file would ripple into tsdown, the image bake, and its content hash.
- **`typecheckWorkspaceDir` stops importing the bundler toolchain.** That import alone is ~90 MB and ~29 threads, permanently, and `check_types` never bundles — it only needs the module that spawns `tsc`.

`harness-bundle.ts` is extracted (the bundle → runtime lifecycle) to keep `harness.ts` under the 500-line cap: 502 → 380.

## Verification

- The child produces a real **7.8 MB** bundle containing `__aaiCreateRuntime`, from **both** the source entry and the bundled `dist/harness.mjs` — the `import.meta.url` self-resolution holds after bundling.
- New regression test: a real in-process build grew the test process **897 MiB**; it now stays flat (asserts < 400 MiB). It failed before the fix and passes after.
- On a **real Modal sandbox**, a build succeeds with the child's exact stripped env: `{"ok":true,"bytes":7976689,"rss_mb":1593,"envKeys":"PATH"}` — confirming both the PATH-only env and the ~1.6 GB cost, now confined to a process that exits.
- `pnpm check` green (45/45 tasks, both quality ratchets); aai-guest 185/185; aai-server integration 12/12 including the real-harness Publish path.

⚠️ **Do not follow this up by setting `SANDBOX_MEMORY_LIMIT_MB` alone** — a cap under ~1.8 GB would OOM-kill sandboxes mid-build, and `--max-old-space-size` can't help because the memory is native, not V8's. That reasoning is recorded in CLAUDE.md.

Also fixes four stale `workspace/build` comments — that RPC is `workspace/deploy` now.

