# fix(billing): never mint milestone invoices over an estimate that was already invoiced (#1203)

Refs #1203.

## Defect

`milestoneEstimateLink` (`packages/api/src/invoices/invoice-schedule.ts`) treated **any** invoice on the job that carries the estimate id as "the first milestone already holds the link". That includes the plain invoice written by `POST /estimates/:id/convert-to-invoice`. It returned `undefined`, and both mint paths (`CreateInvoiceScheduleExecutionHandler` in `proposals/execution/invoice-schedule-handler.ts`, and `mintCompletionMilestones` in `invoices/schedule-completion.ts`) then drafted every milestone with no link. Estimate E ($1,000) converted to INV-0001, followed by an approved 50/50 schedule for E, produced a $500 deposit and a $500 balance on top of INV-0001: **$2,000 of drafts for a $1,000 estimate**. Before #975 the `uq_invoices_estimate` collision blocked this by accident. The RED run below shows it at real Postgres.

## ASSUMPTIONS (for Josh)

1. **Refuse, don't link.** If an estimate already has an invoice outside the schedule, schedule creation and milestone minting are refused (fail closed, nothing written). The alternative, adopting the existing invoice as a milestone of the schedule, is a product decision and is not implemented.
2. **Every invoice status counts, including `void`.** A voided converted invoice still refuses a schedule for that estimate. This matches `convertEstimateToInvoice`, whose idempotency check also ignores status. Letting a voided conversion be replaced by a schedule is a product decision. The change would be one predicate in `invoiceOutsideSchedule`.
3. **The completion path throws, it does not skip.** `mintCompletionMilestones` throws a `ConflictError` with the reason before its first insert. Its only caller, `runJobCompletionEffects`, already catches and `logger.error`s it ("schedule completion milestone minting failed"), so the job completion itself still succeeds.

## What changed (no money math)

- `invoice-schedule.ts`: new pure `invoiceOutsideSchedule(schedule, jobInvoices)`. It returns an invoice whose `estimateId === schedule.estimateId` **and** whose `scheduleId !== schedule.id`. Membership is decided by the schedule linkage (`invoices.schedule_id`, the column behind `uniq_invoices_schedule_milestone`), never by `estimate_id` alone. The schedule's own deposit carries the estimate id and still bills its balance. Also new: `estimateAlreadyInvoicedReason(invoiceNumber)`, the owner-facing message: *"This estimate was already invoiced as INV-0001. No milestone invoices were created for it, because they would bill the same estimate a second time."*
- `invoice-schedule-handler.ts`: the guard runs after the existing-schedule retry/mismatch check and **before** `scheduleRepo.create`. A refusal returns `{ success: false, error: <reason> }`, so no schedule row and no invoice row are written. A retry of the same schedule is still recognised through `schedule_id`. The job-invoice read that the on_accept block already did is now done once, just before the guard, and reused.
- `schedule-completion.ts`: before any insert, every schedule on the job is checked (defence in depth). A schedule approved **before** the estimate was converted, or written before this guard existed, cannot mint over the converted invoice.
- Unchanged: `splitMilestones`, `applyBps`, totals, tax, discount, rounding, `milestoneEstimateLink`'s behaviour, and the supervisor/approval gate.

## Tests: what each proves

`packages/api/test/integration/milestone-billing-estimate-link.test.ts`, new describe `#1203` at real Postgres, driving the real `convertEstimateToInvoice`, the real `CreateInvoiceScheduleExecutionHandler` (total derived from the estimate via `PgEstimateRepository`) and the real `mintCompletionMilestones`:

| test | proves |
|---|---|
| refuses to create a schedule for a converted estimate | convert E → approve a 50/50 schedule → complete: only INV-0001 ($1,000) exists. The execution fails with the reason naming INV-0001, and **no** `invoice_schedules` row is written. |
| a schedule appro
