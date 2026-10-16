# fix: remove uuid dependency, replace with inline implementation

**Requirements**

- [x] I have added test coverage for new or changed functionality
- [x] I have followed the repository's [pull request submission guidelines](../blob/master/CONTRIBUTING.md#submitting-pull-requests)
- [x] I have validated my changes against all supported platform versions

**Related issues**

N/A

**Describe the solution you've provided**

Removes the `uuid` package dependency entirely and replaces it with an inline UUID v4 implementation adapted from [js-core's browser SDK polyfill](https://github.com/launchdarkly/js-core/blob/main/packages/sdk/browser/src/platform/randomUuidV4.ts).

The implementation uses `crypto.randomUUID()` when available, falls back to `crypto.getRandomValues()`, and finally to `Math.random()`.

All three usages (`diagnosticEvents.js`, `AnonymousContextProcessor.js`, `EventSender.js`) now use UUID v4 instead of v1. The diagnostic events spec originally called for v4 anyway.

**Describe alternatives you've considered**

- Upgrading uuid to v11 (latest CJS-compatible version) — still keeps the external dependency.
- Upgrading to uuid v14 (latest) — not feasible as it dropped CommonJS support entirely.

**Additional context**

All 635 tests pass after the change.

Link to Devin session: https://app.devin.ai/sessions/63cc8da489324f20b17db43d0d296dea
Requested by: @kinyoklion

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Medium Risk**
> Changes how anonymous context keys, event payload IDs, and diagnostic IDs are generated (switching from `uuid` v1 to an internal UUID v4 generator), which could affect ID format/uniqueness assumptions in downstream systems.
> 
> **Overview**
> Removes the external `uuid` dependency and replaces all UUID generation with a new internal `src/uuid.js` helper that prefers `crypto.randomUUID`, then `crypto.getRandomValues`, then `Math.random`.
> 
> Updates `AnonymousContextProcessor`, `EventSender`, and `diagnosticEvents` to generate UUID **v4** identifiers (anonymous context keys, `X-LaunchDarkly-Payload-ID`, and diagnostic IDs). Adds a unit test asserting `DiagnosticId().diagnosticId` matches UUID v4 format.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit f28ce25a7c410e2feaa053381024ba8204a0711c. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
