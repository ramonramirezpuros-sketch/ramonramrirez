/**
 * Anotados del drop → público personalizado de Meta
 *
 * Mantiene al día el público "DROP Anotados (planilla)" de la cuenta publicitaria:
 *   - Cada 5 minutos sube los leads nuevos de la pestaña "Leads" que están "completo" y con "Sí" en el
 *     consentimiento. A Meta le llegan el email, el WhatsApp y el nombre cifrados (SHA-256), nunca en texto.
 *     La columna P ("Subido a Meta") dice cuándo se subió cada uno.
 *   - Cada hora revisa los conjuntos de anuncios de las campañas "DROP": los de calentamiento ("hammer them")
 *     y los "Calientes" / "Quedan 10" del domingo incluyen a los anotados; todos los demás los excluyen, así
 *     el que ya se anotó no vuelve a ver el anuncio para anotarse.
 *
 * Va en el mismo proyecto de Apps Script que apps-script-landing.gs: usa HOJA_LEADS y COL de ese archivo.
 * Instalación: ver google-sheets/README-meta.md
 */

var META_API = 'https://graph.facebook.com/v26.0/';
var META_NOMBRE_PUBLICO = 'DROP Anotados (planilla)';
var META_PREFIJO_CAMPANAS = 'drop';
// Conjuntos que les hablan a los anotados. Se busca en "campaña + conjunto", sin mayúsculas ni tildes.
var META_INCLUYEN_ANOTADOS = ['calentamiento', 'calientes', 'quedan 10'];
var META_COL_SUBIDO = 16; // P: la landing escribe hasta la O
var META_LOTE = 10000;    // máximo de personas por envío que acepta Meta
var META_TAREAS = ['sincronizarAnotados', 'aplicarEnCampanas'];

// ---------- Para correr a mano desde el editor ----------

// Solo mira: muestra la cuenta, el público y qué haría en cada conjunto. No cambia nada.
function verCuenta() {
  metaLogCuenta();
  var publico = PropertiesService.getScriptProperties().getProperty('META_PUBLICO');
  if (publico) {
    var p = metaLlamar('get', publico + '?fields=name,approximate_count_lower_bound,approximate_count_upper_bound,delivery_status');
    Logger.log('Público "%s" (%s): entre %s y %s personas · %s', p.name, publico,
      p.approximate_count_lower_bound, p.approximate_count_upper_bound, (p.delivery_status || {}).description || '');
  } else {
    Logger.log('Público "%s": todavía no existe, lo crea configurarTodo.', META_NOMBRE_PUBLICO);
  }
  metaRevisarConjuntos(false);
}

// Una sola vez: crea el público, sube a los anotados, ajusta las campañas y deja todo andando solo.
function configurarTodo() {
  metaLogCuenta();
  Logger.log('Público "%s": %s', META_NOMBRE_PUBLICO, metaPublico());
  sincronizarAnotados();
  aplicarEnCampanas();
  instalarAutomatizacion();
  Logger.log('Listo. Cada 5 minutos se suben los anotados nuevos y cada hora se revisan las campañas DROP.');
}

function instalarAutomatizacion() {
  desinstalarAutomatizacion();
  ScriptApp.newTrigger('sincronizarAnotados').timeBased().everyMinutes(5).create();
  ScriptApp.newTrigger('aplicarEnCampanas').timeBased().everyHours(1).create();
}

// Para apagarlo cuando termine el drop.
function desinstalarAutomatizacion() {
  ScriptApp.getProjectTriggers().forEach(function (t) {
    if (META_TAREAS.indexOf(t.getHandlerFunction()) >= 0) ScriptApp.deleteTrigger(t);
  });
}

// ---------- Tareas automáticas ----------

