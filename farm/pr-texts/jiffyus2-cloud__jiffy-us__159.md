# feat: textura de lienzo en la portada de tela (reaplica #156 con la trama al 20%)

Reaplica el cambio del #156, que se revirtió en el #157, **con el ajuste que se quedó fuera de aquel merge**.

## Por qué se revirtió y qué cambia respecto al #156

El merge del #156 llevó solo el primer commit: la trama de tela a plena opacidad, que competía con el título y estorbaba la lectura. El ajuste que la baja al **20%** se subió a la rama después del merge y nunca llegó a `main`, así que lo que se probó y se revirtió era la versión fuerte.

Este PR trae las dos cosas juntas. No hay ningún otro cambio respecto al #156.

## Qué hace

Cuando el usuario elige carátula tipo **Tela**, la previsualización en pantalla ya no es un blanco plano: la portada tiene una textura de lienzo en tono marfil, con los textos encima. El **PDF de impresión queda idéntico** (blanco plano), porque ahí la tela es física.

El flujo de Tela fuerza `coverImage = justwhite.png` (`AlbumCustomization.tsx:97`) y `CoverPreview` la pinta estirada, así que el cliente veía una portada blanca que no se parecía al producto real.

## Implementación

- **`CoverPreview.tsx`**
  - Nueva prop explícita `forPdf` (default `false`).
  - `CANVAS_BASE` — el tono marfil `#F7F4ED` a opacidad completa, en su propia capa. Va aparte a propósito: si la opacidad se aplicara al div entero, el marfil se volvería translúcido sobre la imagen blanca de abajo y se perdería el tono.
  - `CANVAS_TEXTURE` — hilos de urdimbre (4px) y trama (3px) con **distinto paso** para que no lea como cuadrícula de papel milimetrado, fibras finas y manchas suaves de tejido con `feTurbulence` en data-URI, y un vignette cálido. Todo en un hijo con `opacity: 0.2`. CSS puro, sin assets nuevos.
  - La capa va en `z-[1]`: sobre la imagen blanca (`z-0`) y bajo los textos (`z-10`), en los 3 layouts de Tela. Es opaca en su base, y no puede tapar contenido del usuario porque la portada de Tela nunca lleva foto (`hidePhoto = coverType === 'Tela'`).
- **`OwnerDashboard.tsx`** — `forPdf={true}` en el render offscreen de impresión, el único call-site que lo necesita.

### Nota para quien revise

`hideSpine` venía haciendo doble trabajo: "sin lomo" **y** "modo impresión PDF" (lo decía su propio comentario). Se apoyaba en que solo el export lo pasa en `true`, lo cual es frágil. Esa segunda responsabilidad pasa ahora a `forPdf`; el comportamiento de `hideSpine` (sombras y lomo) no se toca.

Los otros 4 call-sites (configuración del álbum, editor de portada ×2, modal admin de detalles del pedido) heredan `forPdf = false` y muestran la textura, que es el alcance acordado.

## Verificación

El login de Firebase bloquea el flujo real, así que monté el componente real en una página temporal de Vite y la capturé con Chrome headless (la página temporal ya está borrada; el diff son solo los 2 archivos). Comprobado a 1x y 2x:

- Capa base en `rgb(247,244,237)` a opacidad 1, trama en `0.2`, cubriendo exactamente el mismo rectángulo que `data-cover-root`.
- Los 3 layouts de Tela y los 4 tamaños muestran la trama como grano de fondo, sin costuras ni desbordes; título y subtítulo se leen limpios.
- Tipografía dorada, plateada y negra legibles encima.
- Con `forPdf`, la portada de Tela renderiza solo 2 hijos (overlay + textos): **sin** capa de textura, blanco plano idéntico al output actual.
- Papel queda intacto, con su lomo.
- Sin errores de consola. `tsc --noEmit` solo arroja los errores preexistentes de tipados de Firebase, ninguno en los archivos tocados.

Pendiente de validar por alguien con acceso: generar un PDF de portada real de un pedido de Tela desde el OwnerDashboard y confirmar que sale igual que antes.

Si al verlo en producción la trama sigue distrayendo, el número está en un solo sitio (`opacity: 0.2` en `CANVAS_TEXTURE`) y se puede bajar a 0.12–0.15 sin tocar nada más.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
