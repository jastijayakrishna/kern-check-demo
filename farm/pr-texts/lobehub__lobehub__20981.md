# 🐛 fix: open generated files for agent share visitors

### Summary

Contribution source: AI-assisted

On the Agent Share visitor page, clicking a generated file link (`/f/file_xxx`) in a reply opened the right panel with **"File unavailable"**. Clicking the **Edited** card for an HTML file did nothing. The files existed: the preview resolved file metadata through owner-scoped APIs, and visitors do not own the creator's files.

Fixes for the agent-share visitor surface (`context.agentShareId`). The owner path is unchanged:

- **Reply file links** (reported problem): the visitor click previews from the link's own `/f/:id` URL, using `source: { name, url }`. The `/f/:id` proxy is already public by id, so the visitor gets no access it did not already have through the link.
- **File Work cards without a stored URL** (addition): before, the visitor click returned silently. It now falls back to `${appOrigin}/f/<fileId>`, the same public proxy.
- **Edited files card** (addition): the visitor portal only hosts the Artifact and FilePreview views, so the LocalFile view this card pushes never rendered. For visitors the card is now static instead of a dead click. **View changes** still works.
- **Labels without a file extension**, e.g. `[Download the notes](/f/file_x)` (addition, from review): the viewer picks its renderer from the label, so these open the file in a new tab instead of a mismatched viewer.

#### Key Decisions / Non-goals

- Previewing the edited file itself for visitors needs a share-authorized sandbox/filesystem read. That is out of scope; the same file stays reachable through its reply link.
- No share-scoped file metadata endpoint. The public `/f/:id` URL already carries what the viewer needs.
- Topic share pages (`topicShareId`) are not changed.
- Known residual: exported objects are stored as `text/markdown` without a charset. In the new-tab fallback, some browsers may show Chinese text garbled. Making the export write `charset=utf-8` is a possible follow-up.

#### Test

- [x] Tested locally
- [x] Added/updated tests

Regression tests:

- `getFileLinkOpenAction` covers owner, visitor and extensionless-label cases.
- `useVisitorWorkOpen` covers the no-URL fallback.
- The `EditedFilesCard` open action is covered for owner vs visitor.

The 4 regression cases fail with the source reverted. `bun run check` (lint + related tests, 43 passed) and `bun run check --type` are clean.

- Acceptance: https://app.lobehub.com/acceptance/7f6979ef-1da8-410e-a67b-12df73f9fd4f

The acceptance ran on a local runtime seeded from the reported topics. It covers:

- MD/CSV/ICS/HTML/PNG preview and download from reply links;
- file Work cards, with and without a stored URL;
- preview after a refresh;
- the static Edited card;
- the extensionless new-tab fallback;
- another account cannot see the visitor's topic;
- the creator's own preview is unchanged.

#### 🔗 Related Issue

Fixes LOBE-14768

🤖 Generated with [Claude Code](https://claude.com/claude-code)
