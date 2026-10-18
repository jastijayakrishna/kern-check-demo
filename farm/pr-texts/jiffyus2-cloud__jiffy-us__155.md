# fix: recalibrar los límites de texto de portada con medición real

Seguimiento de #154. Los límites de caracteres de la portada **se aplicaban pero quedaban cortos**: probando sobre 20x20 Papel, el texto seguía desbordando en L1 (título y subtítulo), L3 (subtítulo) y L4 (subtítulo).

Esta vez recalibrado **midiendo en el navegador**, no estimando.

## Qué resultó ser falso de lo que asumía #154

| Hipótesis en #154 | Realidad medida |
|---|---|
| Century Gothic es la más ancha del stack | Es **9% más estrecha que Arial** |
| `AVG_CHAR_EM = 0.61` para mayúsculas | Medido: **0.592** |
| La negrita ensancha (`+0.03 em`) | En Century Gothic **no ensancha**: 0.585 vs 0.592 |
| `usableWidthPct` leído del CSS a mano | Medido campo a campo: **correcto, no cambió ningún valor** |

De paso quedó confirmada cuál es la fuente que realmente se pinta. `src/styles/fonts.css` está vacío y no hay ningún `@font-face`, así que el stack de `CoverPreview.tsx:510` se resuelve contra el SO; en Windows con Office gana Century Gothic. La comprobación se hace comparando anchos con `measureText` — `getComputedStyle().fontFamily` sólo devuelve la declaración CSS y no sirve para esto, que es justo el error de método que dejó pasar el bug en #154.

## Las causas reales

1. **El delta de negrita inexistente** inflaba el límite de todos los títulos.
2. **El margen era el problema de fondo.** Con `SAFETY = 0.95` el texto llegaba al **0.93** del ancho útil: sin aire. Basta que el texto real del usuario sea algo más ancho que el corpus de calibración (títulos cortos, más mayúsculas seguidas, menos espacios) para que desborde. Se sustituye por `FIT = 0.77`, calibrado contra los topes comprobados a ojo.

El lomo mantiene su propio margen (`SPINE_FIT = 0.90`): nunca falló y está verificado midiendo contra el renderer del PDF, que es código aparte.

## Resultado en 20x20 Papel

| | L1 t/s | L2 t/s | L3 t/s | L4 t/s |
|---|---|---|---|---|
| Antes | 28/35 | 23/24 | 23/20 | 49/51 |
| **Ahora** | **24/29** | 20/20 | 20/**17** | 43/**43** |
| Tope comprobado | 24/31 | ok | ok/18 | ok/45 |

Da en el clavo o queda 1–2 por debajo de cada tope medido, y aprieta también los campos que iban bien — el margen general que se pidió. El resto de familias se recalcula con las mismas constantes. El lomo queda igual (44/46/62/66).

Que título y subtítulo coincidan ahora en varios layouts no es un error: comparten tamaño de fuente y, sin delta de negrita, comparten límite.

## Verificación

- **Llenado máximo de las 31 combinaciones: 0.926 → 0.757.** Cero desbordes, y `lines === 1` en los 55 campos de texto.
- Idéntico a 200px y 900px de ancho (delta 0.002 = redondeo sub-píxel), que es lo que traslada el veredicto al export de 300 DPI.
- **Contraprueba**: a +4 caracteres todavía entra en una línea (0.879); a **+8 se rompen 8 combinaciones**. El límite sigue siendo ajustado, no arbitrario.
- Con texto real en español el llenado queda en **0.76–0.83** (`NUESTRA BODA`, `VACACIONES EN MADRID`, `MAMA Y PAPA`, `RECUERDOS 2026`).
- El lomo entra en los 4 tamaños replicando la geometría del PDF (llenado 0.88–0.90).
- 67 tests pasan. `typecheck` mantiene los mismos 29 errores de tipado de Firebase que ya había en `main`.

## Limitación que sigue en pie

Contar caracteres no puede garantizar el caso patológico: una cadena del largo máximo compuesta sólo de letras anchas (24 emes seguidas) todavía desbordaría, porque `M` mide 0.919 em frente a los 0.592 del promedio. Con nombres y frases reales hay margen de sobra. Cerrarlo del todo exigiría medir el ancho del texto en tiempo real con `measureText` en vez de contar caracteres — se puede añadir después sin tocar la tabla de geometría.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

