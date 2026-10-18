# P0: drop httpOnly from the Supabase auth cookies middleware writes back

`FILTER: ADVANCE-F1-SURFACE — cat {F1-SURFACE} — fences {clear} — locks {clear} — redirect: n/a`

Fixes the P0 from #228 (`a42589b`): `/dashboard` renders a blank white screen for signed-in users, with no layout and **no redirect to `/login`**.

**Net diff against `main`: one deleted line, plus a comment explaining why it must stay deleted.**

## Cause

Not the CSP — the middleware's Supabase cookie handling. It forces `httpOnly: true` on every cookie Supabase sets.

`@supabase/ssr`'s **browser** client reads the auth token from `document.cookie`. Once middleware refreshes a session and writes those cookies back httpOnly, client-side JS goes permanently blind to them — while the **server** still sees a valid session.

That asymmetry is exactly the reported symptom: middleware considers you authenticated so it passes you through (**no redirect**), while the client considers you signed out and the page dies from there.

This code is not new. It has sat in `middleware.ts` for a long time, but Next never loaded the file while it lived at the repo root — #228 moved it into `src/`, which switched it on for every protected route.

## Relationship to #238

#238 rewrote this same block to `getAll`/`setAll`, fixing the *other* latent defect here (a chunked session read as "no user"). That was a real fix and this PR keeps it — but it carried `httpOnly: true` through unchanged, so the blank dashboard survives on current `main`. This PR removes only that line and leaves #238's `getAll`/`setAll`, `secure`/`sameSite`/`path` handling, and comments intact.

## Verification

Merged with `main` (`0f81e3d`), against a production build (`next build` + `next start`):

- anonymous `/dashboard` → 307 to `/login` (auth gate intact)
- CSP unchanged, 20/20 script tags nonce-stamped
- chunked/garbage auth cookies redirect cleanly instead of 500ing
- `/pdf.worker.min.mjs` 200 same-origin
- `npm run check:bff` OK, build clean, 968 tests pass

**Not verified:** the signed-in path, which needs real Supabase credentials. Please confirm a signed-in `/dashboard` load on the preview before promoting.

## Caveat worth a reviewer's eye

The httpOnly defect is certain and would definitely break client-side auth. I am less certain it accounts for the *entire* blank screen: `DashboardShell` renders its header unconditionally and is server-rendered, so a lost client session alone should still paint a header. The total blank suggests a client component *also* throws on the null session — `DashboardHeader` and `DashboardSpeakerSexPrompt` are the candidates. A browser console error from a signed-in `/dashboard` load would settle it.
