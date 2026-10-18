# fix(evals): improve code eval error surfacing and retry behavior

## Summary

- Python code eval errors now read `KeyError: 'text' (line 4)` instead of `'text'` — runners prefix the exception type and add the evaluator line number; Node runner and local dispatcher prefix non-generic error names. Unit + Floci integration tests added.
- Execute preflight failures are framed (`Evaluator failed when tested against sample data: …`) and shown via the standard `trpcErrorToast` instead of an unstyled sonner toast.
- Code eval BullMQ retry backoff bumped 1s → 30s; removed the always-zero `retryBaggage.attempt` span attribute (real counter: `messaging.bullmq.job.attempts`).

## Linear

- `None`

## Major Decisions

- Dropped the inline form error instead of restyling it — the persistent standard toast already shows the same message with more context. `template-form` keeps its inline error (it has no toast).

## Review Focus

- Regression risk from removing the form footer error: mutation failures still toast (verified in-browser); post-success errors (`onFormSuccess`/`router.push`) now only `console.error` instead of rendering inline.
- Rollout: runner changes need a Lambda redeploy; the new backoff only applies to newly enqueued jobs.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

<!-- greptile_comment -->

<details open><summary><h3>Greptile Summary</h3></summary>

This PR improves how code evaluator errors are surfaced: Python now formats exceptions as `KeyError: 'text' (line 4)` (with type name and user-code line number), the Node/local-dispatcher runners prefix non-generic error names, and the preflight check wraps its error in a consistent "Evaluator failed when tested against sample data: …" frame. The UI switches from a duplicate inline-form error + sonner toast to the standard `trpcErrorToast` only, and the BullMQ retry backoff is raised from 1 s to 30 s.

- **Error formatting**: Python `format_error` always prefixes the exception type and appends the innermost `<string>` traceback line; Node runner and local TS dispatcher skip the "Error" prefix (no-signal name) but keep all other error names.
- **UI**: `inner-evaluator-form` drops the `formError` state and inline error paragraph; `template-form` keeps its inline error with updated destructive styling; the `renderFooter` callback signature loses the `formError` parameter.
- **Queue**: BullMQ exponential-backoff seed bumped from 1 000 ms to 30 000 ms (retries ~30 s / ~60 s); always-zero `retryBaggage.attempt` span attribute removed.
</details>

<details><summary><h3>Confidence Score: 4/5</h3></summary>

Safe to merge. The error-formatting improvements are additive and well-tested; the UI change consolidates duplicate error display into a single toast; the backoff increase only affects newly enqueued jobs.

The changes are focused and low-risk. The one observable behaviour change is that mutation failures in inner-evaluator-form now also log to console.error (via the .catch()) in addition to showing the toast — redundant but not harmful. Post-success errors (router.push, onFormSuccess) are silently console-logged instead of shown inline, which the PR description explicitly acknowledges. Lambda runner changes require a redeploy to take effect, but that is an operational concern, not a code defect.

web/src/features/evals/components/inner-evaluator-form.tsx — the .catch() double-logs mutation errors; worth confirming the UX trade-off is intentional before merging.
</details>

<details><summary>Prompt To Fix All With AI</summary>

`````markdown
Fix the following 1 code review issue. Work through them one at a time, proposing concise fixes.

---

### Issue 1 of 1
web/src/features/evals/components/inner-evaluator-form.tsx:743-748
**`console.error` fires for mutation errors, not just post-success ones**

When the mutation itself fails, `onError: trpcErrorToast` fires (shows the toast) and the `mutateAsync` promise also rejects, which means this `.catch()` fires too — calling `console.error` for the same error that was already toast
