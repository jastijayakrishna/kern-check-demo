# feat(ops): גל 2 — dispatch persist, crons, QR PDF

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
## Summary

גל 2 מהתוכנית [`docs/CORE_FEATURES_ROADMAP.md`](docs/CORE_FEATURES_ROADMAP.md) — **הושלם** (גל 1 כבר ב־main דרך #48).

- **Partner dispatch → Supabase** — persist ל־`vendor_dispatches`, idempotent, fallback ל־memory
- **Cron דוח חודשי** — `/api/cron/monthly-report` (1 לחודש 06:00 UTC) + snapshot + PDF במייל
- **Cron ללא שיוך** — `/api/cron/unassigned-timeout` כל 15ד׳ (`UNASSIGNED_TIMEOUT_HOURS`, ברירת מחדל 2)
- **QR PDF batch** — `/api/stores/qr-batch?format=pdf`
- `ops-notify` קורא `getSettings()` (לא רק memory)

מחוץ להיקף (נשאר אחרי go-live): Zapier, Web Push, i18n FR.

## Checklist

- [x] Unit / typecheck pass (234 tests)
- [x] Smoke: crons + QR PDF (8 עמודים)
- [x] No orphan components

## Test plan

- [x] `npm run typecheck && npm test`
- [x] `GET /api/cron/unassigned-timeout` → `{ ok: true }`
- [x] `GET /api/cron/monthly-report?force=1` → snapshot
- [x] `GET /api/stores/qr-batch?format=pdf` → `application/pdf`

הגדרות נדרשות ב־prod: `CRON_SECRET`, `RESEND_API_KEY`, `notify_email` בהגדרות Ops, `NEXT_PUBLIC_WA_BUSINESS_PHONE` ל־QR.
<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-01a05710-8cba-7d50-9e12-429c141fb48b?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-01a05710-8cba-7d50-9e12-429c141fb48b&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>


