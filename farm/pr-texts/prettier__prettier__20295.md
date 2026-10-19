# Update flow-parser to v0.336.0

This PR contains the following updates:

| Package | Change | [Age](https://docs.renovatebot.com/merge-confidence/) | [Adoption](https://docs.renovatebot.com/merge-confidence/) | [Passing](https://docs.renovatebot.com/merge-confidence/) | [Confidence](https://docs.renovatebot.com/merge-confidence/) |
|---|---|---|---|---|---|
| [flow-estree](https://flow.org) ([source](https://redirect.github.com/facebook/flow)) | [`0.335.0` → `0.336.0`](https://renovatebot.com/diffs/npm/flow-estree/0.335.0/0.336.0) | ![age](https://developer.mend.io/api/mc/badges/age/npm/flow-estree/0.336.0?slim=true) | ![adoption](https://developer.mend.io/api/mc/badges/adoption/npm/flow-estree/0.336.0?slim=true) | ![passing](https://developer.mend.io/api/mc/badges/compatibility/npm/flow-estree/0.335.0/0.336.0?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/flow-estree/0.335.0/0.336.0?slim=true) |
| [flow-parser](https://flow.org) ([source](https://redirect.github.com/facebook/flow/tree/HEAD/packages/flow-parser)) | [`0.335.0` → `0.336.0`](https://renovatebot.com/diffs/npm/flow-parser/0.335.0/0.336.0) | ![age](https://developer.mend.io/api/mc/badges/age/npm/flow-parser/0.336.0?slim=true) | ![adoption](https://developer.mend.io/api/mc/badges/adoption/npm/flow-parser/0.336.0?slim=true) | ![passing](https://developer.mend.io/api/mc/badges/compatibility/npm/flow-parser/0.335.0/0.336.0?slim=true) | ![confidence](https://developer.mend.io/api/mc/badges/confidence/npm/flow-parser/0.335.0/0.336.0?slim=true) |

---

### Release Notes

<details>
<summary>facebook/flow (flow-estree)</summary>

### [`v0.336.0`](https://redirect.github.com/facebook/flow/blob/HEAD/Changelog.md#03360)

[Compare Source](https://redirect.github.com/facebook/flow/compare/v0.335.0...v0.336.0)

Likely to cause new Flow errors:

- Calls such as `Array.from` can now infer narrower literal types, requiring explicit annotations where broader types are needed. Unconstrained class type arguments now use their bounds instead of `empty`.
- Flow now checks `ref` compatibility for JSX tags typed as `string`, exposing refs that assume a more specific element type.
- Explicit `this` parameters on methods in library definitions no longer need to accept the instance type.
- Generic rest-parameter inference can now expose previously hidden parameter-type errors. For example, `(input: string, ...args: Array<unknown>) => void` no longer satisfies `(...args: TArgs) => R` when `TArgs` is inferred as `Array<unknown>` ([Try Flow example](https://flow.org/try/#&#8203;0C4TwDgpgBAwg9gWwQQwHYBMoF4oAoCWqYArsAFxQDOwAToQOYA0UAdG8jfZRQII03IQAHmKoA1qjgB3VAD4AlNllQAbnHzoA3ACht6CAGMANh2gAzUQeD44qKEbj16EdEIAqfLlAgAPYBAxKKAAlCGR0WyMQPgFhUQlpOWZg2VxtKCgECGAACzh0Clw2Fg4uCg9OSkUsZWDGbXlC4tLuKAquatqdPUMTGmgDW2ooQaQ0AthEFAwdBycXXFHp9HlNKAB6dagAUX44GgoAA3jJGUOofCDCUbBkawAjI2gpfFyoQ+o6VHpD7SA)).
- Rest destructuring of exact tuples, e.g. `const [first, ...rest] = t`, now excludes preceding elements' types from `rest`.
- Variance annotations are now checked through tuple type spreads, so `type T<out X> = [string, ...[X]]` is an error.

New Features:

- Support tuple types with trailing rest elements, e.g. `[string, ...Array<number>]`. Array literals ending in array spreads and arguments collected by rest parameters can flow to these types.

Notable bug fixes:

- Declaration merging for interfaces and `declare class` now preserves variance annotations.
- Returns inside functions nested in a type guard function are no longer checked against the enclosing type guard.
- References inside `declare namespace` blocks now see members merged across blocks and library files.
- Functions and constructors are now accepted as builtin `Function` and `Object` values.
- Fixed spurious indexed-access errors involving recursive class type-argument bounds.
- Type arguments used in later tuple spreads, e.g. `B` in `[...A, ...B]`, are now inferred instead of left underconstrained.
- Conditional types using `infer` on rest parameters now preserve the matched function's optional parameters and rest element in the inferred tuple, e.g. `[number, ...Array<boolean>]`. Matching functions with fewer parameters than the pattern and no rest parameter no longer produces underconstrained errors.

Misc:

- `flow-upgrade` now uses Flow parser packages and requires Node 18 and Prettier 3.

Parser:

- Correct JavaScript source columns after characters represented by surrogate pairs.

IDE:

- Hover `Go to` links no longer include the hovered declaration itself.

Library Definitions:

- `Intl` is now a builtin namespace with TypeScript-compatible definitions through ES2020, including `Collator`, `NumberFormat`, `DateTimeFormat`, `PluralRules`, `RelativeTimeFormat`, `Locale`, `DisplayNames`, `getCanonicalLocales`, and `formatToParts` for dates and numbers.
- The legacy `Intl$CollatorOptions`, `Intl$DateTimeFormatOptions`, and `Intl$NumberFormatOptions` aliases now match TypeScript. `Intl.DateTimeFormatPartTypes` includes `'unknown'`, and locale-aware `Date` methods accept `Intl.LocalesArgument` and `Intl.DateTimeFormatOptions`.
- The global `LocalesArgument` type is now `Intl.LocalesArgument`. Library declarations such as flow-typed's `declare var Intl` hide the builtin namespace and must be removed.
- `React.ElementConfig` is removed; use `React.ComponentProps` instead.
- Typed arrays gain `findLast`, `findLastIndex`, `toReversed`, `toSorted`, and `with`, and their constructors can be called without arguments. For types other than `Float16Array`, `findLast` narrows its result with a type-guard callback. Callbacks to `findLast` and `findLastIndex` can no longer annotate `this`.
- `Float16Array` now matches TypeScript's declaration, including its `from` overloads. `length`, `byteLength`, and `byteOffset` are read-only, `find` and `findIndex` predicates must return `boolean`, and callbacks can no longer annotate `this`.
- Add RegExp indices and flags, well-formed string methods, bigint Atomics, `Error.isError`, `Promise.try`, `Atomics.pause`, and additional ArrayBuffer and Date constructor signatures.
- Add TypeScript signatures for `Array.fromAsync`.
- `AggregateError.prototype.errors` is now typed `any[]`, matching TypeScript.
- Decorator definitions now match TypeScript: `ClassDecorator` accepts classes, decorator context and metadata types are available, and `Function` includes `[Symbol.metadata]`.
- Add `DisposableStack`, `AsyncDisposableStack`, `SuppressedError`, `Disposable`, and `AsyncDisposable`. `AsyncGenerator` now extends `AsyncIteratorObject` and includes `[Symbol.asyncDispose]`.

</details>

---

### Configuration

📅 **Schedule**: (UTC)

- Branch creation
  - At any time (no schedule defined)
- Automerge
  - At any time (no schedule defined)

🚦 **Automerge**: Disabled by config. Please merge this manually once you are satisfied.

♻ **Rebasing**: Whenever PR becomes conflicted, or you tick the rebase/retry checkbox.

🔕 **Ignore**: Close this PR and you won't be reminded about these updates again.

---

 - [ ] <!-- rebase-check -->If you want to rebase/retry this PR, check this box

---

This PR was generated by [Mend Renovate](https://mend.io/renovate/). View the [repository job log](https://developer.mend.io/github/prettier/prettier).
<!--renovate-debug:eyJjcmVhdGVkSW5WZXIiOiI0NC4xNTYuMyIsInVwZGF0ZWRJblZlciI6IjQ0LjE1Ni4zIiwidGFyZ2V0QnJhbmNoIjoibWFpbiIsImxhYmVscyI6WyJkZXBlbmRlbmN5Il19-->

