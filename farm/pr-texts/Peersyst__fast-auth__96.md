# landing: NEARauth rebrand + social-login positioning + SEO infra + Lighthouse fixes

## Why

Reposition the public landing on https://auth.near.org/ around what NEAR dApp builders actually search for — *"Sign in with Google or Apple on NEAR · social-login Web3 onboarding"* (the Privy / Reown / Web3Auth space, but NEAR-native and non-custodial via MPC) — back it with production-grade SEO and a Lighthouse-driven a11y/perf pass, **and roll out the NEARauth brand** (new shield logo + wordmark lockup, product renamed FastAuth → NEARauth).

Three commits, separated by intent so reviewers can read them independently.

## Changes 🛠️

### Commit 1 — `feat: pivot to social-login positioning, add SEO infra`
- **Copy** — Hero, WhatIs, and the FAQ source-of-truth (`lib/faq.ts`) lead with Google / Apple / passkey / email and frame the product as the NEAR-native equivalent of Privy / Reown / Web3Auth. Technical precision (Auth0, MPC, NEP-366, non-custodial) preserved.
- **Canonical** — fallback hardcoded to `https://auth.near.org` via a shared `lib/site-url.ts`; `NEXT_PUBLIC_SITE_URL` and Vercel env vars still take precedence.
- **JSON-LD** — four server-rendered blocks: `Organization`, `WebSite`, `SoftwareApplication` site-wide; `FAQPage` on `/`, generated from the same `FAQ_ITEMS` the visible UI consumes so on-page copy and indexed content cannot drift.
- **Metadata** — keywords, authors / creator / publisher, robots + googleBot directives, per-page openGraph / twitter cards, dedicated `/status` metadata.
- **New** — `app/sitemap.ts`, `app/robots.ts`, `lib/site-url.ts`, `lib/faq.ts`.

### Commit 2 — `fix: improve a11y, perf, and contrast per Lighthouse audit`
- **A11y** — FAQ `<summary>` wraps the question in `<h3>` with the +/- toggle as an `aria-hidden` sibling; footer `<h4>` → `<h3>` for a strictly-descending outline; exactly one `<main>` landmark; contrast lift for ink + status text tokens (all ≥ AA on the warm-cream canvas).
- **Perf** — `preconnect` + `dns-prefetch` to GTM; both GA `<Script>` tags moved to `lazyOnload`; modern `browserslist` added.

### Commit 3 — `feat: rebrand to NEARauth + address CodeRabbit review`
**Brand**
- New **shield mark** — the NEAR "N" knocked out of a security shield — in three variants (`nearauth-mark{,-mono,-inverted}.svg`), sourced verbatim from the design system (`preview/10_logo.html`); replaces the old FastAuth marks.
- Header and footer now use the **wordmark lockup**: the NEAR logotype (`components/NearLogotype.tsx`) + mint **`auth`**.
- **FastAuth → NEARauth** across all user-facing copy, metadata, JSON-LD, `lib/faq.ts`, and the social-login hero / sections. Code identifiers are intentionally preserved: `@fast-auth-near/*` packages, `FastAuthProvider` / `useFastAuth` / `IFastAuthProvider`, the `fast-auth.near` contract ids, `FASTAUTH_*` env vars, and the Halborn PDF URL.

**Review feedback (CodeRabbit) — resolved**
- `lib/site-url.ts` — env URL inputs are now **normalized**: `https://` is prepended when the scheme is missing (a bare `auth.near.org` no longer throws in `new URL()`), and the value is collapsed to `origin` so a trailing slash or stray path can't produce malformed joins like `//sitemap.xml`.
- `app/globals.css` — `--color-status-ok-text` (`#0F7049`) and `--color-status-warn-text` (`#845906`) darkened so **small status text clears WCAG AA (4.5:1) on the bg-pill composite**, not just on canvas (~4.94:1 ok, ~4.81:1 warn on the pills). Closes the residual sub-AA gap flagged on the status pills.

## How to test
- [ ] `pnpm --filter landing check-types` (clean)
- [ ] `pnpm --filter landing build` (6 static routes prerender: `/`, `/status`, `/robots.txt`, `/sitemap.xml`, …)
- [ ] Header / footer render the shield + `near` + mint `auth` lockup; favicon is the new mark.
- [ ] `.next/server/app/index.html`: 1 `<main>`, 4 `application/ld+json` blocks, `canonical = https://auth.near.org`, GA `<Script>`s `lazyOnload`, no `<h4>` orphan above the lowest `<h3>`.
- [ ] Set `NEXT_PUBLIC_SITE_URL=auth.near.org` (no scheme, trailing slash) → build still renders; canonical/og/sitemap r
