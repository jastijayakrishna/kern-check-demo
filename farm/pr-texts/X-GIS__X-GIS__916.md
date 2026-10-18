# fix(shader-dsl): renorm raw df64 operands across all cancelling ops (loran + audit)

## What

An exhaustive audit of every `fp64Lower` site that synthesizes a **cancelling df64 op** (sub / div, and the internal sub/div inside fract / mix / normalize). Started from the `loran` df64 collapse on the GPU probe and generalized: `loran` was one of several sites sharing the same **"raw operand (loaded lo) → cancelling op, no renorm"** pattern that #915 (scalar binop sub/div) didn't reach.

## The bug class

A raw df64 value (loaded lo — a uniform/attribute/texture load, or a lane sliced from a loaded vec64) feeding a near-cancellation loses its lo word under a driver's fast-math (Apple Metal, ANGLE→fxc). Renorming through `df64_add(x, 0)` recomputes the pair via an on-GPU twoSum, turning a *loaded* lo into a *computed* lo that survives. Idempotent (exact for a normalized pair) and opaque to the optimizer (a `df64_` call, not `+ 0`).

## Audit result — every cancelling-op site

| Site | Covered by |
|---|---|
| scalar binop `-` / `/` | #915 |
| `distance()` per-lane sub | this PR (commit 1) |
| **scalar `fract`** (`sub(a, ⌊a⌋)`) | this PR (commit 2) |
| **scalar `mix`** (`sub(b, a)`) | this PR |
| **vec64 `-` / `/`** | this PR |
| **vec64 `fract` / `mix`** (per-lane sub) | this PR |
| **vec64 `normalize`** (per-lane div) | this PR |
| `sqrt`, `dot`, `length`, mat64 | left as-is — sqrt passes on-device; dot/length have no cancellation; mat is data-dependent |
| `abs`, `floor`, `min`, `max` | no cancellation — untouched |

## How

- Extract `renormForCancel` (scalar) + add its vec64 twin `renormForCancelVec` (`df64_vN_add(x, 0)`, with `splatPair(0)` = `DF64VecN(0, 0)`).
- Apply at each cancelling site above; non-cancelling builtins are deliberately skipped so no unnecessary ops are emitted.

## Verification

- `tsc` clean; **591/591 shader-dsl tests green**, including the oracle metamorphic gate (authored ≈ lowered) — the renorm is value-preserving, so no render regression on correctly-rounded GPUs.
- Package build + full site build green (probe page emits).
- Goldens: only `fp64-loran`, `fp64-checker-plane`, `fp64-mercator-tiles` change (the added `df64_add` on their fract / distance / vec64 operands) — every other golden is byte-identical.
- **Probe**: added discriminative vec64 gap tests `vec_sub_ld` / `vec_div` / `vec_fract` over `pt = (1e6+0.5, 0)` — the old `vec_sub` used `vBig = 1e8` (f32-exact, lo = 0) and could not catch the loaded-lo loss. Scalar `fract` already had a discriminative test.
- **On-device is the final gate** (per the #901 lesson that a blanket launder can regress a specific driver): after deploy, re-run the probe on Apple + Blackwell. Expect `loran` / `fract` / `vec_sub_ld` / `vec_div` / `vec_fract` to read PASS. `mix` / `normalize` are renormed for structural completeness but stay entangled with the separate `df64_mul` collapse and are not independently probe-validated here.

## Follow-up (out of scope)

- The `df64_mul` internal distributive-fusion collapse (Apple `mul`/`vec_mul` and the remaining Blackwell WebGL2 `rand*` composed trees) — a distinct mechanism inside `df64_mul`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_011vnuqfMLe4o7Tw5zJ7KPat
