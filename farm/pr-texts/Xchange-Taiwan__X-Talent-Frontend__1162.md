# refactor(reservation): simplify booking panel gating per product feedback (X-Tracker #712)

## What Does This PR Do?

Follow-up to #1161 (already merged), based on product feedback on that PR: what happens when a mentor has no availability *this* month but does open up two months from now?

- Removed the **瀏覽其他導師** CTA from the no-availability empty state. The calendar above the form is still fully navigable, so a mentor who opens up in a later month is one page-flip away - a CTA nudging people toward other mentors would undersell that. The empty state is now a plain text notice pointing at switching months.
- The question textarea is now gated on **`!selectedSlot`** instead of on `hasNoAvailabilityThisMonth`. This is a strictly more general rule: it already covers the empty-month case (nothing selectable, so it stays disabled), and it now also correctly covers a mentor who has slots this month but simply hasn't had one picked yet - no separate month-based logic needed.
- Removed the dedicated sign-in-prompt screen; `!isAuthenticated` goes back into the submit button's disabled condition (original behavior), rather than swapping out the whole form.

**Files changed:**
- `src/components/profile/reservation/MenteeBookingForm.tsx`
- `src/components/profile/reservation/BookingForm.test.tsx`

## Screenshot

![Visitor - no-availability state (no CTA)](https://raw.githubusercontent.com/Xchange-Taiwan/X-Talent-Frontend/1a764798f331f8f2e8a1d329bb04196d2af6c9c9/feat-712-mentor-booking-empty-state/20260911T213350Z/0-visitor-desktop-profile_7468899508961767.png)
![Mentee - no-availability state, textarea and submit disabled](https://raw.githubusercontent.com/Xchange-Taiwan/X-Talent-Frontend/8dfffda13e90047a8daa281c606cdd2ef49f7d72/fix-712-followup-simplify-booking-panel/20260911T222938Z/0-mentee-desktop-profile_7468899508961767.png)

## Test plan
- `pnpm type-check`, `pnpm lint`, `pnpm test` (2095 tests) all pass
- Cherry-picked cleanly from the same commit that was reviewed and CI-green on #1161's branch before that PR merged
- Note: the AI Review bot on this PR reports `high` risk because it checks against the *original* ticket wording (which asked for a "browse other mentors" CTA and a dedicated sign-in screen). Both were deliberately removed per direct product feedback - see the discussion linked in the Claude Code session below.

Ref: https://github.com/Xchange-Taiwan/X-Talent-Tracker/issues/712

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01Kh2FAycarrJkJpsry6J2J7

