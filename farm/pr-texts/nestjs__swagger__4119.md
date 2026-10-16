# fix(swagger-ui): preserve $ characters when building swagger-ui-init.js

## PR Checklist
Please check if your PR fulfills the following requirements:

- [x] The commit message follows our guidelines: https://github.com/nestjs/nest/blob/master/CONTRIBUTING.md
- [x] Tests for the changes have been added (for bug fixes / features)
- [x] Docs have been added / updated (for bug fixes / features) — N/A, no public API change


## PR Type
What kind of change does this PR introduce?

- [x] Bugfix
- [ ] Feature
- [ ] Code style update (formatting, local variables)
- [ ] Refactoring (no functional changes, no api changes)
- [ ] Build related changes
- [ ] CI related changes
- [ ] Other... Please describe:


## What is the current behavior?

`buildSwaggerInitJS` injects the serialized OpenAPI document into `swagger-ui-init.js` with:

```ts
jsTemplateString.replace('<% swaggerOptions %>', jsInitOptions)
```

String-form `String.prototype.replace` interprets `$`` / `$&` / `$'` / `$n` / `$$` in the replacement. A response description such as `` `^[a-z][a-z0-9_]{1,63}$` `` therefore corrupts the generated script (`SyntaxError` in the browser), so `/docs` renders blank while `/docs-json` stays valid.

This is the same class of bug already fixed for `buildSwaggerHTML` in #3946 and for `buildJSInitOptions` in #3896. The HTML path in this file already uses `() => value` replacers for that reason; the init-JS path was left on the string overload.

Issue Number: N/A


## What is the new behavior?

`buildSwaggerInitJS` now passes a callback replacer so `$` sequences in the OpenAPI JSON (especially descriptions) are inserted verbatim. `swagger-ui-init.js` remains syntactically valid and the template does not restart mid-document.

## Does this PR introduce a breaking change?
- [ ] Yes
- [x] No


## Other information

Regression coverage in `test/swagger-ui/swagger-ui.spec.ts` feeds a document whose description contains `$``, `$&`, `$'`, `$1`, and `$$`, then asserts:
- the description text is present verbatim (`JSON.stringify(description)`)
- the script is parseable (`new Script(script)` from `node:vm`)
- `window.onload` appears once (template does not restart)

```
npx vitest run test/swagger-ui/swagger-ui.spec.ts
# Test Files  1 passed (1)
#      Tests  6 passed (6)
```
