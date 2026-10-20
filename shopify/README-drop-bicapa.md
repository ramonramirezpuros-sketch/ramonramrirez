# Landing Drop Bicapa · Edición Especial

Landing de Shopify basada en el VSL **"Giuliano VSL_Corregido 1.mp4"** (Drive → RAMÓN RAMIREZ → VIDEOS CRUDOS / TERMINADOS → TERMINADO → VSL DROP BICAPA).

## Qué hay instalado en Shopify

| Qué | Dónde | Estado |
|---|---|---|
| Tema `WEB RAMON RAMIREZ - SHOPIFY` | Tienda online → Temas | Publicado, con todo el drop (landing, banner, fecha del metacampo). La copia del 20/10 con el mismo nombre suma el máximo de 10 por compra y que la landing se actualice sola a las 00:00: **falta publicarla** y borrar las otras dos |
| Metacampo de la tienda `drop_bicapa.start` | Se cambia por API (pedímelo) | `2026-10-25T00:00-03:00`. Si la fecha vuelve a cambiar, se cambia acá y no hace falta publicar nada |
| `sections/drop-bicapa.liquid` | En el tema | Sección completa de la landing |
| `templates/page.drop-bicapa.json` | En el tema | Plantilla de página que usa la sección |
| Página `Drop Bicapa · Edición Especial` (`/pages/drop-bicapa`) | Tienda online → Páginas | **Visible** (13/10), usa la plantilla `drop-bicapa` |
| Banner de la página de inicio ([`snippets/drop-bicapa-banner.liquid`](snippets/drop-bicapa-banner.liquid)) | Sección "Banner Drop Bicapa" arriba de todo en la portada: un Liquid personalizado que solo hace `{% render 'drop-bicapa-banner' %}` | Publicado. Cambia solo a la hora de apertura y al agotarse. En el celular es una franja de ~160 px |
| Producto `Bicapa Edición Especial · Reposado en Ron` (`bicapa-edicion-especial`) | Productos | Precio $28.000, stock 100, no listado (no sale en colecciones ni en el buscador). **Programado para publicarse solo en la Tienda online el dom 25 a las 00:00**: no hace falta tocarlo |
| Video `vsl-drop-bicapa.mp4` + fotos `bicapa-portada.jpg`, `bicapa-estuche.jpg` | Contenido → Archivos | Subidos |

## Cómo funciona la página

Una sola URL con 3 fases que cambian solas según la fecha de apertura:

1. **Lista de espera** (antes de la apertura, o si no hay fecha / producto activo): VSL + formulario
   (nombre, email, WhatsApp, check de +18). Cada anotado queda como cliente con la etiqueta
   `drop-bicapa` y el WhatsApp como etiqueta `wa-<número>`. Si hay fecha cargada, muestra la cuenta regresiva.
2. **Venta abierta** (desde la apertura durante N horas, con producto activo, precio > 0 y stock):
   precio, barra "Quedan X de 100", cuenta regresiva al cierre y botón que va directo al checkout.
   Desde la copia del tema del 20/10: si a la hora de apertura el
   producto todavía no está publicado, la página dice "Estamos abriendo el drop" y se recarga sola apenas aparece
   (lo revisa cada ~5 s durante 30 minutos), aunque la tengan abierta desde antes.
3. **Edición cerrada** (pasadas las N horas o sin stock): mensaje de agotado + formulario para el
   próximo drop (etiqueta `drop-bicapa-proximo`).

Todo se edita desde el editor del tema (sección "Drop Bicapa"): producto, duración, unidades,
textos, video, fotos, etiquetas y mensaje sanitario. La **fecha de apertura** sale del metacampo de la
tienda `drop_bicapa.start`; el campo "Apertura del drop" del editor se usa solo si ese metacampo no existe.

## Checklist para salir

**Ya (antes del sábado):**
1. Tienda online → Temas → la copia de `WEB RAMON RAMIREZ - SHOPIFY` agregada el 20/10 → **⋯ → Publicar**.
2. Borrar las copias de `WEB RAMON RAMIREZ - SHOPIFY` que quedan sin publicar.
3. Abrir ramonramirez.com.ar y `/pages/drop-bicapa`: tienen que decir "domingo 25" y mostrar la cuenta regresiva.

**Producto:** no tocarlo. Ya tiene stock 100 y precio, y se publica solo en la Tienda online el dom 25 a las 00:00.

**Dom 25, 00:00:**
- Recargar la landing: precio, "Quedan 100 de 100" y botón "Comprar mi bicapa". Compra de prueba (después reembolsar).
- Si a las 00:05 no aparece el botón: producto → recuadro **Publicación** → tildar **Tienda online** → Guardar y recargar.
- Avisar a la lista: Clientes → segmento `customer_tags CONTAINS 'drop-bicapa'` → Shopify Email; y WhatsApp a las etiquetas `wa-…`.

**Al agotarse:**
- La página pasa sola a "Edición cerrada" y el banner a "Se agotaron".

## Notas

- **Máximo 10 por compra** (desde la copia del tema del 20/10): el selector de cantidad va de 1 a 10, o hasta el stock si quedan menos. Se cambia en "Máximo por compra" (0 = sin límite). Es un tope de la landing, no por cliente: alguien puede hacer más de una compra. El banner de la portada dice "Máximo 10 por compra" en [`snippets/drop-bicapa-banner.liquid`](snippets/drop-bicapa-banner.liquid): si cambia el tope, cambiarlo también ahí.
- **Clientes ya existentes:** si el email ya está registrado, Shopify puede no sumar la etiqueta nueva. Conviene revisar también por fecha de alta.
- **Legal (Ley 26.687 y reglamentación):** la publicidad de tabaco solo está permitida en comunicaciones directas a mayores de 18 con consentimiento previo y edad verificada, y siempre con un mensaje sanitario (art. 7). La venta a distancia exige verificar fehacientemente que comprador y receptor son mayores de 18. La página incluye el mensaje sanitario, el check de +18 y el aviso legal, y la tienda ya tiene una app de verificación de edad. **Confirmar con un asesor legal** el mensaje sanitario exacto y cómo se verifica la edad en la entrega.
