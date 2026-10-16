# feat(table-stateful): add public `resetSort()` method

## What changed?

`KolTableStateful` gains a new public `resetSort()` async method that restores the sort state to the default directions defined in the `_headers` prop. The sort initialization logic was extracted from the `validateHeaders` watcher into a private `initializeSortFromHeaders()` helper to make it reusable. Calling `resetSort()` re-applies the header-defined sort and immediately refreshes the displayed data, allowing consumers to programmatically restore the default column order after the user has interacted with sort buttons. Two e2e tests cover the method — one with a default sort direction defined in headers and one where no default is set and sorting is fully cleared. A new sample page `stateful-reset-sort` demonstrates the feature with a "Reset Sort" button.

## Linked issues

No linked issues.

## Type of change

- [x] ✨ New feature
- [ ] 🔼 Improvement
- [ ] 🐛 Bug fix
- [ ] 💥 Breaking change
- [ ] 🔧 Internal (no release note needed)

## Checklist

- [x] PR title follows Conventional Commits format
- [ ] Linked issues are referenced
- [x] Breaking changes are documented

---

<details>
<summary>🇩🇪 Deutsche Zusammenfassung</summary>

### Was wurde geändert?

`KolTableStateful` erhält eine neue öffentliche asynchrone Methode `resetSort()`, die den Sortierstatus auf die in der `_headers`-Prop definierten Standardrichtungen zurücksetzt. Die Initialisierungslogik für die Sortierung wurde aus dem `validateHeaders`-Watcher in eine private Hilfsmethode `initializeSortFromHeaders()` ausgelagert. Der Aufruf von `resetSort()` wendet die Header-Standardsortierungen erneut an und aktualisiert sofort die angezeigten Daten. Zwei E2E-Tests decken das Verhalten ab — einmal mit definierter Standard-Sortierrichtung, einmal ohne. Eine neue Beispielseite `stateful-reset-sort` demonstriert das Feature mit einem „Reset Sort"-Button.

### Verknüpfte Tickets

Keine verknüpften Tickets.

### Art der Änderung

✨ Neues Feature

### Geänderte Dateien

- `packages/components/src/components/table-stateful/shadow.tsx` — Private Hilfsmethode `initializeSortFromHeaders()` extrahiert; öffentliche `resetSort()`-Methode hinzugefügt
- `packages/components/src/components/table-stateful/table-stateful.e2e.ts` — E2E-Tests für `resetSort()` hinzugefügt
- `packages/samples/react/src/components/table/stateful-reset-sort.tsx` — Neue Beispielseite mit „Reset Sort"-Button
- `packages/samples/react/src/components/table/routes.ts` — Route für `stateful-reset-sort` registriert

</details>
