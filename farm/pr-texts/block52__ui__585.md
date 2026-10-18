# Reduce dead space below nav header on home page

The home page had excessive vertical whitespace between the fixed navigation header and the main content panels (Game Wallet, Recent Transactions, Available Tables), as visible in the screenshot above.

## Change

- **`src/pages/Dashboard.tsx`**: Reduced top margin on the main content container from `mt-8 sm:mt-12 lg:mt-16` → `mt-2 sm:mt-4 lg:mt-6`

```diff
- <div className="w-full max-w-[1600px] mx-auto px-4 sm:px-6 lg:px-8 z-10 mt-8 sm:mt-12 lg:mt-16">
+ <div className="w-full max-w-[1600px] mx-auto px-4 sm:px-6 lg:px-8 z-10 mt-2 sm:mt-4 lg:mt-6">
```

<!-- START COPILOT CODING AGENT SUFFIX -->

- Fixes #584
