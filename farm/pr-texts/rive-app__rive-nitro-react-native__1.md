# fix: stabilize property setter functions by using global options & fix ci

## Summary

This PR fixes the issue where property setter functions from `useRive*` hooks were unstable, causing unnecessary re-renders.

### Changes
- Extract options objects to global constants in `useRiveBoolean`, `useRiveNumber`, `useRiveString`, and `useRiveColor`
- Use `useMemo` in `useRiveTrigger` to recreate options only when `onTrigger` changes
- Remove unnecessary `useCallback` imports where no longer needed
- fixed GitHub actions  (yarn nitrogen was missing from few places)

### Problem
Property setter functions (setValue, setButtonText, etc.) were unstable because the options object passed to `useRiveProperty` was recreated on each render, even though `useCallback` was used for the `getProperty` function. This caused the `useMemo` and `useEffect` in `useRiveProperty` to re-run unnecessarily, resetting listeners and creating instability.

### Solution
By extracting the options to global constants, we ensure stable object references across renders. For `useRiveTrigger`, which has a dynamic `onTrigger` parameter, we use `useMemo` to only recreate the options when `onTrigger` actually changes.

## Test plan
To reproduce the issue: In [example/src/pages/RiveDataBindingExample.tsx](https://github.com/rive-app/rive-nitro-react-native/blob/main/example/src/pages/RiveDataBindingExample.tsx), apply this diff:

```diff
diff --git a/example/src/pages/RiveDataBindingExample.tsx b/example/src/pages/RiveDataBindingExample.tsx
index 76b2f60..039236c 100644
--- a/example/src/pages/RiveDataBindingExample.tsx
+++ b/example/src/pages/RiveDataBindingExample.tsx
@@ -1,4 +1,4 @@
-import { View, Text, StyleSheet, ActivityIndicator } from 'react-native';
+import { View, Text, StyleSheet, ActivityIndicator, Button } from 'react-native';
 import { useState, useEffect } from 'react';
 import {
   Fit,
@@ -152,6 +152,10 @@ export default function DataBindingExample() {
             hybridRef={setHybridRef}
           />
         )}
+        <Button
+          title="Change button"
+          onPress={() => setButtonText('New Button Text')}
+        />
       </View>
     </View>
   );
```
pressing the change button should change the button for good. Previously it was changed, but changed back immediately

🤖 Generated with [Claude Code](https://claude.com/claude-code)
