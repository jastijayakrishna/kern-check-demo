# fix(driver): guard toPosix against nullish file paths on Windows

## Summary

Guards `toPosix` in `@packages/driver` against `null`/`undefined` inputs so stack-enhancement during `cy.fail()` does not throw a secondary `TypeError` on Windows.

## Motivation

Develop pipeline 83688 (`a7a64008`) failed `windows-run-app-integration-tests-chrome` due to a port-4455 collision flake. The real error was `PORT_IN_USE_SHORT`, but test output showed only:

```
TypeError: Cannot read properties of undefined (reading 'replaceAll')
    at toPosix (packages/driver/src/cypress/util/to_posix.ts)
```

This defensive fix ensures the underlying error surfaces in CI logs. Does **not** fix the port collision itself (tracked separately).

## Changes

- Return nullish inputs unchanged from `toPosix`
- Add unit test coverage

## Testing

```bash
yarn workspace @packages/driver test -- test/unit/cypress/util/toPosix.spec.ts
```

### PR Tasks

- [x] Have tests been added/updated?
- [na] Associated issue — mechanical defensive fix; port flake tracked separately
- [na] cypress-documentation PR
- [na] API type definition changes

<div><a href="https://cursor.com/agents/bc-8ed50152-5d8c-43db-9fe6-71ca878e5f4f"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/automations/8ea3cd43-993b-414b-8a4b-ffb664a27b4b"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/view-automation-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/view-automation-light.png"><img alt="View Automation" width="141" height="28" src="https://cursor.com/assets/images/view-automation-dark.png"></picture></a>&nbsp;</div>

<!-- CURSOR_SUMMARY -->
---

> [!NOTE]
> **Low Risk**
> Small defensive utility change plus a test-only intercept tweak; no auth, security, or broad behavioral changes to production paths.
> 
> **Overview**
> **`toPosix`** in the driver now returns `null`/`undefined` unchanged instead of calling `replaceAll` on Windows, so stack enhancement during failures no longer throws a secondary `TypeError` that can hide the real error (notably on Windows CI).
> 
> The **15.18.2 changelog** documents this bugfix. **Unit tests** cover nullish inputs.
> 
> In **system e2e `xhr.cy.js`**, the intercept pattern changes from `/api/` to `/\/api\//` so only app `/api/` paths match, avoiding accidental matches on Chrome background URLs (e.g. `clientservices.googleapis.com`) that could flake CI.
> 
> <sup>Reviewed by [Cursor Bugbot](https://cursor.com/bugbot) for commit fdaffa0d31a399fc623bb43d1db0ebae37a66a78. Bugbot is set up for automated code reviews on this repo. Configure [here](https://www.cursor.com/dashboard/bugbot).</sup>
<!-- /CURSOR_SUMMARY -->
