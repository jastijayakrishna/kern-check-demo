# Fix Gemini structured output and roadmap repair timeout

## Summary
- enforce Gemini Creative DNA structured output through a compact OpenAPI-compatible responseSchema
- keep the full strict Zod validation and deterministic fallback after generation
- expose bounded production fallback diagnostics without logging prompts, model output, or secrets
- give roadmap generation and repair independent configurable timeout windows
- document the new behavior and add regression coverage

## Verification
- focused classifier/service/route checks after live hardening: 14/14 passed
- broader initial regression selection, including roadmap timeout tests: 18/18 passed
- lint: passed
- typecheck: passed
- Next.js production build: passed
- Vercel Preview checks: passed
- full unit suite: 161/163 passed

The two full-suite failures are pre-existing on main: the sample-roadmap fixture deadline is 2026-08-20, now in the past, and the tracked ontology artifact does not match a fresh compile of the unchanged ontology source.

## Live preview
Tested with a different brief from the earlier hand-tracking case:

> I know basic p5.js. I want microphone volume and frequency bands to make a generative typographic poster pulse in a browser-based installation.

Results:
- Gemini Creative DNA completed without the fallback warning and identified p5.js, microphone, frequency bands, generative typography, pulsing, browser interaction, and installation
- the Add concept safeguard found and added FFT from the ontology
- QUANDA selected **Sound Visualization: Frequency Analysis with FFT** by **The Coding Train**
- the final project-aware roadmap retained that exact tutorial in **Stage 3 — Apply Audio input and FFT**
- /api/roadmap returned 200 and Vercel logs contained no repair AbortError; the route used its deterministic integrated fallback while preserving the selected tutorial

