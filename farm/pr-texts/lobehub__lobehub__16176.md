# 🐛 fix(topic): restore project topic creation from agent subroutes

#### 💻 Change Type

<!-- For change type, change [ ] to [x]. -->

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

N/A

#### 🔀 Description of Change

- Restore the project-folder add-topic action from agent sub-routes such as the assistant profile page by committing the project working directory, clearing the active topic, and navigating back to the agent chat route.
- Add a small shared agent pathname parser for sidebar navigation so prefixed routes such as `/team/agent/:aid/...` and `/_dangerous_local_dev_proxy/agent/:aid/...` are handled by path segments instead of ad-hoc substring checks.
- Preserve detected route prefixes when navigating from agent sub-routes without an active workspace slug.
- Make topic navigation distinguish exact topic routes from topic child routes, so `/agent/:aid/:topicId/page` routes back to the selected topic instead of leaving the URL on the old child page.
- Add regression coverage for project-mode topic creation, prefixed route preservation, and topic route parsing.

#### 🧪 How to Test

- [x] Tested locally
- [x] Added/updated tests
- [ ] No tests needed

```bash
bunx vitest run --silent='passed-only' 'src/routes/(main)/agent/_layout/Sidebar/utils/agentPathname.test.ts' 'src/routes/(main)/agent/_layout/Sidebar/Topic/TopicListContent/ByProjectMode/GroupItem.test.tsx' 'src/routes/(main)/agent/_layout/Sidebar/Topic/hooks/useTopicNavigation.test.tsx'
git diff --check HEAD^..HEAD
```

Local SPA was started and inspected through the debug proxy. The exact project-folder plus button could not be clicked in Browser because the current Web SPA proxy does not render the desktop/bound-device-only project add control.

#### 📸 Screenshots / Videos

N/A

#### 📝 Additional Information

`bun run type-check` is currently blocked by a pre-existing generated `.next/dev/types/validator.ts` reference to the missing `src/app/(backend)/webapi/stt/openai/route.js`, unrelated to this change.

