# Preserve blank line between HTML block and nested list in Markdown list item

<!--
⚠️ Pull requests that do not follow the template may be closed without review.
-->

## Description

Fixes #17738

Inside a list item, a nested list is printed right after the block before it. #17857 kept the blank line when that block is a paragraph or code block, but not when it's HTML.

That matters for HTML because most HTML blocks (`<details>`, `<div>`, ...) only end at a blank line. Drop it and the list becomes part of the HTML block. This input:

<!-- prettier-ignore -->
```md
- Some text

  <details>
    <summary>Summary</summary>

    - Lorem
    - ipsum
  </details>
```

was formatted to

<!-- prettier-ignore -->
```md
- Some text

  <details>
    <summary>Summary</summary>
  - Lorem
  - ipsum

  </details>
```

and if you parse that output again you get a single `html` node containing `- Lorem\n- ipsum`, so it no longer renders as a list.

The fix adds `html` to the existing check. A blank line that isn't in the source is still not added (`html-comment.md` covers that). Only the `markdown` parser changes; `mdx` parses this input differently.

The 4 → 2 space indent change and the extra blank line before `</details>` from the issue are left alone. Both render the same, and changing them would be a style decision.

Tested with `yarn test tests/format/markdown/list/html-before-nested-list` (3 tests, all fail without the change) and a full `yarn test tests/format` run.

## Checklist

- [x] I’ve added tests to confirm my change works.
- [ ] (If changing the API or CLI) I’ve documented the changes I’ve made (in the `docs/` directory).
- [x] (If the change is user-facing) I’ve added my changes to `changelog_unreleased/*/XXXX.md` file following `changelog_unreleased/TEMPLATE.md`.
- [x] I’ve read the [contributing guidelines](https://github.com/prettier/prettier/blob/main/CONTRIBUTING.md).
- [ ] I did _not_ use AI to generate this PR.
- [x] (If the above is not checked) I have reviewed the AI-generated content before submitting.

Made with help from Claude Code.
