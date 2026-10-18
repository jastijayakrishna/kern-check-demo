# perf(storefront): product images go straight to imgproxy (#7)

Closes the frontend half of #7. Pairs with minirue-backend#76 — **that one merges first**.

## The finding

#7 listed five suspected causes, all JS-shaped, and all five were already in place.
So I measured instead of guessing. Playwright's own Chromium, Pixel 5 emulation,
4× CPU throttle, Slow 4G, cold cache, median of three runs against the live
product page:

```
LCP  3732 ms   (4308 / 3732 / 3628)
FCP  1988 ms
TTFB  183 ms
CLS  0.0014      long tasks 8      scripts 22      JS 358 KB
```

The LCP candidate chain is the whole story:

```
2680 ms   <P>
3744 ms   <IMG>   /_next/image?url=https%3A%2F%2Fimg.minirueshop.com%2F...
```

**LCP here is image-bound, not JS-bound.** Text painted at 2.7s; the page then
waited another full second for one image. No amount of bundle work moves a number
that is gated on an image request.

## Why that image was slow

`media.url` was ONE fixed imgproxy render. `next/image` cannot build a srcset from
a single URL, so it proxied the image through `/_next/image` instead:

```
browser -> Next server -> imgproxy -> Garage
```

plus a server-side re-encode at `q=75` of something imgproxy had already produced
at `q=95`. Two round trips and two encodes, on the critical path of the largest
element on the page.

The hero already avoids this (#29): it gets a pre-signed `imageSrcSet` and a custom
loader, so Next proxies nothing. Product images never got the same treatment.

## Why the server has to send the widths

An imgproxy URL is **signed**. The frontend cannot generate a width of its own —
`mediaImageUrl` just returns `media.url`. That is why the hero needed a map rather
than a pattern, and why this does too. minirue-backend#76 adds `srcSet` to product
media; this reads it.

## Verification

Against a local stub emitting the #76 shape, served from `node .next/standalone/server.js`
— `next start` silently does not serve an `output: standalone` build, which invalidated
an earlier check of mine:

| | before | after |
|---|---|---|
| `/_next/image` references on the page | 19 | **0** |
| `<link rel=preload imageSrcSet>` | `/_next/image?…&q=75` | imgproxy direct |
| rungs offered | Next's ladder, re-encoded | the 4 server-signed ones |

All 19 belonged to that one image. The preload link is the one that matters — it is
what the preload scanner acts on, so it sets the LCP request's start time.

## Deploy order is safe in both directions

Where the backend has not shipped #76, the fallback is **nothing**: the `/_next/image`
path stays exactly as it is today.

This is the one place the hero's rule does not transfer, and the tests pin the
difference. `unoptimized` was already the hero's behaviour, so falling back to it there
changes nothing. Here the status quo does emit a real srcset, so falling back to
`unoptimized` would hand a 390px phone the full 1400×1750 render — a regression paid by
exactly the clients the fix has not reached yet, in exchange for nothing.

## Also

`hero-loader.ts` → `imgproxy-loader.ts`, `heroImageLoader` → `imgproxyLoader`. Nothing in
it was ever hero-specific, and a name describing one caller sends the next reader looking
for a rule that is not there.

## Checks

- 644 tests pass (106 suites)
- `tsc --noEmit` clean
- `eslint --no-fix` clean on changed files

`minirue-frontend@0.53.0`

### Not closed by this

The after-measurement. It can only be taken once **both** halves deploy, so I will
re-run the same script and post the delta to #7 rather than assert an improvement I
have not observed end to end.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01B6eD4Vf5YMMKKBaxyL2w5q

