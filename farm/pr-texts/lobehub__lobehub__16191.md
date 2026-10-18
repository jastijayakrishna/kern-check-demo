# ✨ feat(device): improve device connection management

#### 💻 Change Type

- [x] ✨ feat
- [ ] 🐛 fix
- [ ] ♻️ refactor
- [ ] 💄 style
- [ ] 👷 build
- [ ] ⚡️ perf
- [x] ✅ test
- [ ] 📝 docs
- [ ] 🔨 chore

#### 🔗 Related Issue

No matching issue found.

#### 🔀 Description of Change

- Redesign device settings around an overview, device list, detail panel, and empty detail placeholder.
- Add a scoped “Connect another device” action and move Devices under Agent settings.
- Clarify Device Connection, execution environment, security, and access copy across default, en-US, and zh-CN locales.
- Simplify the chat execution target switcher by removing the web download CTA and improving no-device / auto-target states.

#### 🧪 How to Test

- [x] Tested locally
- [x] Added/updated tests
- [ ] No tests needed

Commands run:

```bash
git diff --check
node -e "for (const f of ['locales/en-US/chat.json','locales/en-US/electron.json','locales/en-US/setting.json','locales/zh-CN/chat.json','locales/zh-CN/electron.json','locales/zh-CN/setting.json']) JSON.parse(require('fs').readFileSync(f,'utf8')); console.log('locale json ok')"
bunx vitest run --silent='passed-only' 'src/routes/(main)/settings/hooks/useCategory.test.tsx'
```

Pre-commit also ran prettier, stylelint, and eslint fixes for staged files.

#### 📸 Screenshots / Videos

| Before | After |
| ------ | ----- |
| Not captured | Not captured |

#### 📝 Additional Information

No breaking changes.

