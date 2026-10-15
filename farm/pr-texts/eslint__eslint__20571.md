# feat: Add `meta.languages` support to rules

Implements <a href="https://github.com/eslint/rfcs/blob/main/designs/2025-rule-languages/README.md">RFC 2025-rule-languages</a>: adds a `meta.languages` array to rule metadata, validated at config time against the active language.

## Changes

- **`lib/config/config.js`**
  - Added `doesRuleSupportLanguage(ruleLangs, configLanguageName, validPluginNames)` helper with full matching logic
  - Added defensive `Array.isArray()` and `typeof === "string"` guards for invalid `meta.languages` values
  - Updated `validateRulesConfig()` to collect rules whose `meta.languages` don't match the config language and throw a descriptive `TypeError` listing all offenders
  - Normalizes `@/` to `js/` in the language name shown in error messages (e.g. `"js/js"` instead of `"@/js"`)
  - Validates `meta.languages` structure (must be an array of strings) inside `validateRulesConfig()`, only for enabled rules
  - Attaches `messageTemplate = "rule-unsupported-language"` and `messageData` to the thrown error, enabling both verbose terminal output and clear inline-config error messages

- **`lib/config/flat-config-schema.js`**
  - No longer validates `meta.languages` at `Config` construction time; validation is deferred to `validateRulesConfig()` so rules in plugins with invalid `meta.languages` do not cause errors unless the rule is actually enabled

- **`lib/linter/linter.js`**
  - Added special handling for the `rule-unsupported-language` message template: when a rule enabled via inline config (e.g. `/* eslint my-plugin/my-rule: 2 */`) doesn't support the active language, the lint error now clearly explains why and tells the user to scope the rule with `files` or disable it, instead of showing an incomplete message

- **`messages/rule-unsupported-language.js`** *(new)*
  - Verbose error message template shown in the terminal when ESLint throws for unsupported-language rules, listing the offending rule IDs, the active language, and actionable remediation steps (`files` scoping or `"off"`)

- **`tests/lib/config/config.js`** — Extended `meta.languages` validation test suite covering all matching paths:
  - `js/*` wildcard matching `@` plugin
  - Namespace match with `plugin/*` wildcard
  - `@/js` → `js/js` normalization in error messages
  - Both rule IDs appear in the error when multiple rules are unsupported
  - Invalid `meta.languages` (non-array or non-string entries) throws at `validateRulesConfig()` time only when the rule is enabled

- **`docs/src/extend/custom-rules.md`** — Added `meta.languages` property documentation with usage examples and matching semantics (removed internal `@/js` implementation detail)
- **`docs/src/extend/custom-rule-tutorial.md`** and **`docs/_examples/custom-rule-tutorial-code/enforce-foo-bar.js`** — Updated tutorial example to include `languages: ["js/js"]`

## Matching semantics

```js
// Rule supports any language
meta: { languages: ["*"] }

// Rule supports only JS
meta: { languages: ["js/js"] }

// Rule supports any language from the "markdown" plugin
meta: { languages: ["markdown/*"] }

// Rule supports a specific language; also resolves via plugin.meta.namespace
meta: { languages: ["markdown/gfm"] }

// No meta.languages → backward compatible, works with all languages
```

Rules without `meta.languages` continue to work with every language. Rules that declare `meta.languages` will cause `validateRulesConfig()` to throw if the active language isn't in the list. Invalid `meta.languages` values (non-array or containing non-strings) are only validated when the rule is actually enabled — consistent with how ESLint skips other rule validation (e.g. rule existence checks) when a rule is set to `"off"`.

## Error messages

When a rule doesn't support the active language, the error message now advises the user to either scope the rule with the `files` option or disable it, for example:

```
The following rules do not support the language "json/json":
    - "no-var"

To fix this error:
- Use the "files" option to apply the rule only to files where the language is supported:
  { files: ["**/*.js"], rules: { "no-var": "error" } }
- Or disable the rule with "off" or 0.
```

For rules enabled inline (e.g. `/* eslint no-var: 2 */`), the lint error message is similarly clear:

```
1:1  error  Inline configuration for rule "no-var" is invalid:
              Rule does not support the language "json/json". Use a config block
              with "files" to apply the rule only to supported files, or disable it.
```

<!-- START COPILOT CODING AGENT TIPS -->
---

📱 Kick off Copilot coding agent tasks wherever you are with [GitHub Mobile](https://gh.io/cca-mobile-docs), available on iOS and Android.
