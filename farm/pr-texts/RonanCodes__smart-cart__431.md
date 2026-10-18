# 🐛 fix: porkless + disliked cuisine hard filters, drop mis-tagged non-dinners (#422 #423 #424)

Three meal-planner bugs reported by Renée (paying SlimMandje tester), all rooted in the planner's `hardFilter`: genuinely-blocking preferences were leaking through as soft signals, and the pork-exclusion list missed common forms.

## What changed

**#422 — porkless ignored (bacon in first dish).** An excluded ingredient/protein is now a HARD filter in `hardFilter` (`src/lib/planner/planner.ts`), fed by BOTH the derived `allergies` list and the raw `dislikes` words on the profile. Any pork trigger (`pork` / `porkless` / a single pork form) expands to every form: bacon, ham, gammon, chorizo, lardons, pancetta, prosciutto, and the Dutch `spek`. So "Cauliflower risotto with smoked bacon" and "gerookt spek" dishes are never candidates. The onboarding + profile-edit `porkless` exclusion lists are widened to match (`onboarding-mapping.ts`, `profile-edit-server.ts`).

**#423 — disliked cuisine still appears.** The disliked-cuisine hard filter was already present on `main` (the #374 work); the issue's "still soft" description was stale. Added the build + regenerate regression tests the issue asked for so it stays locked. Liked-cuisine boost + neutral diversity unchanged.

**#424 — snacks/sauces as dinners.** Added a defensive non-dinner TITLE heuristic on top of the existing category gate (#375): a title containing `sauce`/`saus`, `crackers`/`cracker`, `bar`/`reep`, `crumble`, `dip`, `snack`, `dessert`, `toetje` keeps the recipe off the dinner plan even when a single mis-tag says `mealType: 'dinner'` with a null/generic category. Word-boundary matched (EN + NL) so legitimate dinners survive ("barbecue" keeps "bar", "scrambled" keeps "ramble", "snackbar fries" stays). The offending items (gado-gado sauce, low-carb crackers/coconut bars, apple & pear crumble) live in imported D1 recipe data, not committed seed data, so the heuristic is the durable fix rather than a one-off reclassify.

## Regenerate path

Verified `generatePlanForHousehold` (`planner-core.ts`) and `WeekSession` (`week-session.ts` via `replan-context-server.ts`) both pass the full stored `household.profile` (dislikes + disliked cuisines + allergies) into `generateWeek` / `rankRecipes`. No incomplete-profile bug: build and regenerate filter identically. #422's "drops out on a new week" symptom was the pork-form coverage gap, now fixed for both paths. Added `WeekSession` tests asserting regenerate / swap / add never produce a banned dish.

## Tests (TDD, written failing first)

- Porkless household gets ZERO pork/bacon/spek on build AND regenerate; reads `dislikes` directly; doesn't over-exclude non-pork dislikes.
- Household disliking Indian gets ZERO Indian on build AND regenerate.
- A gado-gado sauce / low-carb crackers / coconut bar recipe never lands as a planned dinner; legitimate dinners with substring overlap survive.
- `WeekSession` regenerate/swap/add honour the hard prefs.

Full local gate green via pre-push: format + lint + typecheck + build + 1362 tests. Recsys benchmark unaffected (hard filters don't touch ranking).

Closes #422
Closes #423
Closes #424

🤖 Generated with [Claude Code](https://claude.com/claude-code)
