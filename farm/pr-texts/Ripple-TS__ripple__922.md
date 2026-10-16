# [Prettier]: prefer to break all JSX attributes instead of breaking an expression

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

When an attribute value contains a breaking expression (e.g. multiline object literal, long ternary), the Prettier plugin now prefers breaking all attributes onto separate lines rather than keeping some attributes on the same line as the tag name and breaking the expression value inline.

## Before

```tsx
<div class={styles.item} data-active={state.active ? "true" : "false"} style={{
  gridTemplateColumns: Icon ? "16px minmax(0, 1fr) auto" : "minmax(0, 1fr) auto",
}}>
```

## After

```tsx
<div
  class={styles.item}
  data-active={state.active ? "true" : "false"}
  style={{
    gridTemplateColumns: Icon ? "16px minmax(0, 1fr) auto" : "minmax(0, 1fr) auto",
  }}
>
```

This makes element hierarchy easier to identify at a glance.

## Implementation

In `printElement()`, after printing each attribute doc, we check if any attribute value would cause a line break using Prettier's `willBreak()` utility. If any attribute breaks, we add `breakParent` to the opening tag group, forcing all attributes to break onto separate lines.

Non-breaking attribute lists remain unaffected — they still respect `printWidth` to decide whether to break.

## Tests

Added 3 new tests:
- Breaking with multiline object attribute value
- Breaking with multiline object + `bracketSameLine: true`
- Non-breaking attributes remain on the same line
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-011e7d4a-6258-4d24-bdc6-f10cc54ae4b0"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-011e7d4a-6258-4d24-bdc6-f10cc54ae4b0"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
