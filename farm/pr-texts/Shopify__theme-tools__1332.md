# Accept whitespace around `=` in HTML attributes

## What are you adding in this PR?

`@shopify/liquid-html-parser` now accepts whitespace around `=` in HTML attributes, as browsers and the old ohm grammar do.

Before, the recursive-descent parser ended the attribute name at the space and found no `=`. It then turned each part of the value into an attribute of its own:

| Source | Before | After |
| --- | --- | --- |
| `<img data-ratio = '{{ r }}'>` | `data-ratio` (empty), `{{ r }}` | `data-ratio='{{ r }}'` |
| `<img srcset= "{{ a }}, {{ b }} 2x">` | `srcset=` (empty), `{{ a }}`, `,`, `{{ b }}`, `2x` | `srcset="{{ a }}, {{ b }} 2x"` |

Dawn 5's footer has the `srcset= "…"` form, so this shows up in real themes.

Changes:
- **Tokenizer:** inside a tag, each whitespace run is now its own `Text` token.
- **Parser:** skips those tokens between attributes, before `=`, and before the value. This matches the old grammar's syntactic attribute rules (`AttrDoubleQuoted = attrName "=" doubleQuote …`), which skipped `space` implicitly. Both attribute loops (element and Liquid-branch) share a new `parseAttributeAfterName`, so curly-quoted values inside an `{% if %}` in attribute position now get the same double/single mapping as top-level ones. The parser no longer modifies `token.start`.
- **`scanForHtmlCloseTag`:** compares every `Text` token between `</` and `>`, not just the first one. Without this, the new tokenization would make `</script marker>` (with a non-breaking space) inside a `<script>` or `<style>` body close the tag early and throw. That text is body text, both before this PR and in browsers.

## What's next? Any followup issues?

These cases still differ from the HTML tokenizer. None of them changed in this PR:
- a quote inside an attribute name or unquoted value (`title=Don't`)
- `a==b` and `a=b=c` should give the values `=b` and `b=c`
- `a/b` should split into `a` and `b`

## Tophatting

- New specs in `html.test.ts`: whitespace on either side of `=`, newlines around `=`, unquoted values, attributes inside a Liquid branch, and NBSP close-tag candidates in `script` and `style`. Each fails without its fix.
- `tokenizer.test.ts` updated for the split whitespace tokens.
- `liquid-html-parser`, `prettier-plugin-liquid`, `theme-check-common` and `theme-language-server-common` pass locally (7,152 tests).
- Prettier now prints `data-ratio = 'x'` as `data-ratio='x'`. It used to break the attribute apart.

## Before you deploy

- [x] I included a patch bump `changeset`

🤖 Generated with [Claude Code](https://claude.com/claude-code)
