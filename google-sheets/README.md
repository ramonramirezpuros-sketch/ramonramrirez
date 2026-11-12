# Tienda → Google Sheets

Todo va a una sola planilla, [Drop Bicapa · Leads y visitas de la landing](https://docs.google.com/spreadsheets/d/1lXG7OjKNCnRWtaQDo-a_HAGtMmFgAkSOd3DNhRTJEKE/edit),
con un solo conector ([`apps-script-landing.gs`](apps-script-landing.gs)). La alimentan:

| Qué | Cómo se distingue en la planilla |
|---|---|
| La landing `/pages/drop-bicapa` | Leads: Formulario `lista` o `proximo-drop`. Visitas: Fase `waitlist`, `live` o `closed` |
| El banner de Black Friday + Etiqueta Negra ([`shopify/black-friday/banner-anotate.liquid`](../shopify/black-friday/banner-anotate.liquid)) | Leads: Formulario `black-friday`. Visitas: Fase que empieza con `bf-`. Tiene su propia pestaña **Black Friday** |

El **Resumen** y **Por campaña** del bicapa no cuentan lo de Black Friday.

## Drop Bicapa

La landing manda todo, solo, a la planilla
[Drop Bicapa · Leads y visitas de la landing](https://docs.google.com/spreadsheets/d/1lXG7OjKNCnRWtaQDo-a_HAGtMmFgAkSOd3DNhRTJEKE/edit)
(Drive → RAMÓN RAMIREZ).

| Pestaña | Qué guarda |
|---|---|
| **Resumen** | Visitantes, reproducciones del VSL, leads parciales y completos, clics en comprar y conversión (fórmulas automáticas) |
| **Leads** | Una fila por persona. Se crea apenas escribe algo en el formulario (estado `parcial`) y pasa a `completo` cuando lo envía. Guarda nombre, email, WhatsApp, consentimiento, UTMs y de dónde vino. |
| **Visitas** | Cada visita y cada evento: `visita`, `video_play`, `video_50`, `video_completo`, `formulario_iniciado`, `formulario_enviado`, `click_comprar` |

### Activarlo (una sola vez, 5 minutos)

1. Abrí la planilla → menú **Extensiones → Apps Script**.
2. Borrá lo que haya y pegá todo el contenido de [`apps-script-landing.gs`](apps-script-landing.gs). Guardá (💾).
3. **Implementar → Nueva implementación** → tipo **Aplicación web**:
   - Ejecutar como: **Yo**
   - Quién tiene acceso: **Cualquier persona**
4. Tocá **Implementar**, autorizá los permisos con tu cuenta de Google y copiá la **URL de la aplicación web** (termina en `/exec`).
5. Shopify → Tienda online → Temas → `RR - Drop Bicapa (borrador)` → **Personalizar** → página Drop Bicapa → sección **Drop Bicapa** → campo **"Link del conector de Google Sheets"** → pegá la URL → **Guardar**.

Para probarlo, abrí la URL `/exec` en el navegador: tiene que decir "Conector Drop Bicapa activo". Después entrá a la landing, escribí un nombre y fijate que aparezca en la pestaña Leads.

Si más adelante cambiás el código del script, hacé **Implementar → Administrar implementaciones → Editar → Nueva versión**: así la URL se mantiene.

## Black Friday

[`banner-anotate.liquid`](../shopify/black-friday/banner-anotate.liquid) es el banner del equipo ("Lista de acceso
anticipado", cuenta regresiva al 27/11, 2 puros de regalo) con el formulario conectado: "Anotarme" abre una ventana
con nombre, email, WhatsApp (opcional) y el check de +18. Ya trae la URL del conector de esta planilla.

1. Shopify → Temas → **Personalizar** (el tema publicado) → Página de inicio → sección **Liquid personalizado** (Custom liquid) debajo del hero.
2. Pegá todo el bloque en el campo → **Guardar**.

Cualquier link a `#anotarme` abre el formulario (por ejemplo `ramonramirez.com.ar/#anotarme` en un anuncio o un mail).
La pestaña **Black Friday** muestra cuántos vieron el banner, cuántos tocaron "Anotarme", leads parciales y completos,
los que aceptaron comunicaciones y la lista de anotados. El gasto en Meta se carga a mano para ver el costo por anotado.
Los anotados quedan en Shopify con la etiqueta `black-friday-2026` (y `wa-<número>` si dejaron WhatsApp).

## Datos personales

- Debajo de cada formulario hay un aviso: lo que se escribe se guarda aunque no se envíe, con link a la política de privacidad (Ley 25.326 de Protección de Datos Personales). El texto se edita desde la sección.
- La columna **"Mayor de 18 y acepta comunicaciones"** dice **Sí** solo cuando la persona envió el formulario con el check. Los leads `parciales` no aceptaron recibir mensajes: por la Ley 26.687, solo se les puede mandar comunicaciones del drop a los que tienen **Sí**.
- Revisar que la política de privacidad de la tienda mencione esta planilla y el uso de los datos.
- La planilla tiene datos personales: compartirla solo con quien la necesite.
