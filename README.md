# Ramón Ramírez: proyecto Drop Bicapa Edición Especial

Base de trabajo del lanzamiento de **100 puros bicapa reposados 6 meses en ron**.
Venta durante 24 horas o hasta agotar, con lista de espera previa.

## Estado

| Pieza | Estado | Dónde |
|---|---|---|
| VSL (video final) | ✅ Terminado | Drive: `RAMÓN RAMIREZ / VIDEOS CRUDOS / TERMINADOS / TERMINADO / VSL DROP BICAPA` · [transcripción](vsl/transcripcion-vsl-final.md) |
| Landing en Shopify | ✅ Armada, sin publicar | Tema `RR - Drop Bicapa (borrador)` · página oculta `/pages/drop-bicapa` · [código y guía](shopify/README-drop-bicapa.md) |
| Producto en Shopify | 🟡 Borrador, sin precio ni stock | `bicapa-edicion-especial` |
| Fecha del drop | ✅ Domingo 18/10 00:00 hs, con cuenta regresiva. Venta sin límite de tiempo, hasta agotar stock | Editor del tema (sección "Drop Bicapa") |
| Precio | 🔴 Sin definir | Producto en Shopify |
| Funnel del drop (Miro) | 🟡 Plan completo pasado; faltan Typeform, ManyChat y pop-up | [plan y mensajes](estrategia/funnel-drop.md) |
| Leads y visitas → Google Sheets | ✅ Conectado y probado de punta a punta | [planilla](https://docs.google.com/spreadsheets/d/1lXG7OjKNCnRWtaQDo-a_HAGtMmFgAkSOd3DNhRTJEKE/edit) · [cómo activarlo](google-sheets/README.md) |
| Legal (Ley 26.687) | 🟡 Base cubierta en la landing, falta revisión | [notas legales](legal/ley-26687-tabaco.md) |

## Pendientes

- [ ] Definir **precio** y cargarlo en el producto
- [ ] Revisar la landing en el editor del tema borrador y aprobar textos
- [ ] Publicar el tema borrador (o copiar los 2 archivos al tema actual) y poner visible la página
- [ ] Sumar el mensaje sanitario al VSL y a las piezas de redes
- [ ] Confirmar con el abogado el mensaje sanitario y la verificación de edad en la entrega
- [ ] Aprobar los mensajes de email y WhatsApp por etapa (borradores en estrategia/funnel-drop.md)
- [ ] Revisar con el abogado los anuncios pagos del funnel (tabaco prohibido en Meta/Google/TikTok)
- [ ] Decidir Typeform o formulario de la landing para anotarse (una sola lista)
- [ ] Opcional: app de límite de compra (1 por persona)

## Estructura del repo

```
README.md                         ← este archivo: estado y pendientes
docs/
  Drop-Bicapa-Paso-a-paso.pdf     ← plan completo paso a paso (equipo, calendario, ManyChat, email, WhatsApp)
  paso-a-paso/                    ← fuente HTML del PDF
vsl/
  transcripcion-vsl-final.md      ← lo que dice el video final, con tiempos
  VSL_drop_bicapa_edicion_especial.md  ← guion de referencia inicial (estilo Davidoff) + teoría de VSL
shopify/
  README-drop-bicapa.md           ← qué está instalado y checklist del día del drop
  sections/drop-bicapa.liquid     ← sección de la landing (tema Dawn)
  templates/page.drop-bicapa.json ← plantilla de página
  preview/                        ← capturas de la landing
estrategia/
  funnel-drop.md                  ← etapas del tablero de Miro + mensajes por etapa
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