function sincronizarAnotados() {
  var hoja = SpreadsheetApp.getActiveSpreadsheet().getSheetByName(HOJA_LEADS);
  var lock = LockService.getScriptLock();
  if (!lock.tryLock(30000)) return; // la landing está escribiendo: se reintenta en la próxima vuelta

  // Lee con el candado puesto, pero lo suelta antes de hablar con Meta para no demorar a la landing.
  var inicio = new Date();
  var ultima = hoja.getLastRow();
  var pendientes = [];
  try {
    if (ultima < 2) return;
    hoja.getRange(2, 1, ultima - 1, META_COL_SUBIDO).getValues().forEach(function (f, i) {
      if (f[COL.estado - 1] !== 'completo' || f[COL.consentimiento - 1] !== 'Sí') return;
      // Ya subido y sin cambios desde entonces.
      var subido = f[META_COL_SUBIDO - 1];
      if (subido instanceof Date && f[COL.actualizacion - 1] <= subido) return;
      var persona = metaPersona(f);
      if (persona) pendientes.push({ fila: i + 2, vid: String(f[COL.vid - 1]), persona: persona });
    });
  } finally {
    lock.releaseLock();
  }

  if (!pendientes.length) {
    Logger.log('Sin anotados nuevos para subir.');
    return;
  }
  var r = metaSubir(metaPublico(), pendientes.map(function (p) { return p.persona; }));
  Logger.log('Subidos a Meta: %s anotados (Meta recibió %s, %s con datos inválidos).', pendientes.length, r.recibidos, r.invalidos);

  // Marca la hora de lectura: si el lead cambió mientras tanto, la próxima vuelta lo vuelve a subir.
  // Solo marca las filas que siguen en su lugar, por si alguien borró filas en el medio.
  lock.waitLock(30000);
  try {
    if (!hoja.getRange(1, META_COL_SUBIDO).getValue()) hoja.getRange(1, META_COL_SUBIDO).setValue('Subido a Meta');
    var vids = hoja.getRange(2, COL.vid, ultima - 1, 1).getValues();
    var columna = hoja.getRange(2, META_COL_SUBIDO, ultima - 1, 1);
    var marcas = columna.getValues();
    pendientes.forEach(function (p) {
      if (String(vids[p.fila - 2][0]) === p.vid) marcas[p.fila - 2][0] = inicio;
    });
    columna.setValues(marcas);
  } finally {
    lock.releaseLock();
  }
}

function aplicarEnCampanas() {
  metaRevisarConjuntos(true);
}

// ---------- Público ----------

function metaPublico() {
  var props = PropertiesService.getScriptProperties();
  var id = props.getProperty('META_PUBLICO');
  if (id) return id;

  var existente = metaListar(metaCuenta() + '/customaudiences?fields=id,name&limit=25').filter(function (p) {
    return p.name === META_NOMBRE_PUBLICO;
  })[0];
  id = existente ? existente.id : metaLlamar('post', metaCuenta() + '/customaudiences', {
    name: META_NOMBRE_PUBLICO,
    subtype: 'CUSTOM',
    customer_file_source: 'USER_PROVIDED_ONLY',
    description: 'Anotados al drop (completos y con consentimiento) de la planilla de leads. Se actualiza solo desde Apps Script.'
  }).id;
  props.setProperty('META_PUBLICO', id);
  return id;
}

function metaSubir(publico, personas) {
  var sesion = Math.floor(Math.random() * 9e15) + 1;
  var resultado = { recibidos: 0, invalidos: 0 };
  for (var i = 0, lote = 1; i < personas.length; i += META_LOTE, lote++) {
    var r = metaLlamar('post', publico + '/users', {
      session: JSON.stringify({
        session_id: sesion, batch_seq: lote, last_batch_flag: i + META_LOTE >= personas.length,
        estimated_num_total: personas.length
      }),
      payload: JSON.stringify({ schema: ['EMAIL', 'PHONE', 'FN', 'LN'], data: personas.slice(i, i + META_LOTE) })
    });
    resultado.recibidos += r.num_received || 0;
    resultado.invalidos += r.num_invalid_entries || 0;
  }
  return resultado;
}

