# feat: add authoritative booking settings

## Problem

Booking behavior was distributed across route-specific constants, so the backend, public calendar, admin calendar, Stripe flows, and appointment validation could disagree. The project needs one authoritative Payload Global while preserving Europe/Dublin timezone and DST behavior.

## Implementation summary

- Add the Booking Settings Payload Global with duration, hold, booking horizon, weekly hours, closed days, breaks, buffers, holidays, closures, and blocked intervals.
- Add strict shared settings resolution with safe defaults and tagged cache invalidation.
- Refactor public booking, admin booking, availability, appointment integrity, and Stripe prechecks to use the same resolved settings.
- Add buffer-aware conflict detection and a short-lived date mutex to serialize concurrent adjacent bookings safely.
- Keep stored appointment duration authoritative on private payment and pending pages.

## Files changed

- Payload schema and hooks: src/BookingSettings, src/payload.config.ts, src/payload-types.ts.
- Booking domain: src/config/booking.ts and src/lib/booking.
- Public/admin/Stripe consumers: booking routes, booking components, appointment calendar, appointment collection, and Stripe handlers.
- Migration: src/migrations/20260801_210000_create_booking_settings.ts and migration registry.
- Tests: booking settings, conflicts, locks, calendars, security, dress availability, dress detail, and Stripe webhook coverage.

## Migration notes

- Migration 20260801_210000_create_booking_settings creates the Global only when missing.
- Existing Booking Settings data is validated and left unchanged.
- Seeded data is marked so rollback can distinguish it from pre-existing or subsequently edited data.
- No appointments are rewritten and no production migration has been run from this branch.

## Rollback notes

- The down migration deletes only an untouched Global created by this migration.
- It refuses to reinterpret or remove pre-existing or edited settings.
- Application rollback restores previous constants; existing appointment timestamps remain unchanged.

## Tests added or updated

- npm ci
- npm run generate:types
- npm run generate:importmap
- generated-file idempotency gate
- npx tsc --noEmit
- npm run lint
- focused booking settings and slot-lock tests: 13/13 passed
- npm run test:int: 31 files, 267/267 passed
- npm run build: passed with ephemeral in-memory secrets and repository production URL
- git diff --check

Lint retains one pre-existing warning in src/collections/Media.ts for an unused dirname import.

## Screenshots

Not included per request. No safe staging database was available for local browser verification, and production customer data was not accessed.

## Manual verification

1. Apply the migration in a non-production environment.
2. In Payload admin, update weekly hours, closures, buffers, and holidays.
3. Confirm public and admin calendars expose the same Europe/Dublin slots across a DST boundary.
4. Attempt concurrent same-day and adjacent buffered bookings; confirm one succeeds and the conflicting request receives a safe retryable conflict.
5. Confirm pending, success, and cancellation URLs remain private, noindex, and no-store.
6. Replay a Stripe webhook event and confirm appointment validation remains idempotent.

## Security and privacy

- Backend settings and appointment checks remain authoritative.
- Customer phone numbers, notes, full email content, secrets, and unnecessary Stripe data are not logged.
- Private booking/payment route protections are preserved.
- Mutex records contain only date-scoped booking coordination data, not customer PII.

## Accessibility

Existing semantic booking controls and labels are preserved. No new customer-facing interaction pattern was introduced. Manual keyboard and screen-reader smoke testing remains part of staging verification.

## SEO and cache

- Booking Settings changes invalidate 
