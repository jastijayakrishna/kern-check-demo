# fix(oas): resolve Path Item `$ref`s in analyzer operation scope

| 🚦 Resolves |
| :------------------- |
| — |

## 🧰 Changes

`analyzeOperation()` / `analyzeWebhookOperation()` (added in #1170) threw `Operation “… not found”` for valid OpenAPI 3.1 documents whose Path Item is a `$ref` — including the documented `components.pathItems` pattern.

**Bug and impact:** Scoped analysis of a single operation crashes on specs that reuse Path Items. Downstream feature detection (security types, `$ref` usage, media types) never runs for those operations.

**Concrete trigger:** OAS 3.1 spec with `/pets/{petId}` → `#/components/pathItems/petById` containing `GET`. `analyzeOperation(def, { path: '/pets/{petId}', method: 'get' })` threw even though `Oas.operation()` already resolved the same `$ref`.

**Root cause:** `computeOperationScope()` / `computeWebhookScope()` looked up HTTP methods on the authored Path Item object. A `$ref` only exposes `$ref`, so method lookup failed. `Oas.operation()` / `getPaths()` already dereference Path Items; the analyzer path did not.

**Fix:** Resolve Path Item `$ref`s (without mutating the definition), then scope only the requested method and its common parameters at the `$ref` target so sibling operations on the same Path Item stay out of the analysis.

## 🧬 QA & Testing

- Added regression tests that a `components.pathItems` `$ref` is scoped for both paths and webhooks, including sibling-method isolation and common parameters.
- Added `analyzeOperation()` integration coverage for security types and `$ref` locations on a referenced Path Item.
- `npx vitest run packages/oas/test/analyzer` — 75 tests passed.
- `npm run lint:types --workspace=oas` passed.

Not environment-dependent or flaky.

<div><a href="https://cursor.com/agents/bc-36e360d1-063e-4c5b-aed4-b9682319d202?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/automations/206fd12c-a17c-11f1-b532-320a589b8025"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/view-automation-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/view-automation-light.png"><img alt="View Automation" width="141" height="28" src="https://cursor.com/assets/images/view-automation-dark.png"></picture></a>&nbsp;</div>
