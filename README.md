# Ramón Ramírez: proyecto Drop Bicapa Edición Especial

Base de trabajo del lanzamiento de **100 puros bicapa reposados 6 meses en ron**.
Lista de espera hasta el **domingo 25/10 a las 00:00** (antes era el 18); desde ahí, venta abierta hasta agotar stock.
Anuncios y estrategia desde el **lunes 19/10 a las 00:00**.

## Estado

| Pieza | Estado | Dónde |
|---|---|---|
| VSL (video final) | ✅ Terminado | Drive: `RAMÓN RAMIREZ / VIDEOS CRUDOS / TERMINADOS / TERMINADO / VSL DROP BICAPA` · [transcripción](vsl/transcripcion-vsl-final.md) |
| Landing en Shopify | ✅ Publicada con el domingo 25: ramonramirez.com.ar/pages/drop-bicapa. Todo el drop quedó también en el tema `WEB RAMON RAMIREZ - SHOPIFY` | [código y guía](shopify/README-drop-bicapa.md) |
| Banner en la página de inicio | ✅ Publicado con el domingo 25. Versión compacta para celular: falta publicar el tema nuevo | [drop-bicapa-banner.liquid](shopify/snippets/drop-bicapa-banner.liquid) |
| Producto en Shopify | 🟡 Precio cargado, todavía fuera de la tienda online. Stock en 1000: pasarlo a 100 el sáb 24 | `bicapa-edicion-especial` |
| Fecha del drop | ✅ Domingo 25/10 00:00 hs (antes 18/10), con cuenta regresiva. Venta sin límite de tiempo, hasta agotar stock | Metacampo de la tienda `drop_bicapa.start`: la landing y el banner leen la fecha de ahí |
| Precio | ✅ $28.000 | Producto en Shopify |
| Funnel del drop (Miro) | 🟡 Plan de ejecución en el PDF; falta armar ManyChat | [plan y mensajes](estrategia/funnel-drop.md) · [PDF](docs/Drop-Bicapa-Paso-a-paso.pdf) |
| Anuncios (8) | 🟡 Arrancan el lunes 19/10 a las 00:00 (captación hasta el sáb 24 23:30). Texto de captación con "domingo 25" | [anuncios](estrategia/anuncios-transcripciones.md) · [Meta paso a paso](docs/Meta-Ads-Paso-a-paso.pdf) |
| Leads y visitas → Google Sheets | ✅ Conectado y probado de punta a punta | [planilla](https://docs.google.com/spreadsheets/d/1lXG7OjKNCnRWtaQDo-a_HAGtMmFgAkSOd3DNhRTJEKE/edit) · [cómo activarlo](google-sheets/README.md) |
| Legal (Ley 26.687) | ✅ Resuelto por el equipo | [notas legales](legal/ley-26687-tabaco.md) |

## Pendientes

- [ ] **Ya:** publicar el tema `WEB RAMON RAMIREZ - SHOPIFY` y borrar los 4 `RR - Drop Bicapa …`; corregir el mail de bienvenida
- [ ] Vie 16, 19:00: M0 (cambio de fecha) por email y WhatsApp a los que ya se anotaron
- [ ] Dom 18, antes de las 21: los 8 anuncios programados para el lunes 19 00:00, con "domingo 25" en el texto; ManyChat con "domingo 25"
- [ ] Nombres de los responsables de ManyChat, Email y WhatsApp
- [ ] Crear los estáticos "YA ESTÁN DISPONIBLES" y "SOLAMENTE QUEDAN 10" (subirlos el sáb 24 antes de las 12)
- [ ] Sáb 24, 22:00: producto activo en la tienda online con stock 100
- [ ] Borrar de la planilla las filas de prueba
- [ ] Opcional: pop-up de escasez en la tienda

## Estructura del repo

```
README.md                         ← este archivo: estado y pendientes
docs/
  Drop-Bicapa-Paso-a-paso.pdf     ← plan de ejecución: cronograma, historias de Ramón, ManyChat, email y WhatsApp
  Meta-Ads-Paso-a-paso.pdf        ← guía clic por clic para subir y controlar los anuncios en Meta
  WhatsApp-Drop-Bicapa.pdf        ← estrategia y mensajes día por día para quien hace WhatsApp
  Anuncios-Lunes-a-Viernes.pdf    ← cuadro de una página: qué anuncios corren cada día y qué hay que tocar
  paso-a-paso/, meta-ads/, whatsapp/, anuncios/ ← fuentes HTML de los PDF
vsl/
  transcripcion-vsl-final.md      ← lo que dice el video final, con tiempos
  VSL_drop_bicapa_edicion_especial.md  ← guion de referencia inicial (estilo Davidoff) + teoría de VSL
shopify/
  README-drop-bicapa.md           ← qué está instalado y checklist del día del drop
  sections/drop-bicapa.liquid     ← sección de la landing (tema Dawn)
  snippets/drop-bicapa-banner.liquid ← banner "Anotate a los bicapa" de la portada (compacto en el celular)
  templates/page.drop-bicapa.json ← plantilla de página
  preview/                        ← capturas de la landing
estrategia/
  funnel-drop.md                  ← etapas del tablero de Miro + mensajes por etapa
  anuncios-transcripciones.md     ← los 8 anuncios: qué dicen y cuándo corren
google-sheets/
  README.md                       ← cómo activar el envío de datos a la planilla
  apps-script-landing.gs          ← conector que escribe en la planilla
legal/
  ley-26687-tabaco.md             ← publicidad, venta a distancia y plataformas
```

## Datos de referencia

- **Tienda:** ramonramirez.com.ar (Shopify, ARS, tema Dawn 15.2 personalizado)
- **Bicapa actual:** variante de la ½ Corona Ramírez, $21.250 (sin stock)
- **Etiquetas de clientes:** `drop-bicapa` (anotados), `drop-bicapa-proximo` (próximo drop), `wa-<número>` (WhatsApp)
