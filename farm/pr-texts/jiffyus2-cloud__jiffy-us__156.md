# feat: textura de lienzo en la portada de tela (solo previsualización)

## Qué cambia

Cuando el usuario elige carátula tipo **Tela**, la previsualización en pantalla ya no se ve como un blanco plano: ahora la portada tiene una textura de lienzo en tono marfil, con los textos encima.

El **PDF de impresión queda idéntico a como estaba** (blanco plano), porque ahí la tela es física.

## Por qué

El flujo de Tela fuerza `coverImage = justwhite.png` (`AlbumCustomization.tsx:97`) y `CoverPreview` la pinta estirada, así que el cliente veía una portada blanca que no se parecía al producto real. El `coverColor` que se guarda para Tela (`#E8DCC4`) nunca se usaba para renderizar nada.

## Implementación

- **`CoverPreview.tsx`**
  - Nueva prop explícita `forPdf` (default `false`).
  - `CANVAS_TEXTURE`: CSS puro, sin assets nuevos. Base marfil `#F7F4ED` + hilos de urdimbre (4px) y trama (3px) con **distinto paso** para que no lea como cuadrícula de papel milimetrado, fibras finas y manchas suaves de tejido con `feTurbulence` en data-URI, y un vignette cálido.
  - La capa va en `z-[1]`: sobre la imagen blanca (`z-0`) y bajo los textos (`z-10`), en los 3 layouts de Tela. Es opaca, y no puede tapar contenido del usuario porque la portada de Tela nunca lleva foto (`hidePhoto = coverType === 'Tela'`).
- **`OwnerDashboard.tsx`** — `forPdf={true}` en el render offscreen de impresión, el único call-site que lo necesita.

### Nota para quien revise

`hideSpine` venía haciendo doble trabajo: "sin lomo" **y** "modo impresión PDF" (lo decía su propio comentario). Se apoyaba en que solo el export lo pasa en `true`, lo cual es frágil. Esa segunda responsabilidad pasa ahora a `forPdf`; el comportamiento de `hideSpine` (sombras y lomo) no se toca.

Los otros 4 call-sites (configuración del álbum, editor de portada ×2, modal admin de detalles del pedido) heredan `forPdf = false` y muestran la textura, que es el alcance acordado.

## Verificación

El login de Firebase bloquea el flujo real, así que monté el componente real en una página temporal de Vite y la capturé con Chrome headless (la página temporal ya está borrada; el diff son solo los 2 archivos). Comprobado a 1x y 2x:

- Los 3 layouts de Tela y los 4 tamaños muestran la trama, sin costuras ni desbordes — la capa mide exactamente lo mismo que `data-cover-root`.
- Tipografía dorada, plateada y negra siguen legibles encima.
- Con `forPdf`, la portada de Tela renderiza solo 2 hijos (overlay + textos): **sin** capa de textura, blanco plano idéntico al output actual.
- Papel queda intacto, con su lomo.
- Sin errores de consola. `tsc --noEmit` solo arroja los errores preexistentes de tipados de Firebase, ninguno en los archivos tocados.

Pendiente de validar por alguien con acceso: generar un PDF de portada real de un pedido de Tela desde el OwnerDashboard y confirmar que sale igual que antes.

Detalle menor, no es regresión: el plateado `#C0C0C0` tiene poco contraste sobre el marfil, pero ya lo tenía sobre el blanco anterior.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
