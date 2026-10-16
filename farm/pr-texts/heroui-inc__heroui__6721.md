# fix(spinner): move accessible name from hidden svg to root status role

Closes #6718

As discussed in https://github.com/heroui-inc/heroui/issues/6718#issuecomment-5009662783.

## 📝 Description

`Spinner` currently renders its inner SVG with contradictory accessibility attributes:

```tsx
<SpinnerPrimitive aria-hidden aria-label="Loading" role="presentation" />
```

- `aria-label` on an `aria-hidden` element is dead code, and `role="presentation"` is a naming-prohibited role, so axe flags `aria-prohibited-attr`.
- Since the only labeled element is hidden and the root `<span data-slot="spinner">` has no role or name, the spinner is entirely absent from the accessibility tree — screen reader users get no indication anything is loading.

## ⛳️ Current behavior (updates)

The spinner subtree is invisible to assistive technology, and axe reports `aria-prohibited-attr` on the SVG.

## 🚀 New behavior

- The decorative SVG is plainly `aria-hidden` with no name.
- The root element gets `role="status"` and `aria-label="Loading"`, so the spinner is announced as a live status region.
- Both attributes are placed **before** the props spread, so consumers can still override them (localize the label, or opt out entirely when a parent already announces loading, e.g. `aria-hidden` on nested usages).

```tsx
<dom.span
  aria-label="Loading"
  data-slot="spinner"
  role="status"
  {...(props as any)}
  ...
>
  <SpinnerPrimitive aria-hidden />
</dom.span>
```

## 💣 Is this a breaking change (Yes/No):

No

## 📝 Additional Information

This is exactly the diff proposed in the issue, which @wingkwong greenlit for a PR. `pnpm lint` and `pnpm typecheck` pass on the change. The repo has no test infrastructure yet ("No tests yet" per AGENTS.md), so no test accompanies it; happy to add one if/when a test setup lands.


🤖 Generated with [Claude Code](https://claude.com/claude-code)
