# 🐛 fix(desktop): preserve workspace scope in tab navigation

#### 💻 Change Type

- [ ] ✨ feat
- [x] 🐛 fix
- [ ] ♻️ refactor
- [ ] 💄 style
- [ ] 👷 build
- [ ] ⚡️ perf
- [ ] ✅ test
- [ ] 📝 docs
- [ ] 🔨 chore

#### 🔗 Related Issue

None found.

#### 🔀 Description of Change

- Preserve literal desktop tab, recently viewed, and navigation-history URLs when switching entries so workspace-prefixed paths are not re-prefixed by the current workspace.
- Pass route search parameters into dynamic route metadata and resolve workspace scope from route params.
- Filter agent, group, page, document, and task metadata by the route workspace before displaying desktop tab titles.
- Store workspace-aware URLs when opening chat topics, group topics, pages, and fleet agents in new desktop tabs.
- Add regression coverage for workspace tab URL parsing, route metadata workspace matching, and desktop-only recently viewed separation.

#### 🧪 How to Test

- [x] Tested locally
- [x] Added/updated tests
- [ ] No tests needed

```bash
bunx vitest run --silent='passed-only' src/store/electron/actions/__tests__/recentPages.test.ts src/features/Electron/titlebar/TabBar/url.test.ts src/features/RouteMeta/workspaceScope.test.tsx
```

Result: 3 files, 24 tests passed.

`bun run type-check` was also attempted, but this checkout cannot currently resolve `react-router-dom` from root `node_modules` and also reports stale `.next` generated type paths.

#### 📸 Screenshots / Videos

Not applicable. This changes desktop navigation and metadata data selection logic.

#### 📝 Additional Information

The local `canary` branch was 80 commits behind `origin/canary` when this branch was created; the PR targets `canary` for normal merge validation.

