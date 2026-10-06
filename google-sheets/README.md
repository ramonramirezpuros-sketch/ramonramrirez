# Landing → Google Sheets

La landing manda todo, solo, a la planilla
[Drop Bicapa · Leads y visitas de la landing](https://docs.google.com/spreadsheets/d/1lXG7OjKNCnRWtaQDo-a_HAGtMmFgAkSOd3DNhRTJEKE/edit)
(Drive → RAMÓN RAMIREZ).

| Pestaña | Qué guarda |
|---|---|
| **Resumen** | Visitantes, reproducciones del VSL, leads parciales y completos, clics en comprar y conversión (fórmulas automáticas) |
| **Leads** | Una fila por persona. Se crea apenas escribe algo en el formulario (estado `parcial`) y pasa a `completo` cuando lo envía. Guarda nombre, email, WhatsApp, consentimiento, UTMs y de dónde vino. |
| **Visitas** | Cada visita y cada evento: `visita`, `video_play`, `video_50`, `video_completo`, `formulario_iniciado`, `formulario_enviado`, `click_comprar` |

## Activarlo (una sola vez, 5 minutos)

1. Abrí la planilla → menú **Extensiones → Apps Script**.
2. Borrá lo que haya y pegá todo el contenido de [`apps-script-landing.gs`](apps-script-landing.gs). Guardá (💾).
3. **Implementar → Nueva implementación** → tipo **Aplicación web**:
   - Ejecutar como: **Yo**
   - Quién tiene acceso: **Cualquier persona**
4. Tocá **Implementar**, autorizá los permisos con tu cuenta de Google y copiá la **URL de la aplicación web** (termina en `/exec`).
5. Shopify → Tienda online → Temas → `RR - Drop Bicapa (borrador)` → **Personalizar** → página Drop Bicapa → sección **Drop Bicapa** → campo **"Link del conector de Google Sheets"** → pegá la URL → **Guardar**.

Para probarlo, abrí la URL `/exec` en el navegador: tiene que decir "Conector Drop Bicapa activo". Después entrá a la landing, escribí un nombre y fijate que aparezca en la pestaña Leads.

Si más adelante cambiás el código del script, hacé **Implementar → Administrar implementaciones → Editar → Nueva versión**: así la URL se mantiene.

## Datos personales

- Debajo de cada formulario hay un aviso: lo que se escribe se guarda aunque no se envíe, con link a la política de privacidad (Ley 25.326 de Protección de Datos Personales). El texto se edita desde la sección.
- La columna **"Mayor de 18 y acepta comunicaciones"** dice **Sí** solo cuando la persona envió el formulario con el check. Los leads `parciales` no aceptaron recibir mensajes: por la Ley 26.687, solo se les puede mandar comunicaciones del drop a los que tienen **Sí**.
- Revisar que la política de privacidad de la tienda mencione esta planilla y el uso de los datos.
- La planilla tiene datos personales: compartirla solo con quien la necesite.
