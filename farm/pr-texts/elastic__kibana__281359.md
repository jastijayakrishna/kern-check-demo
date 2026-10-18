# [SLO] Fix welcome page displayed for remote-only spaces

## Summary

resolves https://github.com/elastic/kibana/issues/281361

- The SLO welcome (empty-state) page was incorrectly shown to users whose space had SLOs on remote clusters only. The presence check used `useFetchSloDefinitions` which queries local saved objects only and has no visibility into cross-cluster summary indices.
- Both the list page (`slos.tsx`) and the welcome page (`slos_welcome.tsx`) form a mutual redirect pair — both needed fixing simultaneously to avoid an infinite redirect loop for remote-only users.
- Introduces a shared `useHasSlos` hook that wraps the existing remote-aware `useFetchSloDefinitionsWithRemote` hook (CCS over summary indices, local + remote), using `size: 1` for a presence-only check.

## Test plan

- [ ] Unit tests: `node scripts/jest x-pack/solutions/observability/plugins/slo/public/hooks/use_has_slos.test.ts`
- [ ] Unit tests: `node scripts/jest x-pack/solutions/observability/plugins/slo/public/pages/slos_welcome/slos_welcome.test.tsx`
- [ ] Unit tests: `node scripts/jest x-pack/solutions/observability/plugins/slo/public/pages/slos/slos.test.tsx`
- [ ] Manual (with a remote cluster configured): space with zero local SLOs but ≥1 remote SLO → SLO list renders, no redirect to `/welcome`, no redirect flicker/loop
- [ ] Regression: local-only space with SLOs → still shows the list
- [ ] Regression: truly empty space (no local, no remote SLOs) → still shows the welcome page

🤖 Generated with [Claude Code](https://claude.com/claude-code)
