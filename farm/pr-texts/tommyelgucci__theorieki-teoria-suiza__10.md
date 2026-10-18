# Ampliar banco de preguntas (+20) y corregir hueco de césped en maniobras

## Summary
- Ronda 8 del banco de preguntas: +20 preguntas nuevas, 5 temas (`velokindersitz`, `wenden`, `dachtransport`, `gruenekarte`, `wechselschild`), en los 6 idiomas. Banco: 314 → 334 preguntas.
- Fix de un bug visual en "Animated manoeuvres" (`laengere_strecke_rueckwaerts` / `links_abbiegen_einspuren`): faltaba césped en una franja de `junctionScene()` junto a la calle secundaria, quedaba transparente. El margen este ahora es un único bloque de césped continuo (altura completa) con un borde (`curbLine`) también continuo, sin costuras.

Este PR reemplaza al #8 (revertido en #9): incluye solo la ronda de preguntas y el fix del césped — deliberadamente **sin** los ajustes de posición del coche ni la ampliación de calle que se probaron para ese mismo bug, que no quedaron bien y se descartaron.

## Test plan
- [x] `npm run lint` — 0 errores
- [x] `npm test` — 104/104
- [x] `npx vitest run src/data/maneuvers.test.js` — 34/34 (geometría de las maniobras)
- [x] `npm run build` — sin errores
- [x] Verificación visual del paso 6 de "Reversing a longer distance"

--
