# fix(seo): a favicon that is visible in both browser chromes (#12)

Closes #12's remaining half.

## The premise was inverted

The title says *"black mark invisible on dark browser chrome — use the white version"*. Measured against the live site:

```
favicon.ico, 32x32 frame, opaque pixels only
    0- 95 :    0        ← zero dark pixels
   96-127 :    3
  128-159 :   55
  160-255 :  933
mean 228 / 255 · corner alpha 0
```

**It is already the white version**, on transparency — so it disappears against a **light** tab strip, which is the default in Chrome, Safari and Firefox on a light desktop theme.

`apple-touch-icon.png` is its opposite and its answer: fully opaque, mean luminance **4.8**, with 1.5% of its pixels above 159 — a light mark on a near-black tile. A solid tile reads against either chrome, which is exactly why iOS home-screen icons are built that way.

**Both marks already existed.** Each is right for one chrome. `media` picks between them.

## Order is deliberate

Safari **ignores `media` on icon links** and takes the first entry it can use. So the first entry has to be the one that is safe when nobody is choosing — the opaque tile, legible on both. The white mark follows, behind `(prefers-color-scheme: dark)`.

## And the part that makes it work

**`app/favicon.ico` → `public/favicon.ico`.**

Next's file convention emits its own `<link rel="icon">` **before** anything from `metadata.icons`. While that file sat in `app/`, the rendered head began with the white-on-transparent mark and everything below it was decoration — the media split would have shipped and changed nothing.

It also explains the duplicate `/favicon.ico` I noticed on the live site earlier and filed as "untidy": it was load-bearing.

`public/favicon.ico` serves the same URL as a plain static asset and injects nothing. Verified in the built output:

```html
<link rel="icon" href="/apple-touch-icon.png" type="image/png" sizes="180x180"/>
<link rel="icon" href="/favicon.ico" sizes="32x32" media="(prefers-color-scheme: dark)"/>
<link rel="icon" href="/icon.png" type="image/png" sizes="512x512"/>
<link rel="apple-touch-icon" href="/apple-touch-icon.png"/>
```

## Tests — 8 new, 16 in the file

Three check the **filesystem**, because dropping `favicon.ico` back into `app/` would silently restore the bug with every other assertion still green. Proven by doing exactly that: **2 failed**.

One of them allows `app/icon.png` deliberately — it *is* the list's last entry, so the convention and the metadata agree. The rule reads as *"do not let an unlisted icon jump the queue"*, not *"never use the convention"*.

## What would still be better

A purpose-built `.ico` with 16 and 32 px frames on an opaque ground. `apple-touch-icon.png` is 180px and the browser downscales it, and a mark covering 1.5% of the tile is thin at 16px.

That needs someone who can author the brand mark. This uses only what the brand already ships — and **a faint-but-present icon beats one that vanishes**.

640 tests passing. `next build` clean.

Ships `minirue-frontend@0.52.1`.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01B6eD4Vf5YMMKKBaxyL2w5q
