# fix: stop ConnectWise time entries and notes from emailing by default

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

WYREAI-495. Time entries could email a customer's client when nobody asked, and `cw_add_ticket_note` with `emailContactFlag=true` (or `emailCcFlag=true` plus `emailCc`) returned ConnectWise 400.

- `cw_create_time_entry` now sends `emailContactFlag`, `emailResourceFlag`, and `emailCcFlag` as **false** unless the caller sets them. `emailCc` is sent only when the caller provides it.
- `cw_add_ticket_note` no longer posts those four names. A flag set to true only turns on ServiceNote `processNotifications` (an explicit `processNotifications: false` still wins). When that is true and the caller did not set a note-type flag, the body sets `detailDescriptionFlag` so Manage has a place to display the note.
- A Manage error, including the 400 response body, is returned on the tool result (`isError`) instead of being dropped. `cw_add_project_ticket_note` does the same, so a failure from `/project/tickets/{id}/notes` includes the vendor status and body.
- Optional `memberId` on service and project ticket notes is sent as `member: { id }` only when the caller sets it.

## What caused the 400

`POST /service/tickets/{id}/notes` takes a **ServiceNote**. In the ConnectWise Manage Public Endpoints OpenAPI (2025.8, the published contract under that name; this repo's 2025.16 notes were checked against the same document family), ServiceNote properties are:

`id`, `ticketId`, `text`, `detailDescriptionFlag`, `internalAnalysisFlag`, `resolutionFlag`, `issueFlag`, `member`, `contact`, `customerUpdatedFlag`, `processNotifications`, `dateCreated`, `createdBy`, `internalFlag`, `externalFlag`, `sentimentScore`, `_info`.

There is no `emailContactFlag`, `emailResourceFlag`, `emailCcFlag`, or `emailCc`. Those four are **TimeEntry** fields (`emailCc` is a string; the flags are nullable booleans). The OpenAPI text calls each flag an action flag and points updates at the ticket: `automaticEmailContactFlag`, `automaticEmailResourceFlag`, `automaticEmailCcFlag`, and `automaticEmailCc`.

`buildTicketNoteBody` was copying those names onto the note whenever the caller set them, and it also set `processNotifications: true` when a flag was true, without a display flag. Manage rejects the unknown properties with 400. That matches the report: no flags posts the note and sends no mail; `emailContactFlag=true` or `emailCcFlag=true` plus `emailCc` returns 400.

The working workaround follows the contract: turn on the ticket `automaticEmail*Flag`, post the note with `processNotifications: true`, then turn the flag off. `processNotifications` is the only ServiceNote switch that sends mail, and the ticket fields choose the recipients. A separate, older Manage validation ("Please choose where to display the notes", fields `detailDescriptionFlag, internalAnalysisFlag, resolutionFlag`) applies when a note is saved for notification with no type flag. Text-only notes already succeed in the reported tenant, so a missing display flag is not what 400s a flag-less note. This change still sets `detailDescriptionFlag` when `processNotifications` is true and the caller set no type flag, so that validation is not the next 400. It does not override an explicit type flag, and it does not toggle ticket `automaticEmail*` settings.

`emailCc` cannot be given a supported shape on this endpoint. It is not an array or a contact reference on ServiceNote; the string lives on the ticket as `automaticEmailCc` (and on TimeEntry as `emailCc`). The tool accepts the argument and does not send it.

## Time-entry default: the commit

No commit in this repository sets `emailContactFlag: true` on `cw_create_time_entry`.

- The tool was added in `b2ed6da` (2026-03-23, "feat: implement ConnectWise Manage MCP server with full API coverage") and the create body has omitted the flag ever since.
- `03433c5` (2026-09-22, WYREAI-400, #84) added time-entry update/delete and the note email arguments. It did not change the time-entry create body.
- The 2026-10-09 commits on `main` (`061cc50`, invoice update, #100) and `f1454da` (gateway URL check, not on `main`) do not touch time entries.

The OpenAPI spec does not declare a default of true. It describes `emailContactFlag` as an action flag whose stored value is the ticket `automaticEmailContactFlag`. Omitting it lets Manage apply that ticket flag, which is often true, so the entry emails the contact. That is the behavior reported since about Oct 9. The fix sends `false` unless the caller sets the flag. True is sent only then.

## Note author (member 176)

`POST /service/tickets/{id}/notes` accepts `member` as a MemberReference (`id`, `identifier`, `name`). Project ticket notes (`POST /project/tickets/{id}/notes`, schema TicketNote) accept the same `member` reference. There is no separate author-id field.

When `member` is omitted, Manage attributes the note to the API member that authenticated the request. In this report that member is **176, "Hermes - WMTS"**. That is the integration identity, not a field we were hard-coding. `createdBy` on the ServiceNote response is that member's identifier string; it is not how you choose the author on create.

`memberId` is optional. It is sent as `{ "member": { "id": <memberId> } }` only when the caller sets it. Omitting it leaves the author as the API member.

## Tests

`src/__tests__/wyreai-495.test.ts` covers time-entry false defaults, note bodies that omit the rejected email names, `member` only when set, and a Manage 400 body returned on the tool error for both service notes and project notes.

## Review

CodeRabbit's only unresolved thread on `72f6e8fd` asked `cw_add_project_ticket_note` to return Manage failures as tool errors. That is fixed in `4aa628d`.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-2a6cc4ce-827d-5c7b-8d5a-489e541c15a1?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-2a6cc4ce-827d-5c7b-8d5a-489e541c15a1&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>

<!-- codesmith:footer -->
---
<a href="https://app.blacksmith.sh/WYRE-AI/codesmith/connectwise-manage-mcp/pr/114?autoLogin=true&ref=codesmith_pr_footer"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v3.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-light-v3.svg"><img alt="View with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/view-with-codesmith-dark-v3.svg"></picture></a> <a href="https://backend.blacksmith.sh/track/enable-autofix?expires=1794522575&installation_model_id=431408&pr_number=114&ref=codesmith_pr_footer&repository=WYRE-AI%2Fconnectwise-manage-mcp&return_to=https%3A%2F%2Fgithub.com%2FWYRE-AI%2Fconnectwise-manage-mcp%2Fpull%2F114&signature=a2dd3bbac51030b92804176f48f970e83b4a524a6a725ab0f79f17491ea4afcc"><picture><source media="(prefers-color-scheme: dark)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"><source media="(prefers-color-scheme: light)" srcset="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-light.svg"><img alt="Autofix with [code]smith" src="https://pr-comments-assets.blacksmith.sh/codesmith/autofix-with-codesmith-dark.svg"></picture></a>
<sup>Need help on this PR? Tag <code>@codesmith-bot</code> with what you need.</sup>

<!-- codesmith:autofix:disabled -->
<!-- /codesmith:footer -->

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

* **New Features**
  * Ticket and project-ticket notes can specify an optional member as the author. Ticket-note notifications follow `processNotifications` and the ticket’s email settings.
  * Time-entry email action flags default to off when omitted, and optional email settings are supported.
* **Bug Fixes**
  * Unsupported email recipient fields are no longer sent with ticket-note requests. API error details are surfaced in tool errors.
* **Documentation**
  * Updated guidance explains notification behavior, note authorship, and time-entry email defaults.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->
