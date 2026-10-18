# fix(seo): collapse the locale URLs onto their canonical paths

Implements Step 5b — collapse every locale-prefixed URL onto its canonical path.

## Why

`app/[locale]` was scaffolding for an internationalisation that never happened. `next-intl` is installed but **never imported**, so `/en`, `/es` and `/fr` render byte-identical English — duplicate content on three extra URLs per page.

They are orphans: grepping `app/` and `components/` for locale-prefixed `href`s returns **nothing**, and `public/sitemap.xml` already lists only the five canonical URLs.

## The rules

Two rules cover the whole 15-path set (3 locales × 5 pages), and keep covering it if a page is added under `[locale]` later:

```js
{ source: "/:locale(en|es|fr)",        destination: "/",       statusCode: 301 },
{ source: "/:locale(en|es|fr)/:path*", destination: "/:path*", statusCode: 301 },
```

**301, not `permanent: true`** — Next emits **308** for `permanent`, while the redirects already in `staticwebapp.config.json` (`/about`, `/solutions`, `/contact`) are 301. One status code for every redirect on the site.

## The scaffolding stays, deliberately

`[locale]` still builds. If `redirects()` turns out not to fire on the SWA hybrid adapter, those pages **keep serving exactly as they do today rather than 404ing** — the failure mode is "no change," not "pages disappear."

Emptying `generateStaticParams` belongs in a follow-up, once production has proven the redirects fire. Doing both at once would mean a failed rung 1 leaves `/en` worse than it started.

That caution isn't theoretical: `globalHeaders` in `staticwebapp.config.json` were **silently ignored by this same adapter**, which is why the site served no CSP at all until #34.

## The ladder, made self-reporting

Rung 1 is `redirects()` — **unproven on this adapter**. So the post-deployment step now asserts the redirects against production and **fails the build if they don't fire**, naming rung 2 in the failure message:

> `next.config.js redirects() is not honoured by the Static Web Apps hybrid adapter. Move these to routes[] in staticwebapp.config.json, which is the proven mechanism on this deployment.`

**If this PR's deploy goes red on that section, rung 1 doesn't work and rung 2 is the next commit.** That is the ladder executing as designed, not a broken PR.

It also confirms the canonical paths still return 200 — a rule that matched them would loop.

## Verification

Built the production bundle and served it locally on port 3111:

| Path | Result |
|---|---|
| `/en`, `/es`, `/fr` | **301 → `/`** |
| `/en/terms` | **301 → `/terms`** |
| `/es/privacy` | **301 → `/privacy`** |
| `/fr/product-terms` | **301 → `/product-terms`** |
| `/en/engagement-terms` | **301 → `/engagement-terms`** |
| `/`, `/terms`, `/privacy`, `/product-terms`, `/engagement-terms` | **200**, no loop |
| `/banana` | **404**, unchanged |

| Check | Result |
|---|---|
| New unit tests over the redirect declaration | 6 passed |
| Full suite | **116 passed / 1 skipped** (was 110/1) |
| `bash -n`, `shellcheck -s bash` on the verification step | clean |
| `npm run validate` | 6/6 gates |

`tsc` rejected the first version of one assertion (`permanent` is absent from the inferred type), which is the type-checker doing its job — the assertion now reads through an index signature.

## Known unrelated issue this does not address

`/fr` currently returns **404** in production while `/en` and `/es` return 200 — noticed during last night's verification. I could not determine whether that is new. After this lands, all three 301 regardless, so the inconsistency stops mattering for users; it is still worth understanding.

## Not changed

No page content, no copy, no security headers, no CSP, no API behaviour, no Azure resources, and no governing-law, venue, or dispute-resolution language. `public/sitemap.xml` needed no edit.

## Relationship to #40 and #41

All three touch `cost-optimized-ci.yml` in different regions. Whichever merges later may need a trivial `gh pr update-branch`.

🤖 Generated with [Claude Code
