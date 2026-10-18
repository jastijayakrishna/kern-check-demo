# Multithreaded KOKKOS build with per-simulation opt-in (suffix kk)

Re-lands the multithreaded KOKKOS/Web-Worker build (#376, reverted in #377) with the regression fixed: **KOKKOS is now opt-in per simulation**, so nothing breaks by default — plus a critical worker bug fix found during verification.

## How per-simulation opt-in works
`Kokkos::initialize` is one-shot per wasm module — the startup mode can never change between runs (in-place switching and even worker recreation deadlock the next run; all verified). So the startup args are **constant** (`-k on t N -sf kk`) and the *script* decides:

- **Opt in**: a `suffix kk` line in the input script (a self-documenting no-op under the global `-sf kk`). The script runs unmodified, fully accelerated.
- **Everything else**: preprocessed at write-time only (`src/utils/kokkos.ts`; the editor shows original text): `suffix off` prepended + `atom_style`/`pair_style hybrid` wrapped in `suffix kk`/`off` (the only two things `-k on` requires to be Kokkos-enabled). All other styles run their plain serial implementations — **measured identical to a true serial build** (457 vs 459 tps).

## Critical bug fixed: asyncify re-entry wedge (pre-existing in #376)
Worker messages that call into wasm (per-step `setSyncFrequency`, bond settings) were handled **while the module was asyncify-suspended** between steps. Re-entering a suspended module corrupts asyncify — deterministically reproduced in node: the run's final rewind is lost, `runFile` never settles, and **the app wedges after any run that completes naturally**. Invisible before because nearly every example runs 10000+ steps and was always stopped manually (the stop path has a grace fallback). Fix: defer wasm-touching commands to the safe step window + dedupe unchanged `setSyncFrequency`.

## Opted-in examples (≥5k atoms, kk-safe, counts measured via local LAMMPS)
faceted SiC (24,050) · Crack 2D (8,141) · Diffusion (6,750) · NaCl solution (5,666) · 3D LJ fluid (5,500) · generate nanoporous (5,184) · nanoporous SiO2 (1.5M — untested, likely too heavy for the browser regardless of kk)

## Browser-verified
- Molecular hybrid examples (Benzene, Methane, Peptide) **run again** — the #376 regression is gone
- kk examples accelerated: Diffusion **137 tps** kk vs ~120 serial, Crack 175, 3D-LJ 178
- SiC (`run 20`) completes naturally and the app stays healthy (previously wedged)
- serial↔kk alternation, stop→rerun clean; `tsc` clean; 430/430 tests; build clean

## Known follow-up (non-blocking)
A single intermittent, non-fatal `RangeError: Maximum call stack size exceeded` appeared once during a 5-sims-in-a-row session (app kept working; not reproducible with the same example alone). Possibly pre-existing in the worker/plotting layer; worth a separate look.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
