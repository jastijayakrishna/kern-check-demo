# fix(payment): SSR-safe redirect on /payment/success (render-phase router.replace → 500)

## Problem

The payment-confirmation page `/payment/success` returns **HTTP 500 on SSR for all users**.

The page has no `getServerSideProps`, but `_app`'s `getInitialProps` forces SSR on every page — so it renders on the server before the current user is known. Its guard ran in the render body:

```js
if (cid !== customerId?.slice(-8)) {
  router.replace('/');   // called DURING the React render
  return null;
}
```

`next/router`'s `replace()` has **no router instance during server render**, so it throws `Error: No router instance found...` mid-render. Next then serves `/_error` → 500. Because `customerId` is `undefined` on SSR, `cid !== undefined` is always true, so the throwing branch fires on every request.

This is a generic Next.js pages-router pitfall: **never navigate during render** — SSR renders before the user is known, so the render-body guard fired and called `router.replace` during render.

## Fix

Move the guard into a client-only `useEffect` that runs only once the user has hydrated (`customerId` defined):

```js
useEffect(() => {
  if (customerId && cid && cid !== customerId.slice(-8)) router.replace('/');
}, [customerId, cid]);
```

The render stays pure and SSR-safe, showing the generic "Payment Complete!" success content (which contains no user-specific/private data). The security intent is preserved: a signed-in user whose customer-id suffix doesn't match `cid` is still redirected to `/`, now client-side after hydration.

## Tests

Adds browser-mode component tests (`success.browser.test.tsx`):
- **Regression:** rendering with an anonymous/undefined current user (the SSR condition) renders the success content and does **not** call `router.replace` during render. Fails against the old render-body guard, passes with the fix.
- An authed user whose customer-id suffix mismatches `cid` is redirected (`router.replace('/')`) from the effect.
- No redirect when `cid` matches, or when the user is anonymous.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
