# feat(attributes): Add `langchain.chain.name` (deprecated) in favor of `gen_ai.pipeline.name`

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
The JavaScript SDK ships `langchain.chain.name` on LangChain chain spans, but it has no conventions registry entry. That value is the name of the AI pipeline/chain being executed, which is already covered by `gen_ai.pipeline.name` (and LangGraph already sets that attribute).

This registers `langchain.chain.name` as deprecated with `gen_ai.pipeline.name` as its replacement, `_status: backfill`, and adds it to the existing `gen_ai.pipeline.name` / `ai.pipeline.name` alias group so ingest can copy historical values onto the canonical name.

The agent span name template `{{gen_ai.operation.name}} {{gen_ai.pipeline.name}}` is already in place from #593.

Conventions work for [JS-3452](https://linear.app/getsentry/issue/JS-3452/move-langchainchainname-to-gen-aipipelinename) / [getsentry/sentry-javascript#23683](https://github.com/getsentry/sentry-javascript/issues/23683). SDK emission of `gen_ai.pipeline.name` instead of `langchain.chain.name` is a follow-up in sentry-javascript.

## PR Checklist

- [x] I have run `yarn test` and verified that the tests pass.
- [x] I have run `yarn generate` to generate and format code and docs.

If an attribute was added:

- [x] The attribute is in a namespace (e.g. `nextjs.function_id`, not `function_id`)
- [x] I have used the correct value for `apply_scrubbing` (i.e. `manual` or `auto`. Use `never` only for values that should never be scrubbed such as IDs)

If an attribute was deprecated:

- [x] I've followed the policies described in [CONTRIBUTING.md](https://github.com/getsentry/sentry-conventions/blob/main/CONTRIBUTING.md)

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-5f444f4a-1e6d-49bb-b7c9-d981b96ff493?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-5f444f4a-1e6d-49bb-b7c9-d981b96ff493&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
