# ✨ feat: Sentry-branded feedback widget as the single always-on affordance + subtle beta badge

## What this does

A single, always-available, on-brand **feedback** button on every page, plus a **subtle Beta** indicator everywhere that keeps the Souso wordmark centered. Refines #404 (feedback) and #407 (beta badge).

### 1. Sentry user-feedback widget — branded, always on
- Wired Sentry's `feedbackIntegration` into `Sentry.init` (`src/lib/observability-client.ts`). It auto-injects a small button that hovers bottom-right on **every** page (landing + signed-in) and opens a short form.
- Souso theme via the integration options: mustard accent (`#e8a33d`) on cream/forest surfaces, Sentry branding hidden, plain-voice labels (`Feedback` trigger, "Tell us what you think", "Send feedback"), no required name/email so a beta tester can fire a quick note.
- The branding/copy is a pure exported helper `sousoFeedbackOptions()` so it's unit-testable without booting Sentry.
- **Guarded**: skips cleanly if the SDK build lacks `feedbackIntegration`, and the whole init is already prod-gated (`OBSERVABILITY_ENABLED`), so dev never crashes with Sentry off.

### 2. Reconciled with the custom bubble (#412)
- Removed the custom floating `FeedbackBubble` from `_authed.tsx` so the Sentry widget is the **single** bottom-right feedback affordance (no two competing widgets). Deleted the now-dead component.
- **Kept** the in-app feedback path: Settings "Send feedback" + `FeedbackForm` + the `app_feedback` table + admin inbox are untouched and still work (Settings opens the existing form, not the Sentry dialog).

### 3. Beta badge — subtle, every page, wordmark centered (#407)
- Restyled `BetaBadge` from the loud solid-mustard fill to a **subtle muted pill**: soft mustard tint + hairline mustard border + low-contrast text, smaller, in the warm sticky-note spirit of the home-page tagline tag.
- Repositioned under the **centered** wordmark on the landing hero and onboarding welcome board (column layout) so the mark stays dead-centre. Kept beside the title in `ScreenHeader` so it shows on every signed-in screen.

## Tests
- `beta-badge.test.tsx`: locks the subtle styling (muted tint, not the old solid fill) + existing label/copy guards.
- `observability-client.test.ts`: locks the feedback config (brand palette, plain copy, no em/en dashes, short form). Render/no-crash level for the prod-gated wiring.

## Gate
`pnpm quality` green locally (format + lint + typecheck + build + 1356 tests). Pre-push gate green.

## Caveats
- `@sentry/react@10.59.0` does **not** re-export `feedbackIntegration` from its own entry; it re-exports `* from '@sentry/browser'`, which does export `feedbackIntegration` + `getFeedback` (confirmed in the installed build's types). The call is `Sentry.feedbackIntegration(...)` and is wrapped in a `typeof === 'function'` guard as a belt-and-braces against a future SDK build dropping it.

Refs #404, #407.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
