# Landing Drop Bicapa · Edición Especial

Landing de Shopify basada en el VSL **"Giuliano VSL_Corregido 1.mp4"** (Drive → RAMÓN RAMIREZ → VIDEOS CRUDOS / TERMINADOS → TERMINADO → VSL DROP BICAPA).

## Qué hay instalado en Shopify

| Qué | Dónde | Estado |
|---|---|---|
| Tema copia `RR - Drop Bicapa (borrador)` | Tienda online → Temas | Sin publicar. Es una copia exacta del tema actual + los 2 archivos de abajo |
| `sections/drop-bicapa.liquid` | En el tema borrador | Sección completa de la landing |
| `templates/page.drop-bicapa.json` | En el tema borrador | Plantilla de página que usa la sección |
| Página `Drop Bicapa · Edición Especial` (`/pages/drop-bicapa`) | Tienda online → Páginas | **Oculta**, usa la plantilla `drop-bicapa` |
| Producto `Bicapa Edición Especial · Reposado en Ron` (`bicapa-edicion-especial`) | Productos | **Borrador**, precio $0, stock 0 (inventario controlado, no vende sin stock) |
| Video `vsl-drop-bicapa.mp4` + fotos `bicapa-portada.jpg`, `bicapa-estuche.jpg` | Contenido → Archivos | Subidos |

## Cómo funciona la página

Una sola URL con 3 fases que cambian solas según la fecha de apertura:

1. **Lista de espera** (antes de la apertura, o si no hay fecha / producto activo): VSL + formulario
   (nombre, email, WhatsApp, check de +18). Cada anotado queda como cliente con la etiqueta
   `drop-bicapa` y el WhatsApp como etiqueta `wa-<número>`. Si hay fecha cargada, muestra la cuenta regresiva.
2. **Venta abierta** (desde la apertura durante N horas, con producto activo, precio > 0 y stock):
   precio, barra "Quedan X de 100", cuenta regresiva al cierre y botón que va directo al checkout.
3. **Edición cerrada** (pasadas las N horas o sin stock): mensaje de agotado + formulario para el
   próximo drop (etiqueta `drop-bicapa-proximo`).

Todo se edita desde el editor del tema (sección "Drop Bicapa"): producto, fecha de apertura,
duración, unidades, textos, video, fotos, etiquetas y mensaje sanitario.

## Checklist para salir

**Para abrir la lista de espera (ya se puede):**
1. Tienda online → Temas → `RR - Drop Bicapa (borrador)` → Personalizar → elegir la página "Drop Bicapa" y revisar.
2. Publicar ese tema (o copiar los 2 archivos al tema actual desde "Editar código").
   ⚠️ Si se publica la copia, cualquier cambio hecho en el tema actual después del 05/10/2026 no está en la copia.
3. Páginas → Drop Bicapa → poner **Visible**. Link para el VSL: `https://ramonramirez.com.ar/pages/drop-bicapa`

**Antes del drop:**
- Producto: cargar **precio**, vitola/detalles si se quieren mostrar, y fotos.
- En la sección: cargar **Apertura del drop** con formato `2026-10-11T20:00-03:00`.

**El día del drop (a la hora de apertura):**
- Producto → stock **100** → estado **Activo** (publicado en Tienda online).
- Avisar a la lista: Clientes → segmento `customer_tags CONTAINS 'drop-bicapa'` → Shopify Email; y WhatsApp a las etiquetas `wa-…`.

**Al cerrar (24 h):**
- Producto → pasar a **Borrador** o stock 0. La página muestra "cerrado" sola, pero el cierre real lo hace el producto.

## Notas

- **Máximo 1 por compra:** el botón agrega 1 unidad, pero no impide que alguien compre dos veces. Para un límite real hace falta una app de límites de compra.
- **Clientes ya existentes:** si el email ya está registrado, Shopify puede no sumar la etiqueta nueva. Conviene revisar también por fecha de alta.
- **Legal (Ley 26.687 y reglamentación):** la publicidad de tabaco solo está permitida en comunicaciones directas a mayores de 18 con consentimiento previo y edad verificada, y siempre con un mensaje sanitario (art. 7). La venta a distancia exige verificar fehacientemente que comprador y receptor son mayores de 18. La página incluye el mensaje sanitario, el check de +18 y el aviso legal, y la tienda ya tiene una app de verificación de edad. **Confirmar con un asesor legal** el mensaje sanitario exacto y cómo se verifica la edad en la entrega.
