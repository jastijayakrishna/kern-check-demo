# Remove icons from file access context menu

## Context

Per UX research (Nielsen Norman Group, McDougall et al.), non-standardized icons in dense menus increase cognitive load and slow scanning — users end up reading the text labels anyway. Removing them improves readability.

## Changes

- Stripped all `iconProps` from every item in `useFileAccessContextMenu.ts`: `Expand all`, `Collapse all`, `Open`, `Open with`, `Save metadata as`, `Process files`, `Edit metadata`, `Copy to vast`, `Download`

**Before:**
```ts
{
    key: "download",
    text: "Download",
    iconProps: { iconName: "Download" },
    onClick() { ... },
}
```
**After:**
```ts
{
    key: "download",
    text: "Download",
    onClick() { ... },
}
```

## Testing

Manually verified the context menu renders text-only items without icons.

<!-- ## Screenshots (if relevant) -->
