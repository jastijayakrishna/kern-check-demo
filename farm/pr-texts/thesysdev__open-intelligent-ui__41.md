# Add PostHog analytics to the deployed demo

## Summary
Adds PostHog to the deployed demo. `<Analytics />` (`src/app/analytics.tsx`, rendered in the root layout) lazy-imports `posthog-js` and calls `posthog.init` only when both hold:

```ts
process.env.NODE_ENV === "production" && process.env.NEXT_PUBLIC_POSTHOG_KEY
```

`NEXT_PUBLIC_POSTHOG_HOST` sets `api_host` when present (PostHog's default otherwise). Both are documented, commented out, in `.env.example`. Without the key, nothing loads, so local dev and clones send nothing. Config matches the openui.com site: `capture_pageview: "history_change"`, session recording sampled at 0.3, surveys off.

To enable it on the deployment, set `NEXT_PUBLIC_POSTHOG_KEY` (and `NEXT_PUBLIC_POSTHOG_HOST`) on the Vercel project and redeploy. These are inlined at build time.

Verified with a production build under the base path: with the env vars set, `posthog-js` loads and calls `/flags/` and the project config on the configured host.

Link to Devin session: https://app.devin.ai/sessions/e883019c60e74de7b8c38fe3a9198442
Open in Devin Desktop: https://app.devin.ai/desktop/session/e883019c60e74de7b8c38fe3a9198442?variant=devin
