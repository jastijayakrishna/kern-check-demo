# Tooltip: Allow multiple children without manual Box wrapping

Enhanced the Tooltip component to automatically handle multiple children, eliminating the need for users to manually wrap them in a `<Box>` component.

## Problem

Previously, users who wanted to place multiple components (like `<Inline>` and `<Text>`) inside a tooltip trigger had to manually wrap them in a `<Box>`:

```tsx
// Before: Required manual wrapping
<Tooltip label="Tooltip text">
  <Box>
    <Inline>
      <Text>First</Text>
      <Text>Second</Text>
    </Inline>
    <Text>Additional text</Text>
  </Box>
</Tooltip>
```

This was because the Tooltip component used `Children.only()` which enforced exactly one child element.

## Solution

Now users can place multiple children directly without any wrapper:

```tsx
// After: Multiple children work automatically
<Tooltip label="Tooltip text">
  <Inline>
    <Text>First</Text>
    <Text>Second</Text>
  </Inline>
  <Text>Additional text</Text>
</Tooltip>
```

## Implementation Details

- **Type Update**: Changed `children: ReactElement` to `children: ReactNode` to accept multiple children
- **Smart Wrapping**: Single children use the existing logic (backwards compatible), while multiple children are automatically wrapped in a `<span>` that receives the necessary event handlers and ref
- **Full Backwards Compatibility**: All existing single-child usage continues to work exactly as before

## Testing

Added comprehensive tests covering:
- Single child backwards compatibility
- Multiple children rendering and interaction
- Real-world scenarios with Inline and Text components
- Edge cases (empty labels, etc.)

Fixes #1110.

---

💡 You can make Copilot smarter by setting up custom instructions, customizing its development environment and configuring Model Context Protocol (MCP) servers. Learn more [Copilot coding agent tips](https://gh.io/copilot-coding-agent-tips) in the docs.
