# Add `no-legacy-computed` rule to disallow `computed` and computed macros

This adds an opt-in lint rule to prevent introducing legacy Ember computed APIs while teams migrate to tracked/getter-based patterns. It covers both `computed` from `@ember/object` and all macro imports from `@ember/object/computed`.

- **New rule: `ember/no-legacy-computed`**
  - Reports `ImportSpecifier` for `computed` imported from `@ember/object`
  - Reports all imports from `@ember/object/computed` (e.g. `and`, `gt`, `sortBy`, etc.)
  - Implemented as non-recommended (no default config changes)

- **Rule docs**
  - Added `docs/rules/no-legacy-computed.md` with scope, rationale, and correct/incorrect examples
  - Regenerated rule documentation metadata so the rule appears in the README rule table

- **Rule tests**
  - Added focused coverage for:
    - valid non-Ember imports and modern patterns
    - invalid direct and aliased `computed` imports
    - invalid single/multiple macro imports from `@ember/object/computed`
    - side-effect import from `@ember/object/computed`

```js
// now flagged
import { computed } from '@ember/object';
import { and, gt, sortBy } from '@ember/object/computed';
```
