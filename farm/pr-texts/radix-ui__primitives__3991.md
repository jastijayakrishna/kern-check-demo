# perf: reduce forced style recalculations during modal open

### Description

Reduces forced style recalculations triggered during modal/dialog open by optimizing two hot paths:

**1. `FocusScope.isHidden()` — use `Element.checkVisibility()`**

```diff
 function isHidden(node, { upTo }) {
+  if (typeof node.checkVisibility === 'function') {
+    return !node.checkVisibility({ checkVisibilityCSS: true });
+  }
+  // fallback: per-ancestor getComputedStyle loop
   ...
 }
```

The per-ancestor `getComputedStyle` loop is expensive when body styles have been dirtied by `react-remove-scroll` / `DismissableLayer`. `checkVisibility()` performs a single native check for both `visibility: hidden` and `display: none` across the ancestor chain.

**2. `Presence.usePresence()` — cache `animationName` from layout/ref phase**

```diff
+  const mountAnimationNameRef = React.useRef<string | undefined>(undefined);

   // ref callback (commit phase, before passive effects)
   ref: useCallback((node) => {
     stylesRef.current = getComputedStyle(node);
+    mountAnimationNameRef.current = getAnimationName(stylesRef.current);
   }, [])

   // passive effect (after sibling effects may have dirtied body)
   useEffect(() => {
-    prevAnimationNameRef.current = getAnimationName(stylesRef.current);
+    prevAnimationNameRef.current = mountAnimationNameRef.current ?? getAnimationName(stylesRef.current);
+    mountAnimationNameRef.current = undefined;
   }, [state]);
```

By the time the passive effect runs, sibling effects (`react-remove-scroll`, `DismissableLayer`) have written inherited styles to `<body>`, invalidating style caches. Reading from the live `CSSStyleDeclaration` at that point forces a synchronous style recalculation. The fix captures the value eagerly during the commit phase when styles are still clean.

**Tests added:**
- `FocusScope`: verify `display: none` and `visibility: hidden` elements are skipped during tab navigation
- `Presence`: verify mount/unmount behavior and render-function children pass correct `isPresent` value

**Remaining reflow sources (external):** `react-remove-scroll` writing inherited CSS vars on body, `aria-hidden` walking the DOM. A future improvement could replace both with the native `inert` attribute.

Ref: https://github.com/radix-ui/primitives/issues/1634

Link to Devin session: https://app.devin.ai/sessions/eab354d202a141f7b4d4ae5642eec8b7
Requested by: @chaance
