# fix(evidence): editing a row from the list no longer deletes its tags

## The bug

Open **Edit** from an evidence list row. Change nothing. Save. **Every tag on that row is gone.**

Three things line up to make it silent:

1. `EvidenceClient.tsx` seeded `EditEvidenceModal` **without** `tags`. That field is optional on `EditEvidenceInitial`, so the omission type-checked.
2. The modal rendered the tags field **empty** — indistinguishable from "this evidence has no tags".
3. Submit sent `tags: []` **unconditionally**, and `updateEvidence` reconciles that as remove-them-all (`if (data.tags !== undefined) setTags(...)`).

The detail sheet's edit button *always* passed tags, so the same modal behaved correctly from there. That asymmetry is why this survived in an otherwise carefully built surface — and why "the modal is fine" was true and misleading at the same time.

## Two fixes, because either alone leaves a hole

**The modal tracks whether it was seeded**, and omits the `tags` key entirely when it wasn't. A modal never told the current set has no business reconciling it, and omitting the key is already what the usecase reads as "leave them alone". *This closes the class* — a future seed site that forgets tags can no longer destroy them.

**The list row now seeds them**, matching the detail sheet. The data was already on the wire: `evidenceListSelect` has always selected tags, but `EvidenceRow` never declared the field, so nothing client-side could see it.

## An incidental finding

The select's comment claims tags power *"tag chips on the list row + the tag filter's client-side match"*. Neither exists — `grep tags EvidenceClient.tsx` returned **0** before this change. The comment is stale; I've left the behaviour alone and only noted it, since adding chips is a feature decision, not a bug fix.

## The test, and why it's shaped this way

`tests/rendered/evidence-edit-tags-preserved.test.tsx` drives the real modal and asserts on the **PUT body**, because that is where the defect lived. A source scan for `tags:` would have passed against the broken code.

**Mutation-verified**: restoring the unconditional `tags: []` fails the unseeded case while the two seeded cases stay green.

That direction is the point. A test that only proved "the original bug is gone" would validate the *diagnosis*; this one fails if the *remedy* is wrong. Three cases:

| Case | Expected |
|---|---|
| unseeded modal | no `tags` key in the payload |
| seeded, untouched | round-trips `['soc2','q1']` |
| seeded, cleared by user | sends `[]` — the deliberate-clear path still works |

That third case matters: the fix must not swallow a real instruction to remove tags.

## Note on CI

The E2E job is currently OOM-killing runners stochastically, on any commit — unrelated to this change, and being fixed separately. If E2E goes red here, check the signature (`Creating an optimized production build ...` → cancelled, `Generating static pages` never reached) before reading it as a defect in this diff.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
