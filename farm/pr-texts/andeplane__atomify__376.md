# Run the multithreaded (KOKKOS) atomify build in a Web Worker

Makes Atomify use lammps.js **1.5.0**'s multithreaded `wasm-atomify` build (KOKKOS/pthreads + full 14-package set). Follow-up to the serial migration (#375).

## The core problem & solution
A pthreads+ASYNCIFY emscripten module **cannot initialize on the browser main thread** — its thread-pool handshake needs `Atomics.wait` blocking, which browsers forbid off a Worker (confirmed: `createModule()` deadlocks forever on the main thread). So LAMMPS now runs **inside a Web Worker**.

Rather than rewrite Atomify's synchronous, live-heap simulation pipeline, the worker streams data into a plain-JS **"bridge heap"** on the main thread, so the existing store + modifier + render pipeline runs **unchanged**, reading through the familiar heap-pointer path. Two key enablers:
- Run the pthreads module in a Worker → no deadlock (loads ~0.5s).
- Fetch the module once as a **Blob** (`Module.mainScriptUrlOrBlob`) so all 8 pthread workers instantiate from one in-memory blob instead of each re-fetching ~50 MB (which failed with `ERR_CACHE_WRITE_FAILURE`).

## What's implemented (all browser-verified in Chromium)
- **Runs multithreaded**: Diffusion — 6750 atoms across 8 Kokkos threads.
- **Particle + bond rendering**: SiC nanoparticle — 740 atoms, 1359 bonds, Vashishta (MANYBODY); Water vapor — 1981 bonds.
- **Multi-run reset + clean Stop**: verified Diffusion → Stop → SiC (independently confirmed, zero errors).
- **Pause/Continue**: timestep freezes and resumes.
- **Analysis UI**: computes/fixes/variables panels populated; color-by-compute (`displace`) with legend.
- **Walls, memory, timesteps/sec** (e.g. 71 steps/s on SiC).
- Cross-origin isolation via vite COOP/COEP headers + coi-serviceworker (GitHub Pages).
- `npm run build` exit 0, `tsc` clean, **430/430 unit tests pass**.

## New/changed files
`src/wasm/lammps.worker.ts`, `src/wasm/LammpsWorkerProxy.ts`, `src/wasm/workerMessages.ts` (new); `src/wasm/lammpsAdapter.ts`, `src/components/Simulation.tsx`, `src/modifiers/colormodifier.ts`, `src/types.ts`, `index.html`, `vite.config.ts`, `public/coi-serviceworker.min.js`.

## Known follow-up (not blocking)
The clean-stop path swallows a build-specific "function signature mismatch" asyncify rejection + a 300ms grace, stemming from a **real bug in lammps.js@1.5.0's atomify build**: `lammpsweb_throw_error → UTF8ToString` is handed a BigInt pointer (MEMORY64) and crashes. Worth fixing upstream in lammps.js (it also corrupts error reporting); the workaround here is verified robust meanwhile.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
