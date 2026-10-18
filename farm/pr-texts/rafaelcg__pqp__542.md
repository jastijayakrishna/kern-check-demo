# Server header: say the name once, label the actions

## Summary

The channel sidebar header drew the server's name three times (inside the banner image, over the banner, and again in the row below) with an unlabelled, untranslated role next to an unlabelled icon row — the exact shape the owner flagged as "very confusing" from a screenshot of "QG do pqp".

**Before**
- Banner (if set) draws the name over the image.
- A second, separate row below repeats the name, truncated to one line ("QG do..." on a narrow sidebar).
- The role shows as the raw wire value (`"owner"`), CSS-uppercased into "OWNER" — not translated, not labelled.
- Four icon buttons (settings, members, invite, collapse) with tooltips but no dedicated a11y test coverage.

**After**
- One header block. `ServerHeaderBanner` (`client/src/components/layout/server-identity.tsx`) draws the server's banner as this row's *background* when it has one — icon, name, role and actions sit inside it — and the row's ordinary background otherwise (or when the image 404s after mount, so a load failure never takes the content off screen with it). The name is drawn exactly once, regardless.
- The name wraps to two lines (`line-clamp-2`) instead of truncating to one — "QG do pqp" no longer collapses to "QG...".
- The role reads a word: `compatRoleLabel` (`client/src/lib/role-labels.ts`) borrows "Owner"/"Admin" from the same translation the roles editor already uses, and "Member" gets its own key (`chrome.role.member`, en + pt-BR).
- Fixed a real contrast bug while building this: the banner-overlay text used the theme-relative `text-paper` role, which is dark ink in a light theme — over a photo that's dark text sitting on the same dark scrim used to keep it legible. Verified locally against a real banner image in both light and dark colour schemes. Switched both this header and `ServerBanner`'s own name (used by the settings-dialog banner preview) to a literal `text-white` with a drop shadow, matching the same treatment `landing-page.tsx` / `marketing-nav.tsx` already use over their own hero photography.
- Settings, Members, Invite and Collapse/Close keep their existing `Tooltip` wrappers, which is what actually puts the `aria-label` on each button (`tooltip.tsx`) — visible bubble and accessible name share one source.
- Considered moving Settings/Invite into a dropdown to cap the row at three icons, but there's no click-triggered dropdown primitive in `ui/` yet (`docs/DESIGN.md` lists "Menu" as a planned primitive), and four separate e2e specs (`server-identity.spec.ts`, `communities.spec.ts`, `server-settings-sections.spec.ts`, `issue-71-review.spec.ts`) click the persistent "Community settings" button directly. Kept all four visible rather than take on that risk in a header-clarity fix; the header's own right-click context menu already offers Settings/Invite/Members as a secondary path.

## Test plan

- [x] `pnpm --filter @pqp/client exec tsc --noEmit`
- [x] `pnpm exec eslint` on every touched file
- [x] `pnpm exec vitest run` on the new `channel-list-header.test.tsx` plus every touched/adjacent `channel-list-*.test.tsx`, `server-identity.test.tsx`, `role-labels.test.ts` — 78 passing
- [x] `pnpm --filter @pqp/client bench:tokens` — contrast 800/800, 0 leaks, 0 ui aliases/statics, 0 token drift
- [x] `pnpm --filter @pqp/client run i18n:check`
- [x] Manually verified against a running local stack (dev auth bypass + a real banner image) at desktop width, a long server name, and the 390px mobile drawer, in both light and dark colour schemes — confirmed the name draws once, wraps to two lines, and the banner-overlay text is legible in both themes.
- [ ] `client/e2e/server-identity.spec.ts` and the other sidebar/server e2e specs (not run here — no `S3_*` configured for the upload half; the no-storage half's selectors are unchanged by this PR)

client-only, no API restart.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01LptYkv7RTzV6WVQNEWNYUv