// Una fila de "Leads" → [email, teléfono, nombre, apellido], normalizados como pide Meta y cifrados.
function metaPersona(f) {
  var email = String(f[COL.email - 1]).trim().toLowerCase();
  if (email.indexOf('@') < 0) email = '';
  var telefono = metaTelefono(f[COL.whatsapp - 1]);
  if (!email && !telefono) return null;
  var nombres = metaMinusculas(f[COL.nombre - 1]).replace(/[^a-z\s]/g, '').trim().split(/\s+/);
  var apellido = nombres.length > 1 ? nombres[nombres.length - 1] : '';
  return [email, telefono, nombres[0], apellido].map(metaHash);
}

// Meta pide el número con código de país y solo dígitos. Los de Argentina van como celular:
// 549 + área + número (10 dígitos), venga como venga: "11 2345 6789", "011 15 2345 6789", "54 11...", "549 11...".
// Los de otros países ya llegan con su código desde la landing y se dejan como están.
function metaTelefono(valor) {
  var d = String(valor).replace(/\D/g, '').replace(/^00/, '');
  var n = d;
  if (/^54/.test(n) && n.length >= 12) n = n.slice(2).replace(/^9/, '');
  n = n.replace(/^0/, '');
  if (n.length === 12) {
    for (var k = 2; k <= 4; k++) {
      if (n.substr(k, 2) === '15') { n = n.slice(0, k) + n.slice(k + 2); break; }
    }
  }
  if (/^[1-3]\d{9}$/.test(n)) return '549' + n;
  return d.length >= 8 ? d : '';
}

