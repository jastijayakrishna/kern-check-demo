# fix(tenant): restore Account / Sign out on partner subdomains (#2150)

Fixes #2150 — the half the issue flagged as *"higher-priority"* and *"should be confirmed"*. Now confirmed, and fixed.

## Confirmed live

The issue asked whether signed-in users on a tenant subdomain have any account control. They do not. Checked 2026-07-27 against the **hydrated** DOM of `bph.sourcelibrary.org/book/aurora-consurgens-…`, in a browser holding a **valid session** (`/api/auth/session` → `dereklomas@gmail.com`):

```
headerPresent:     false
navHrefs:          null
embedUserMenu:     false
authAffordances:   []      ← zero sign-in/out/account controls anywhere on the page
```

A signed-in reader on a partner subdomain is stranded: no Account, no Sign out, on any page.

## Why it hid for two months

Two individually-correct behaviours compose into the gap, and **`curl` cannot see it** — the server HTML still contains a header, which is removed only after hydration.

After the tenant-as-filter migration a partner subdomain serves the **global** routes directly (`src/proxy.ts` rewrites only `/`, `/catalogue*`, `/catalog/*`). So on `/book/<slug>`:

1. `src/app/embed/layout.tsx` never runs — and it is the **only** mount point for `EmbedUserMenu`, which its own header comment calls *"the only sign-out affordance"* for surfaces where the SiteHeader is stripped;
2. `ConditionalSiteHeader` then strips the SiteHeader post-hydration on a tenant host, taking the header's account control with it.

## The fix

Mount the menu from the **root layout**, client-gated, in a new `account-only` variant.

- **Root layout, not a tenant layout.** Reading `headers()` there would force dynamic rendering and blank the book page's ISR cache (`revalidate = 86400`) — the same constraint that already makes site-mode detection client-side. `useEmbedContext` resolves the host in a post-mount effect, so server HTML stays host-agnostic and cacheable.
- **`account-only` renders nothing for anonymous visitors**, and omits the view-options toggles and BPH catalogue search. Anonymous BPH pages are byte-identical to today. Restoring auth is a bug fix; putting the toggles back is a **separate product decision** (2026-05-28: BPH is deliberately "hidden, no toggle"), so this deliberately does not reopen it — the plumbing is there to flip later.
- **`/embed/*` untouched** — it still mounts the full menu from its own layout, and `TenantAccountMenu` returns `null` there so the two never stack.

## Guard

`tests/unit/tenant-account-menu.test.ts` pins each link in the chain: root-layout mount, inside `<Providers>`, no `next/headers` in the root layout, no double-mount on `/embed/*`, anonymous renders nothing, toggles stay out, Account + Sign out still present. Removing any one restores the bug silently.

725 unit tests pass; `npx tsc --noEmit` clean.

## Verification — read this before approving

**A Vercel preview cannot verify this.** Two independent reasons:

1. CLAUDE.md's known trap — curling a preview with `Host: bph.sourcelibrary.org` makes Vercel's router serve the **production** deployment for that domain, producing a convincing false result.
2. The gate is `isTenantSubdomain(window.location.host)`, and a preview host is `sourcelibrary-v2-git-….vercel.app` — not a `.sourcelibrary.org` subdomain, so the menu correctly does not mount there regardless.

What the preview **can** confirm, and what I'll check on it: `/embed/bph/*` still shows exactly one floating menu, and the apex site is unchanged.

The tenant path must be verified **after deploy, on the real subdomain, while signed in** — same method as the confirmation above. I can run that check once it ships.

## Out of scope

- The view-options toggles on tenant pages (product decision above).
- `EmbedUserMenu`'s `navigateToAccount` comment is now stale — it says the proxy rewrites *every* non-`/embed/` path, which stopped being true. Its behaviour (routing `/account` to the apex, where the shared `.sourcelibrary.org` cookie carries the session) is still correct, so I left it alone rather than widen 
