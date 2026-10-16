# fix(webdriverio): honor getHTML exclusion options

## Proposed changes

`getHTML({ excludeElements: ['style', 'script'], pierceShadowRoot: false })` silently retains the excluded elements. The option is also dropped when browser-runner forwards a shadow-piercing snapshot to Node. Both failures reproduce on the `main` baseline (`ba488fa`, v9.31.7).

Pass the exclusions to the browser script, filter a detached copy, and serialize it with the browser's native `innerHTML`/`outerHTML`. Forward `excludeElements` in the browser-runner path as well. No option or dependency is added, and the live DOM remains unchanged.

The copy is imported through an inert document to avoid invoking custom element constructors, then adopted back without insertion so `noscript` keeps the original document's serialization behavior. Native serialization preserves case-sensitive SVG attributes. Excluding the target itself returns an empty string only when its tag is included.

CI follow-up: the affected window/frame tests use local HTTP fixtures with Lighthouse enabled. The branch is reconciled with upstream main, including EdgeDriver 6.3.1 and its valid lockfile. Frozen installation, compilation and full lint checks pass; 1,613 WebdriverIO/utils tests, two navigation cases and two standalone shadow-exclusion cases pass on the final tree.

## Types of changes

- [x] Bugfix (non-breaking change which fixes an issue)

## Checklist

- [x] I have read the [CONTRIBUTING](https://github.com/webdriverio/webdriverio/blob/main/CONTRIBUTING.md) doc
- [x] I have added tests that prove my fix is effective or that my feature works
- [x] I have added the necessary documentation (if appropriate; existing option behavior is restored)
- [x] I have added proper type definitions for new commands (if appropriate; no new commands)

## Backport Request

- [x] This change is solely for `v9` and doesn't need to be back-ported

## Validation

- Before the fix, regression assertions fail because excluded `<style>`, `<script>`, and `.omit` elements remain in the output.
- All WebdriverIO package tests: **1,255 passed, 1 skipped**, across **182 files**; no type errors reported by the runner.
- **Three focused browser-runner integration tests** pass on Chrome **153.0.8010.12**: option combinations/live DOM preservation, literal `noscript` text, and case-sensitive SVG attributes.
- Standalone Chrome, **BiDi and Classic**: all eight combinations of `pierceShadowRoot` and `includeSelectorTag` return filtered HTML and preserve the live DOM.
- DOM tests cover target exclusion and verify that snapshotting does not invoke custom element constructors.
- WebdriverIO compilation (including declarations), targeted ESLint, and `git diff --check` pass.
- Dedicated Node/BiDi coverage with `globalThis.wdio` absent verifies real reconstruction and sanitization of nested shadow templates. Disabling the Node exclusion loop makes the regression fail.
- **Two standalone Chrome/BiDi tests** pass with open and closed nested roots, adopted styles, `style`/`script`/`.omit` exclusions, both selector-tag options, and an unchanged live DOM.
- The complete published tree at `4f1976a` was fetched back and matches the tested local tree exactly.

Reproduction, using `<section id="snapshot"><span>Keep</span><style>p { color: red }</style></section>`:

```js
await $('#snapshot').getHTML({
    excludeElements: ['style'],
    pierceShadowRoot: false,
    prettify: false
})
// Before: <section id="snapshot"><span>Keep</span><style>p { color: red }</style></section>
// After:  <section id="snapshot"><span>Keep</span></section>
```

## Further comments

AI disclosure: OpenAI Codex performed the investigation, implementation, and local validation for this GitHub account. Maintainer review is pending.

Could a TSC member confirm whether this contribution qualifies under the [non-project-member contribution expense policy](https://github.com/webdriverio/webdriverio/blob/main/GOVERNANCE.md#expenses-from-non-project-members), and the approved amount and claim requirements if accepted?

### Reviewers: @webdriverio/project-committers