// Minúsculas y sin tildes: "Captación" → "captacion", "Ramírez" → "ramirez".
function metaMinusculas(valor) {
  return String(valor || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
}

function metaHash(texto) {
  if (!texto) return '';
  return Utilities.computeDigest(Utilities.DigestAlgorithm.SHA_256, texto, Utilities.Charset.UTF_8)
    .map(function (b) { return ('0' + (b & 255).toString(16)).slice(-2); })
    .join('');
}

// ---------- Campañas ----------

// Recorre los conjuntos vigentes de las campañas DROP. Con aplicar = false solo cuenta lo que haría.
function metaRevisarConjuntos(aplicar) {
  var publico = aplicar ? metaPublico() : PropertiesService.getScriptProperties().getProperty('META_PUBLICO');
  var errores = [];

  metaConjuntosDrop().forEach(function (c) {
    var t = c.targeting || {};
    var incluidos = metaIds(t.custom_audiences);
    var excluidos = metaIds(t.excluded_custom_audiences);
    var regla = metaRegla(c);
    var nombre = c.campaign.name + ' › ' + c.name + ' [' + c.effective_status + ']';
    var nota = regla === 'incluir' && t.targeting_automation && t.targeting_automation.advantage_audience === 1
      ? ' · ojo: tiene Público Advantage+, Meta puede mostrarlo también a gente fuera de los públicos' : '';

    if ((regla === 'incluir' ? incluidos : excluidos).indexOf(publico) >= 0) {
      Logger.log('✔ %s: ya %s a los anotados%s', nombre, regla === 'incluir' ? 'incluye' : 'excluye', nota);
      return;
    }
    // No convierte un conjunto amplio en uno solo para anotados: eso lo decide una persona.
    if (regla === 'incluir' && !incluidos.length) {
      Logger.log('⚠ %s: es de calentamiento pero no apunta a públicos personalizados. No lo toco.', nombre);
      return;
    }
    if (regla === 'excluir' && incluidos.indexOf(publico) >= 0) {
      Logger.log('⚠ %s: incluye a los anotados y debería excluirlos. No lo toco: revisalo a mano.', nombre);
      return;
    }
    if (!aplicar) {
      Logger.log('→ %s: va a %s a los anotados%s', nombre, regla, nota);
      return;
    }

    var campo = regla === 'incluir' ? 'custom_audiences' : 'excluded_custom_audiences';
    t.custom_audiences = incluidos.map(function (id) { return { id: id }; });
    t.excluded_custom_audiences = excluidos.map(function (id) { return { id: id }; });
    t[campo].push({ id: publico });
    if (!t.custom_audiences.length) delete t.custom_audiences;
    if (!t.excluded_custom_audiences.length) delete t.excluded_custom_audiences;
    try {
      metaLlamar('post', c.id, { targeting: JSON.stringify(t) });
      Logger.log('✚ %s: ahora %s a los anotados%s', nombre, regla === 'incluir' ? 'incluye' : 'excluye', nota);
    } catch (err) {
      errores.push(nombre + ': ' + err.message);
      Logger.log('✖ %s: %s', nombre, err.message);
    }
  });

  // Que la tarea figure como fallida (y Google mande el aviso por mail) si algún conjunto no se pudo cambiar.
  if (errores.length) throw new Error('No se pudieron actualizar ' + errores.length + ' conjuntos:\n' + errores.join('\n'));
}

function metaConjuntosDrop() {
  var ahora = new Date();
  // %7Bname%7D es {name}: UrlFetchApp no acepta llaves sin codificar en la dirección.
  return metaListar(metaCuenta() + '/adsets?fields=id,name,effective_status,end_time,campaign%7Bname%7D,targeting&limit=25')
    .filter(function (c) {
      return metaMinusculas(c.campaign && c.campaign.name).indexOf(META_PREFIJO_CAMPANAS) === 0
        && ['DELETED', 'ARCHIVED'].indexOf(c.effective_status) < 0
        && !(c.end_time && metaFecha(c.end_time) < ahora);
    });
}

function metaRegla(conjunto) {
  var nombre = metaMinusculas(conjunto.campaign.name + ' ' + conjunto.name);
  return META_INCLUYEN_ANOTADOS.some(function (p) { return nombre.indexOf(p) >= 0; }) ? 'incluir' : 'excluir';
}

function metaIds(publicos) {
  return (publicos || []).map(function (p) { return String(p.id); });
}

// Meta manda las fechas como "2026-10-24T23:30:00-0300".
function metaFecha(texto) {
  return new Date(String(texto).replace(/([+-]\d{2})(\d{2})$/, '$1:$2'));
}

// ---------- Conexión ----------

function metaLogCuenta() {
  var c = metaLlamar('get', metaCuenta() + '?fields=name,currency,timezone_name');
  Logger.log('Cuenta publicitaria: %s (%s) · %s · %s', c.name, metaCuenta(), c.currency, c.timezone_name);
}

function metaCuenta() {
  return 'act_' + metaPropiedad('META_CUENTA').replace(/^act_/, '');
}

function metaPropiedad(clave) {
  var valor = PropertiesService.getScriptProperties().getProperty(clave);
  if (!valor) throw new Error('Falta la propiedad del script ' + clave + ' (ver google-sheets/README-meta.md).');
  return valor.trim();
}

function metaLlamar(metodo, ruta, datos) {
  var opciones = {
    method: metodo,
    headers: { Authorization: 'Bearer ' + metaPropiedad('META_TOKEN') },
    muteHttpExceptions: true
  };
  if (datos) opciones.payload = datos;
  var texto = UrlFetchApp.fetch(/^https:/.test(ruta) ? ruta : META_API + ruta, opciones).getContentText();
  var cuerpo;
  try {
    cuerpo = JSON.parse(texto);
  } catch (err) {
    throw new Error('Meta respondió algo inesperado: ' + texto.slice(0, 200));
  }
  if (cuerpo.error) {
    var e = cuerpo.error;
    throw new Error('Meta: ' + (e.error_user_msg || e.message) + ' (código ' + e.code + (e.error_subcode ? '/' + e.error_subcode : '') + ')');
  }
  return cuerpo;
}

// Trae todas las páginas de un listado.
function metaListar(ruta) {
  var items = [];
  while (ruta) {
    var pagina = metaLlamar('get', ruta);
    items = items.concat(pagina.data || []);
    ruta = pagina.paging && pagina.paging.next;
  }
  return items;
}
