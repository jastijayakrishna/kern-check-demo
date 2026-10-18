# feat(release): generate AI-assisted release notes

## What this PR does

This PR adds AI-assisted release notes for stable releases. GitHub-generated notes remain the authoritative pull request set; the generator enriches those pull requests with their descriptions, labels, changed paths, and diff statistics, then produces concise user-facing summaries and up to six highlights.

The model cannot add, remove, or renumber pull requests. The generator validates the complete pull request set, output length, and plain-text formatting. An invalid summary falls back independently to its original pull request title, while a generator-level failure leaves the release workflow on GitHub's existing `--generate-notes` path. Nightly and preview releases are unchanged.

Generated notes carry a versioned marker so the changelog generator can reuse the same content with adjusted heading levels instead of producing a second, divergent summary.

## Why it's needed

Current release notes and the aggregated changelog are primarily built from commit or pull request titles. They are complete and auditable, but larger releases are difficult to scan because they do not explain user impact or identify the most important changes.

This keeps the full linked pull request list while adding a non-blocking editorial layer. AI does not participate in version calculation, pull request inclusion, or release publication decisions.

## Reviewer Test Plan

### How to verify

1. Configure `OPENAI_API_KEY`, `OPENAI_BASE_URL`, and `OPENAI_MODEL`, run the generator, and confirm the result contains Highlights, Breaking Changes, and a Complete Change List.
2. Confirm every pull request from GitHub-generated notes appears exactly once in the Complete Change List and retains its pull request link, author attribution, and New Contributors credit.
3. Remove the model configuration or return an invalid model response and confirm affected summaries safely fall back to the original pull request titles.
4. Simulate an unsupported GitHub-generated-notes entry format and confirm generation fails, allowing the release workflow to retain its `--generate-notes` fallback.
5. Confirm marked release notes are reused in `CHANGELOG.md` with headings demoted below the release version heading.
6. Confirm nightly and preview releases continue to use the existing GitHub-generated-notes path.

Local verification:

- `npm run lint`
- `npm run typecheck`
- `npx vitest run scripts/tests/generate-release-notes.test.js scripts/tests/generate-changelog.test.js scripts/tests/ai-release-notes-workflow.test.js` — 53/53 passed
- `actionlint -ignore SC2129 .github/workflows/release.yml`
- `npm run build`
- Real `v0.19.8...v0.19.9` smoke test with `qwen3-coder-flash`: 87/87 pull requests retained in the Complete Change List and six highlights generated

### Evidence (Before & After)

N/A — this changes release automation and generated Markdown, not runtime UI.

### Tested on

|     OS     | Status |
| :--------: | :----: |
|  🍏 macOS  | ✅ tested |
| 🪟 Windows | ⚠️ not tested |
|  🐧 Linux  | ⚠️ not tested |

### Environment (optional)

Node.js 22, GitHub API, and an OpenAI-compatible `qwen3-coder-flash` provider.

## Risk & Scope

- Main risk or tradeoff: Summary and highlight quality depends on the configured model. Classification remains deterministic from pull request labels and Conventional Commit prefixes, so maintainers should still scan the generated highlights before publication.
- Not validated / out of scope: This does not rewrite historical releases, let AI decide inclusion or classification, or send full diffs to the model. The AI path requires three repository secrets; without them, generation safely falls back.
- Breaking changes / migration notes: None. Nightly releases, preview releases, and version calculation are unchanged.

## Linked Issues

N/A

<details>
<summary>中文说明</summary>

## What this PR does

这个 PR 为稳定版本增加 AI 辅助的 Release Notes 生成流程。GitHub generated notes 仍然是完整 PR 集合的权威来源；生成器读取 PR 描述、labels、变更路径和 diff 统计，为每个 PR 生成简短的用户视角摘要，并从
