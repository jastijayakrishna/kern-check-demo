# SIG-89: render timestamps in the viewer's local timezone, not hardcoded ET

## Why
Every displayed time (price "as of", projection computed/cutoff, observed, kickoff, decision/settlement/correction) was formatted in a hardcoded `America/New_York` zone, so a Central-time viewer saw everything an hour off and labelled "ET".

## What changed
- `formatEt` / `formatEtDate` / `formatEtTime` (`values.tsx`) no longer pin `timeZone` — `Intl` defaults to the runtime zone, i.e. the **browser's local zone** in these client components. Added `localZone()` for an optional short zone label.
- Removed the now-incorrect `" ET"` label suffixes (13 sites across `ContractDetail`, `Accuracy`, `Slate`).
- `Slate.tsx` marked `"use client"` (it's purely presentational, props-in/JSX-out) so its header times render in the viewer's zone rather than the server's UTC.
- `suppressHydrationWarning` on the slate's time elements (server SSRs UTC; client re-renders in the local zone, which is the correct value).

## Verification
tsc, eslint, prettier clean; slate + screens Jest suites (**133 passing**; one assertion that pinned `/corrected .* ET/` updated).

## Note
Uses each viewer's browser zone (true "adjust to location"). If you'd rather pin one fixed display zone for everyone, that's a smaller, hydration-trivial change — say the word.

Closes SIG-89.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
