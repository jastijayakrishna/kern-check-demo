# Sidebar: gerahmter Active-State und stabile Slide-Animation

<!-- CURSOR_AGENT_PR_BODY_BEGIN -->
Die aktive Sidebar-Zeile war ein flacher Pill mit einer 2px-Kante am linken Rand. Die Slide-Animation ist zusätzlich an zwei Stellen gebrochen: die Position war hart auf `index * 2.5rem` gerechnet, und beim Gruppenwechsel ist der Indikator nach oben zur ersten Zeile zurückgerutscht. Weil die Sidebar in jeder Seite neu gemountet wurde, ist die Bewegung außerdem mitten in der Transition abgebrochen.

## Design

- Auswahl als **gerahmter Chip**: Fill, Inset-Hairline, leichte Top-Kante
- Statt der bündigen Kante: **3px-Kapsel innen** im Chip
- Aktives Icon in einem **invertierten Well** (wie das Brand-Mark)
- Hover der anderen Zeilen bleibt leiser, damit er nicht mit dem Frame konkurriert

## Animation

- Position kommt aus dem DOM (`offsetTop` / `offsetHeight` + ResizeObserver), nicht aus Rem-Arithmetik
- Innerhalb einer Gruppe: Slide
- Beim Verlassen einer Gruppe: Fade am letzten Ort, kein Snap nach oben
- Beim Betreten: Snap auf die Zielzeile, dann Fade-in
- Erste Paint ohne Transition, damit der Indikator nicht vom oberen Rand einfährt
- `prefers-reduced-motion` bleibt instant

## Shell

Sidebar, Mobile-Nav und Command-Palette sitzen jetzt in einem persistenten `AppShell` im Root-Layout. Nur Header/Panel wechseln noch per Page-Transition. Die Auswahl-Animation kann dadurch zu Ende laufen.

## Tests

- `nextNavHighlight`: Hide behält die Box, Enter slidet nicht, Move slidet, First Paint slidet nicht
- `activeToolFromPathname`: Home, Nested ASN, Legal-Seiten ohne Active

<!-- CURSOR_AGENT_PR_BODY_END -->

<div><a href="https://cursor.com/agents/bc-33c3cbb0-00c9-464a-ba90-1c60bbc4c416?cursor_ref=pr_footer&cursor_cta=open_in_web"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-web-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-web-light.png"><img alt="Open in Web" width="114" height="28" src="https://cursor.com/assets/images/open-in-web-dark.png"></picture></a>&nbsp;<a href="https://cursor.com/background-agent?bcId=bc-33c3cbb0-00c9-464a-ba90-1c60bbc4c416&cursor_ref=pr_footer&cursor_cta=open_in_cursor"><picture><source media="(prefers-color-scheme: dark)" srcset="https://cursor.com/assets/images/open-in-cursor-dark.png"><source media="(prefers-color-scheme: light)" srcset="https://cursor.com/assets/images/open-in-cursor-light.png"><img alt="Open in Cursor" width="131" height="28" src="https://cursor.com/assets/images/open-in-cursor-dark.png"></picture></a>&nbsp;</div>


