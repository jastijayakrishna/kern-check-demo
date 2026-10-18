# Evaluate: landing page, create-suite page, suite overview

Evaluate gets a real landing page, creating a suite becomes a page instead of a modal, and a suite gets an overview. Design work by @marcelo; the last two commits are an engineering pass over it.

## What the design changes

- **`/evals` has a list again.** Landing there used to run an effect that picked the most recently *run* suite and `replace`d the URL with its dashboard, so the only way to see what suites existed — or to reach one that had never run — was the breadcrumb's suite dropdown. The redirect is gone; the landing renders `SuitesOverview` behind a **Suites | Runs** switcher.
- **`CreateSuiteDialog` → `CreateSuitePage`** at the `/evals/create` route the dialog was already opening. Mutation, payload shape and post-create navigation are unchanged and still owned by `EvalsTab`.
- **`SuiteDetailOverview`** — run-history table plus case list, with its arithmetic extracted into `suite-detail-model.ts` as pure functions with their own tests.
- **One header across both eval surfaces.** `EvalsHeader` owns the title, description, Create suite and the landing tabs; CI Evals' hand-rolled breadcrumb and `evals-mode-nav.tsx` are deleted.

## What the engineering pass changes

### It did not compile

Five type errors, all in `create-suite-page.tsx`, all from the page being written against a composer API that never landed — `EnvironmentStack.modelId: string | null`, where main shipped `modelSelection` (`includeClientDefaults` plus explicit ids) in #4256.

Two are renames. The third is a deletion and it is the one worth reading: the page seeded the previewed host's own `modelId` into the stack as an **explicit** pick. That looks identical on screen to the default and resolves differently — `environment-stack.ts` says so directly, the fingerprint treats explicit-equals-default as its own row — so every suite born on this page would have minted a duplicate ad-hoc environment. The default selection already means "run the client's model."

### `slots` was only half-implemented

Only the models pill consulted it. Environments, clients, servers, skills and sandbox ignored it, so a caller that passed `slots` still got the whole strip — the create page's two sections, **Servers** and **Where it runs**, were rendering two identical full strips rather than the split they are named for.

Every pill now checks the list, still AND-ed with its own flag so `slots` narrows and never widens. Omitting it keeps `DEFAULT_COMPOSER_SLOTS`, so swarm and User Testing render exactly what they rendered before (46 files / 449 tests green).

`emptyServerLabel` / `serverInfoText` land as real props rather than arguments the page was already passing to a component that did not take them. `ServerGroupPicker`'s `triggerTestId` is wired through instead of dead.

### Three affordances came back

None of them had moved somewhere else. Each was gated behind a condition that stopped holding as soon as the user made any progress.

- **The sample suite.** The empty hero showed its CTAs only when the project had *zero* connected servers, so connecting a server removed "Try sample suite" — and the Excalidraw quickstart has no other entry point in the product. "Has servers, has no suites" is the exact state it exists for. Cards and CTAs now both render, CTAs demoted to ghost buttons so there is still one obvious primary action.
- **Generate.** It lived only in the zero-case hero, so a suite lost it the moment it had its first case — which is when "generate more from live discovery" is most useful. Now also on the Test Cases card, same capability gate and disabled-reason tooltip. That card's other button said "Edit" while calling `onCreateTestCase`; it says **Add case**.
- **Delete.** `SuitesOverview` lost its `onDelete`, and the breadcrumb `SuiteSwitcher` that carried the other quick delete is no longer rendered anywhere. Suite settings still has one, but that path needs the suite opened first — wrong shape for a suite you want gone, and for a suite that has never run the l
