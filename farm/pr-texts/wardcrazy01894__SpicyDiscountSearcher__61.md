# Badge each row with the evidence behind it, and stop counting

A car race now mixes all three confidences in one list — Avis and Hertz `verified`, National `driven`, the hotel builders `best-effort` — and the single line under the list could not say which row was which.

CLAUDE.md has recorded badging per row as the better fix since that line was written. This is it.

## The problem with counting

The old line was one of five fixed alternatives, the useful one being:

> 2 of these search links are unverified — a result that looks wrong probably is. The rest are checked against the live site…

It never said **which** two, and there was nothing on screen to work it out from. Worse, being a fixed set of alternatives, it described states the list was not in — a run of only verified links still had a branch that spoke about the unverified.

## What each row says now

`confidenceBadge` prints one of three beside the code, each carrying the real caveat in its tooltip:

| confidence | badge | what it claims |
|---|---|---|
| `verified` | `checked link` | the URL was replayed against the live site, for a US airport round trip, driver 25+ |
| `driven` | `form filled` | the URL carries no search; the trip and code were typed into the vendor's own form and checked against what it rendered back |
| `best-effort` | `unverified link` | reverse-engineered, never checked |

The words are deliberately **not** a grade out of three. `driven` is not "better than best-effort, worse than verified" — it is a different kind of claim, and at National a stronger one than any deep link makes.

The line beneath now explains only the kinds actually present, one clause per kind, so it cannot describe a state the list is not in.

## Two exclusions carried over, because both were bugs

- **`link-build` gets no badge at all.** The worker stamps those `best-effort` on its catch path, so badging on `confidence` alone would print "unverified link" against a link that was never built — the exact mistake the summary line had already been taught to avoid, arriving one row further down.
- **`driven` is never folded in with the links**, since it has no link to grade.

## Colour

Only `unverified` takes one, and it is the warning colour rather than the error one — the link may well be fine, and nothing about the row has failed. The other two stay grey on purpose: a green "checked" would promise the price is right when the claim is only about the URL. Outlined rather than filled, so a badge does not read as a status.

## Tests

Driven through a real `RUN_STATE` broadcast rather than by calling the renderer. Mutation-checked:

- `confidenceBadge` stubbed to return null → the badge test fails
- the `link-build` guard removed → "badges no link at all when no link was built" fails
- the `unverified` clause un-gated → "explains each badge it actually showed, and nothing it did not" fails

Suite (520), typecheck, eslint, prettier and `npm run build` are green.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

