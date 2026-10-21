# Anotados → público de Meta (automático)

Cada persona que se anota en la landing queda **excluida de los anuncios para anotarse** y pasa a ver solo los
de **calentamiento ("hammer them")**. Lo hace solo el Apps Script de la
[planilla de leads](https://docs.google.com/spreadsheets/d/1lXG7OjKNCnRWtaQDo-a_HAGtMmFgAkSOd3DNhRTJEKE/edit),
con [`meta-publicos.gs`](meta-publicos.gs):

| Cada | Qué hace |
|---|---|
| **5 minutos** | Sube a Meta los anotados nuevos de la pestaña **Leads** (estado `completo` y consentimiento **Sí**) al público **DROP Anotados (planilla)**. Email, WhatsApp y nombre viajan cifrados. La columna **P · Subido a Meta** marca cuándo se subió cada uno. |
| **1 hora** | Revisa los conjuntos de las campañas que empiezan con **DROP** y que siguen vigentes. Los de *Calentamiento*, *Calientes* y *Quedan 10* **incluyen** a los anotados. Todos los demás (*Captación*, *Follow me*, *Domingo · Amplio*) los **excluyen**. Si un conjunto ya está bien, no lo toca. También configura sola la campaña del domingo cuando se cree. |

El público "Anotados web" del píxel sigue como está. Los dos se complementan: el píxel actúa enseguida, pero pierde
a quien tiene bloqueadores o se anotó desde otro celular. La lista suma a esas personas, aunque Meta tarda
de unos minutos a unas horas en procesarla. **Reemplaza el CSV "Anotados lista"** que se iba a subir a mano
el miércoles 21 y el sábado 24.

## Instalarlo (una sola vez, 15 minutos)

### 1. Token de Meta (Facebook for Developers + configuración del negocio)

1. Entrá a [developers.facebook.com/apps](https://developers.facebook.com/apps) con el Facebook que administra el negocio de Ramón Ramírez → **Crear app**.
   - Nombre: `Planilla Drop` · caso de uso: **Crear y administrar anuncios con la API de marketing** (*Create & manage ads with Marketing API*) · portfolio comercial: el de **Ramón Ramírez** → **Crear app**.
2. Andá a [business.facebook.com/settings](https://business.facebook.com/settings) → **Usuarios → Usuarios del sistema → Agregar**.
   - Nombre: `Planilla Drop` · rol: **Administrador**.
3. Con ese usuario elegido → **Asignar activos**:
   - **Cuentas publicitarias** → la de la marca → **Control total** (administrar la cuenta publicitaria).
   - **Apps** → `Planilla Drop` → **Control total** (desarrollar la app).
4. **Generar token** → app `Planilla Drop` → caducidad **Nunca** → permisos **ads_management** y **ads_read** → **Generar**.
   **Copialo ya**: Meta lo muestra una sola vez. No lo mandes por chat ni por mail; va directo al paso 3.
5. Anotá el **número de la cuenta publicitaria**. Está en el Administrador de anuncios, en la dirección (`act=123456789…`) o en ⚙️ Configuración.
6. Aceptá las condiciones de públicos personalizados (si ya creaste alguna vez un público con lista de clientes, ya están aceptadas):
   `https://business.facebook.com/ads/manage/customaudiences/tos/?act=NÚMERO_DE_CUENTA`

### 2. Pegar el código

1. Planilla → **Extensiones → Apps Script** (el mismo proyecto del conector de la landing).
2. A la izquierda, **＋ → Script** → nombre `meta-publicos` → borrá lo que trae y pegá todo [`meta-publicos.gs`](meta-publicos.gs) → 💾.
   No hace falta volver a implementar la aplicación web: la landing sigue igual.

### 3. Guardar el token en el script

**⚙️ Configuración del proyecto → Propiedades del script → Agregar propiedad**:

| Propiedad | Valor |
|---|---|
| `META_TOKEN` | el token del paso 1.4 |
| `META_CUENTA` | el número de la cuenta publicitaria (con o sin `act_`) |

→ **Guardar propiedades del script**. El token queda guardado en el script, no en la planilla. Solo lo ve quien puede editar el Apps Script.

### 4. Probar y prender

1. Arriba, en la lista de funciones, elegí **`verCuenta`** → **Ejecutar** → autorizá los permisos con tu cuenta de Google.
   Solo mira, no cambia nada. En el registro tiene que aparecer el nombre de la cuenta y cada conjunto DROP con lo que va a hacer:
   `→ DROP Captación › … : va a excluir a los anotados`.
2. Si está bien, elegí **`configurarTodo`** → **Ejecutar**. Crea el público, sube a los que ya se anotaron, ajusta los conjuntos y deja corriendo las dos tareas automáticas.
3. Controlá en Meta:
   - **Públicos** → aparece **DROP Anotados (planilla)** (al principio dice "Procesando" o "Muy pequeño": es normal, se llena en unas horas).
   - **DROP Captación** → conjunto → **Público** → *Excluir* → figura **DROP Anotados (planilla)** junto a "Anotados web".
   - **DROP Calentamiento** → conjunto → **Público** → figura en los públicos incluidos.

## Qué tener en cuenta

- **Aprendizaje de Meta:** cambiar el público de un conjunto que está corriendo reinicia la fase de aprendizaje. Pasa una sola vez por conjunto, cuando se agrega el público.
- **Qué marcas significan** en el registro (Apps Script → **Ejecuciones**): ✔ ya estaba bien · ✚ lo cambió · ⚠ no lo tocó y explica por qué · ✖ Meta no aceptó el cambio. Si una tarea falla, Google te avisa por mail.
- **No toca** conjuntos amplios de calentamiento: si uno de calentamiento no apunta a ningún público personalizado, lo deja como está y avisa con ⚠. Tampoco toca campañas que no empiecen con "DROP".
- **Solo suben los que dieron el consentimiento** (columna H en **Sí**). Los `parciales` siguen viendo los anuncios para anotarse, que es lo que se busca.
- **Anotados por otros caminos** (ManyChat, WhatsApp directo) no están en la planilla, así que no se excluyen. Si se suman ahí, entran solos.
- **Política de privacidad:** sumar que los datos de contacto se comparten cifrados con Meta para no mostrarle anuncios repetidos a quien ya se anotó (Ley 25.326).
- **Cuando termine el drop:** ejecutá **`desinstalarAutomatizacion`** para apagar las tareas automáticas. Para cortar el acceso del todo, en el usuario del sistema → **Revocar tokens**.
- **Si cambian los nombres de las campañas:** la regla usa "DROP" al principio del nombre de la campaña y las palabras *calentamiento*, *calientes* o *quedan 10* para incluir. Se cambia arriba de todo en `meta-publicos.gs`.
