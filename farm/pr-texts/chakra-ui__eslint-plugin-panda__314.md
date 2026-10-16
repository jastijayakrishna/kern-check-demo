# Add missing CSS logical shorthand properties to `compositeProperties`

- [x] Add missing CSS logical shorthand properties to `compositeProperties` in `plugin/src/utils/composite-properties.ts`
  - [x] Simple logical shorthands: `insetBlock`, `insetInline`, `marginBlock`, `marginInline`, `paddingBlock`, `paddingInline`, `scrollMarginBlock`, `scrollMarginInline`
  - [x] Border logical shorthands: `borderBlock`, `borderBlockColor`, `borderBlockStyle`, `borderBlockWidth`, `borderInline`, `borderInlineColor`, `borderInlineStyle`, `borderInlineWidth`
- [x] Reverted test changes per review feedback
- [x] Added changeset

<!-- START COPILOT ORIGINAL PROMPT -->



<details>

<summary>Original prompt</summary>

> 
> ----
> 
> *This section details on the original issue you should resolve*
> 
> <issue_title>`prefer-atomic-properties` and `prefer-composite-properties` do not handle CSS logical shorthand properties</issue_title>
> <issue_description>Several CSS logical shorthand properties are missing from `compositeProperties`, causing `prefer-atomic-properties` and `prefer-composite-properties` to not handle them correctly.
> 
> ## Missing properties
> 
> - `insetBlock` → `insetBlockStart`, `insetBlockEnd`
> - `insetInline` → `insetInlineStart`, `insetInlineEnd`
> - `marginBlock` → `marginBlockStart`, `marginBlockEnd`
> - `marginInline` → `marginInlineStart`, `marginInlineEnd`
> - `paddingBlock` → `paddingBlockStart`, `paddingBlockEnd`
> - `paddingInline` → `paddingInlineStart`, `paddingInlineEnd`
> - `scrollMarginBlock` → `scrollMarginBlockStart`, `scrollMarginBlockEnd`
> - `scrollMarginInline` → `scrollMarginInlineStart`, `scrollMarginInlineEnd`
> 
> ### Border logical shorthands
> 
> - `borderBlock` → `borderBlockWidth`, `borderBlockStyle`, `borderBlockColor`
> - `borderBlockColor` → `borderBlockStartColor`, `borderBlockEndColor`
> - `borderBlockStyle` → `borderBlockStartStyle`, `borderBlockEndStyle`
> - `borderBlockWidth` → `borderBlockStartWidth`, `borderBlockEndWidth`
> - `borderInline` → `borderInlineWidth`, `borderInlineStyle`, `borderInlineColor`
> - `borderInlineColor` → `borderInlineStartColor`, `borderInlineEndColor`
> - `borderInlineStyle` → `borderInlineStartStyle`, `borderInlineEndStyle`
> - `borderInlineWidth` → `borderInlineStartWidth`, `borderInlineEndWidth`
> 
> ## Example
> 
> With `prefer-atomic-properties` enabled, the following should be flagged but is not:
> 
> ```ts
> // Should warn: use `marginBlockStart` and `marginBlockEnd` instead
> css({ marginBlock: '4 8' })
> ```
> 
> ## UX concern
> 
> If `borderBlockWidth`, `borderBlockStyle`, and `borderBlockColor` (and their `borderInline*` counterparts) were also registered as composite keys, `prefer-atomic-properties` would flag them at two levels:
> 
> 1. `borderBlock` is flagged → suggests replacing with `borderBlockWidth`, `borderBlockStyle`, `borderBlockColor`
> 2. Each of those would then be flagged again → suggests replacing with their `Start`/`End` variants
> 
> While this would correctly reflect the CSS shorthand hierarchy, it may feel overly granular in practice.</issue_description>
> 
> ## Comments on the Issue (you are @copilot in this section)
> 
> <comments>
> </comments>
> 


</details>



<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes chakra-ui/eslint-plugin-panda#307

<!-- START COPILOT CODING AGENT TIPS -->
---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
