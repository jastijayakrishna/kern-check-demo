# fix(execution-plan): remediate the ten ExecutablePlan sidecar audit findings

Audit remediation for the ExecutablePlan sidecar landed in #540. Ten findings, all fixed.

No G-code snapshot changed, so no `Snapshot change acknowledged` line is required.

## Root causes

**1 — The three "independent" readers share one engine.** `buildMotionManifest`, `buildGcodeRenderModel` and `parseGcodeProgram` all compose the single modal engine in `src/core/gcode/` (ADR-255 stage 1), and the manifest and simulator sample arcs through the same centre solver and the same sampler — which `parser-equivalence.test.ts` pins on purpose. For an arc the endpoint comparison evaluates the same code twice, so agreement there carries no evidential weight. The contract called `parseGcodeProgram` "clean-room" and implied mutual verification. Section 7 now splits what the gate detects (policy divergence layered on the shared engine) from what it cannot (any defect inside it). The word "clean-room" is withdrawn.

**2 — Canned cycles failed opaquely.** The Inspector expands one `G73`/`G81`/`G82`/`G83` word into a whole drilling sequence (ADR-255 stage 12) while the manifest models that line as a single move, so the readers can never agree. The class was already refused, as `compound-motion-line` on a raw line. It now returns `unsupported-input` with a `canned-cycle-unsupported` issue, pinned by two corpus fixtures. **No input that previously built now fails** — this renames an existing refusal and does not widen one (collaboration rule 7); the pre-change behaviour was captured before the edit.

**3 — Flat full-circle arcs were classified `plunge` (live-path defect).** `classifyMotion` decided from endpoint displacement, and a closed arc ends where it started. Because `isMaterialEntry` rejects a plunge on a laser, `firstProcessPoint` stayed `null` for a job whose first cut was a circle — the value `canvas-motion-plan.ts` uses for the canvas material-entry marker. Measured before the fix: `["travel","plunge"]`, `firstProcessPoint: null`; after: `["travel","process"]`, `{x:5,y:0,z:0}`. ADR-271's contract section 5 already required this and the sidecar carried a compensating special case; fixing the manifest lets that workaround go, leaving one implementation on the path recovery and the overlay already read.

**4 — The success path re-sourced `gcode` from the plan.** A no-op only because `byteParity` ran first, which made byte neutrality depend on check ordering rather than on never rewriting the emitter's output. The emission is now returned unchanged on all paths.

**5 — The byte check passes by construction.** `serializeExecutablePlan` returns `compatibility.exactProgram`, so on a freshly built plan it compares a string to itself. It guards storage and transport, not emitter correctness. Stated in `byteParity` and in section 7.

**6 — Roughly five passes per emission.** `determinismParity` ran a full second build plus two whole-plan `JSON.stringify` calls, each embedding the entire program. Determinism is a property of the builder, already proven per corpus fixture, so it is now an off-by-default `deterministicRebuild` option; when it runs it skips the carrier `byteParity` covers.

**7 — Endpoint tolerance was absolute.** A fixed `1e-6 mm` against `Float32Array` storage, where one ULP is already ~`1.2e-4 mm` at `1200 mm`. Now the larger of `1e-6 mm` and four ULPs, with a large-coordinate fixture.

**8 — Park classification existed twice.** `classifyPlanParks` re-derived terminal and `M0`/`M1` parks over blocks the manifest had already classified, converting only `travel` motions that were by then already `park`. A no-op holding a second copy of a safety-relevant rule; removed.

**9 — The schema was unenforced.** Adding a controller id or `ProgramEvent` kind would have left the versioned contract silently stale. All nine corpus plans are now validated against it, with `Record<Union, true>` maps so the compiler rejects a drifted enum. The validator lives in `__fixtures__` and adds no runtime dependency (that would need its own ADR); its 
