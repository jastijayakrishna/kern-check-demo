# Rehacer geometría de rotondas (diagramas + maniobra animada) y ampliar Kreisverkehr

## Summary
- Los 3 diagramas de kreisel en preguntas de examen (1ª salida, 2ª+ salida, doble carril) tenían trayectorias con quiebres visibles, desvíos hacia el lado incorrecto antes de girar, o flechas de salida que quedaban apuntando de lado en vez de conectar con la calle de salida. Rehechos con coordenadas polares centradas en el anillo (`x = cx + r·sen(φ)`, `y = cy + r·cos(φ)`, tangente exacta `heading = 90 - φ`) y verificados con un script que muestrea cada curva contra la calzada real (calle ∪ anillo), no solo a ojo.
- Maniobra animada nueva "Kreisel: die richtige Ausfahrt nehmen" (`src/data/maneuvers.js`, categoría B) con 4 variantes (1ª–4ª salida), generada con el mismo enfoque paramétrico. Se amplió el ancho de las 4 calles de la escena (76→130px) y se recalculó el offset de carril del coche en consecuencia, para que circule pegado a su carril y no por el centro de la calle.
- +8 preguntas nuevas de Kreisverkehr (`src/data/questions.json`, 334→342 preguntas), 2 por cada uno de 4 subtemas: peatones y ciclistas, vehículos grandes/camiones, vehículos de emergencia, y Minikreisel — redactadas desde cero a partir de fuentes suizas (TCS, BFU, ACS), no copiadas del banco oficial. Conteos hardcodeados actualizados en `Home.test.jsx`, `Study.test.jsx` y el comentario de `questionBank.js`.

## Test plan
- [x] `npm run lint` — 0 errores, 0 warnings
- [x] `npm test` ×8 seguidas — 112/112 cada vez (el banco se baraja al azar, una sola corrida no basta)
- [x] `npx vitest run src/data/maneuvers.test.js` — 42/42
- [x] `npm run build` — sin errores
- [x] Verificación visual real en navegador (Playwright) de los 3 diagramas corregidos, las 4 variantes de la maniobra animada, y el conteo de preguntas del filtro Kreisverkehr (11→19)

Detalle completo del proceso (incluida la iteración con varios intentos fallidos antes de llegar al enfoque de coordenadas polares) en `CHECKPOINT.md`.


