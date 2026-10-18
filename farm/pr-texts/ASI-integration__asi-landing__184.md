# fix: use canonical property knowledge readiness boundary

## Результат

Unit readiness теперь читает каноническую Telegram-схему property knowledge и безопасно блокируется при ошибке запроса. Успешный запрос без строки по-прежнему отличается от ошибки базы.

## Scope

- Task: UNIT READINESS PROPERTY KNOWLEDGE BOUNDARY
- Baseline SHA: `e47d7510f1d8f48724647b8325a640d9974e7d6e`
- In scope: `checkReadinessGates()` и focused unit-state regression tests
- Out of scope: auth из PR #183, migrations/DB writes, public intake scoping, providers, repository/deployment topology, public UX и unrelated lifecycle behavior

## Root cause и исправление

- Исправлена таблица: `property_knowledge` → `tg_property_knowledge`
- Исправлено поле: `check_in_instructions` → `checkin_instructions`
- Ошибка Supabase больше не игнорируется: readiness возвращает безопасную стабильную причину `property_knowledge_lookup_failed`
- Детали ошибки базы не возвращаются
- После ошибки lookup выполнение прекращается до запроса turnover tasks
- Успешный lookup с `data=null` сохраняет `property_knowledge_missing`
- Остальные readiness reasons и переходы сохранены

## Autonomy и риск

- Уровень: `yellow`
- Merge и production actions не выполнялись
- Rollback: revert commit `d7f31c9b50e536f0a0b597c0c61e18de09cc6ffe`

## Проверки

| Check | Result | Evidence |
| --- | --- | --- |
| Focused unit-state tests | PASS | 1 file, 24 tests |
| Touched-file ESLint | PASS | 2 touched TypeScript files |
| Typecheck | PASS | `npm.cmd run typecheck` |
| Production build | PASS | `npm.cmd run build` |
| `git diff --check` | PASS | working and staged diff |
| Exact diff review | PASS | 2 task-relevant files only |
| Repository PR Validation | PASS | validate 3m33s; PostgreSQL job 1m1s |

Broad suite не запускался по testing budget.

## Side effects

- Migrations не менялись и не применялись
- Production/staging data не читались и не изменялись
- Secrets не читались, не печатались и не менялись
- DNS, платежи, реальные сообщения и provider calls не затрагивались
- Auth/public UX/public copy не менялись

## Checklist

- [x] Canonical table and column used
- [x] Missing row and query error are distinguishable
- [x] Query errors fail closed before subsequent readiness work
- [x] Existing readiness behavior remains covered
- [x] No unrelated files, package changes, or generated files
- [x] Repository PR Validation green
- [x] PR remains draft

