# Ramón Ramírez: proyecto Drop Bicapa Edición Especial

Base de trabajo del lanzamiento de **100 puros bicapa reposados 6 meses en ron**.
Lista de espera hasta el **domingo 25/10 a las 00:00** (antes era el 18); desde ahí, venta abierta hasta agotar stock.

## Estado

| Pieza | Estado | Dónde |
|---|---|---|
| VSL (video final) | ✅ Terminado | Drive: `RAMÓN RAMIREZ / VIDEOS CRUDOS / TERMINADOS / TERMINADO / VSL DROP BICAPA` · [transcripción](vsl/transcripcion-vsl-final.md) |
| Landing en Shopify | ✅ Publicada: ramonramirez.com.ar/pages/drop-bicapa. La versión con el domingo 25 está en el tema `RR - Drop Bicapa (domingo 25)`: falta tocar **Publicar** | [código y guía](shopify/README-drop-bicapa.md) |
| Banner en la página de inicio | ✅ Publicado. La versión con el domingo 25 sale con el mismo tema `RR - Drop Bicapa (domingo 25)` | [banner-home-drop-bicapa.liquid](shopify/banner-home-drop-bicapa.liquid) |
| Producto en Shopify | 🟡 Precio cargado, todavía fuera de la tienda online. Stock en 1000: pasarlo a 100 el sáb 24 | `bicapa-edicion-especial` |
| Fecha del drop | ✅ Domingo 25/10 00:00 hs (antes 18/10), con cuenta regresiva. Venta sin límite de tiempo, hasta agotar stock | Metacampo de la tienda `drop_bicapa.start`: la landing y el banner leen la fecha de ahí |
| Precio | ✅ $28.000 | Producto en Shopify |
| Funnel del drop (Miro) | 🟡 Plan de ejecución en el PDF; falta armar ManyChat | [plan y mensajes](estrategia/funnel-drop.md) · [PDF](docs/Drop-Bicapa-Paso-a-paso.pdf) |
| Anuncios (8) | ✅ Corriendo desde el miércoles 14/10 a las 00:00. Hoy: texto de captación al 25 y fechas nuevas (captación hasta el sáb 24) | [anuncios](estrategia/anuncios-transcripciones.md) · [Meta paso a paso](docs/Meta-Ads-Paso-a-paso.pdf) |
| Leads y visitas → Google Sheets | ✅ Conectado y probado de punta a punta | [planilla](https://docs.google.com/spreadsheets/d/1lXG7OjKNCnRWtaQDo-a_HAGtMmFgAkSOd3DNhRTJEKE/edit) · [cómo activarlo](google-sheets/README.md) |
| Legal (Ley 26.687) | ✅ Resuelto por el equipo | [notas legales](legal/ley-26687-tabaco.md) |

## Pendientes

- [ ] **Hoy jue 15, cambio de fecha:** publicar el tema `RR - Drop Bicapa (domingo 25)`; en Meta, texto de captación "domingo 25" y fechas nuevas; ManyChat Mensaje 1; mail de bienvenida; M0 a las 19:00 por email y WhatsApp; historia de Ramón
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
  paso-a-paso/, meta-ads/, whatsapp/ ← fuentes HTML de los PDF
vsl/
  transcripcion-vsl-final.md      ← lo que dice el video final, con tiempos
  VSL_drop_bicapa_edicion_especial.md  ← guion de referencia inicial (estilo Davidoff) + teoría de VSL
shopify/
  README-drop-bicapa.md           ← qué está instalado y checklist del día del drop
  sections/drop-bicapa.liquid     ← sección de la landing (tema Dawn)
  banner-home-drop-bicapa.liquid  ← banner "Anotate a los bicapa" para pegar en la página de inicio
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
