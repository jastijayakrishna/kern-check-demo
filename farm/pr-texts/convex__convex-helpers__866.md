# Add vRequired / VRequired utils in validators.ts

## Summary

Adds `vRequired` function and `VRequired` type to `validators.ts` as requested in #847. These utilities convert optional validators to required validators, serving as the inverse of `v.optional()`.

The implementation was extracted from the Zod 4 integration (PR #840) to make it available as a general-purpose utility.

**New exports:**
- `VRequired<T>` - Type-level conversion from optional to required validator
- `vRequired(validator)` - Runtime function to convert optional validators to required

**Example usage:**
```ts
const optionalString = v.optional(v.string());
const requiredString = vRequired(optionalString); // v.string()

// Already required validators are returned as-is
const alreadyRequired = v.string();
const stillRequired = vRequired(alreadyRequired); // v.string()
```

Closes #847
