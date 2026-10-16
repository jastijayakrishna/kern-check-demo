# Add LinkedIn logo in footers and a short follow line

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## What does this PR do?

People coming from ads can find Clarvia on LinkedIn without the follow ask competing with the question form.

- Every site footer, including `/ask`, now has the LinkedIn logo only. It opens https://www.linkedin.com/company/clarvia-org in a new tab.
- The “We’re on it” confirmation (`/ask/sent` and `/{lang}/ask/sent`) adds a short line under the Lex email note: “Follow us on LinkedIn.” The word LinkedIn is the link. The footer on that page is still just the logo.
- Lex’s email footer has the same short line in all 14 language packs, with LinkedIn linked. The page is English-only, so anyone who cannot read that short line is outside the audience.

## What to check

- Open `/en` and `/ask`. The footer shows the LinkedIn mark and no follow sentence. The Ask form is unchanged.
- Open `/ask/sent?lang=en` and `/fr/ask/sent`. Under the confirmation text, the follow line is in that language. The footer logo is still there.
- Switch `/ask/sent?lang=` across a few packs (for example `de`, `ar`). The sentence stays short and still contains “LinkedIn”.

## Checklist

- [ ] CI passes (`pnpm validate`, `pnpm test`, `pnpm typecheck`)
- [x] New graph records start as `draft` / `restricted_source` — not applicable
- [x] Source assertions include `text_quote` anchors — not applicable
- [x] Scenario tests cover new consequences — not applicable
- [x] Documentation updated (if applicable) — not applicable

Checked locally: Ask copy tests, and the email footer includes the company URL in all 14 locales.

## Related issues

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-80e1555f-7720-4177-9233-e23db6db441d?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-80e1555f-7720-4177-9233-e23db6db441d&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>
