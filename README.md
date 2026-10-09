# Ramón Ramírez: proyecto Drop Bicapa Edición Especial

Base de trabajo del lanzamiento de **100 puros bicapa reposados 6 meses en ron**.
Lista de espera hasta el domingo 18/10 a las 00:00; desde ahí, venta abierta hasta agotar stock.

## Estado

| Pieza | Estado | Dónde |
|---|---|---|
| VSL (video final) | ✅ Terminado | Drive: `RAMÓN RAMIREZ / VIDEOS CRUDOS / TERMINADOS / TERMINADO / VSL DROP BICAPA` · [transcripción](vsl/transcripcion-vsl-final.md) |
| Landing en Shopify | ✅ Armada, sin publicar | Tema `RR - Drop Bicapa (borrador)` · página oculta `/pages/drop-bicapa` · [código y guía](shopify/README-drop-bicapa.md) |
| Producto en Shopify | 🟡 Precio cargado, todavía fuera de la tienda online. Stock en 1000: pasarlo a 100 el sáb 17 | `bicapa-edicion-especial` |
| Fecha del drop | ✅ Domingo 18/10 00:00 hs, con cuenta regresiva. Venta sin límite de tiempo, hasta agotar stock | Editor del tema (sección "Drop Bicapa") |
| Precio | ✅ $28.000 | Producto en Shopify |
| Funnel del drop (Miro) | 🟡 Plan de ejecución en el PDF; falta armar ManyChat | [plan y mensajes](estrategia/funnel-drop.md) · [PDF](docs/Drop-Bicapa-Paso-a-paso.pdf) |
| Anuncios (8) | ✅ Transcriptos y con fecha: arrancan el lunes 12/10 | [anuncios](estrategia/anuncios-transcripciones.md) · PDF pág. 3 |
| Leads y visitas → Google Sheets | ✅ Conectado y probado de punta a punta | [planilla](https://docs.google.com/spreadsheets/d/1lXG7OjKNCnRWtaQDo-a_HAGtMmFgAkSOd3DNhRTJEKE/edit) · [cómo activarlo](google-sheets/README.md) |
| Legal (Ley 26.687) | ✅ Resuelto por el equipo | [notas legales](legal/ley-26687-tabaco.md) |

## Pendientes

- [ ] **Antes del lunes 12:** publicar el tema borrador y poner visible la página (los anuncios arrancan ese día)
- [ ] Nombres de los responsables de ManyChat, Email y WhatsApp
- [ ] Crear los estáticos "YA ESTÁN DISPONIBLES" y "SOLAMENTE QUEDAN 10" (subirlos el sáb 17 antes de las 12)
- [ ] Sáb 17, 22:00: producto activo en la tienda online con stock 100
- [ ] Borrar de la planilla las filas de prueba
- [ ] Opcional: pop-up de escasez en la tienda
- [ ] Opcional: app de límite de compra (1 por persona)

## Estructura del repo

```
README.md                         ← este archivo: estado y pendientes
docs/
  Drop-Bicapa-Paso-a-paso.pdf     ← plan de ejecución: cronograma, historias de Ramón, ManyChat, email y WhatsApp
  Meta-Ads-Paso-a-paso.pdf        ← guía clic por clic para subir y controlar los anuncios en Meta
  paso-a-paso/, meta-ads/         ← fuentes HTML de los PDF
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
