# Populate once-off invoice items during quote acceptance

### Motivation
- Ensure that when a quote is accepted and the atomic workflow creates an invoice, matching invoice line items are created from the quote's once-off items so the invoice is complete and auditable.

### Description
- Update `acceptQuote` in `lib/actions.ts` to reuse a single Supabase client, capture the returned `invoice_id`, load the quote's `once_off_total_cents` and `quote_items`, and insert corresponding `invoice_items` rows linked to the created invoice.
- Add `buildOnceOffInvoiceItemsFromQuoteItems` to `lib/business-rules.ts` which maps quote item `description`, `quantity`, and `once_off_cents` into invoice item rows, skips monthly-only items, assigns `unit_amount_cents`, and validates the summed total against `quote.once_off_total_cents`.
- Import the helper into `lib/actions.ts` and only insert invoice items when an `invoice_id` was returned by the atomic acceptance procedure.
- Add tests in `tests/business-rules.test.ts` for successful invoice item building, skipping monthly-only rows, and the total-mismatch error path.

### Testing
- Ran `npm test` (Vitest) and all tests passed: the updated `tests/business-rules.test.ts` file ran and the test suite succeeded.
- Ran `npm run typecheck` (TypeScript `tsc --noEmit`) and it completed without errors.
- Ran `npm run lint` (ESLint) and no new lint errors were reported.
- Note: an earlier attempt to run `npm test -- --runInBand` failed because Vitest does not support the `--runInBand` option, but the plain `npm test` run succeeded.

------
[Codex Task](https://chatgpt.com/codex/cloud/tasks/task_e_6a3422a70a988332a32b9bad08ec443b)
