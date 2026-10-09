/**
 * Conector landing Drop Bicapa → Google Sheets
 *
 * Recibe los datos que manda la landing de Shopify y los guarda en esta planilla:
 *   - Pestaña "Visitas": cada visita y cada evento (play del VSL, video completo, clic en comprar...).
 *   - Pestaña "Leads": una fila por persona y formulario. Se crea apenas escribe algo (estado "parcial")
 *     y se completa cuando envía el formulario (estado "completo").
 *
 * Instalación: ver google-sheets/README.md
 */

var HOJA_LEADS = 'Leads';
var HOJA_VISITAS = 'Visitas';
var MAX_LARGO = 300;

// Columnas de "Leads" (1 = A)
var COL = {
  alta: 1, actualizacion: 2, vid: 3, estado: 4, nombre: 5, email: 6, whatsapp: 7,
  consentimiento: 8, formulario: 9, utm_source: 10, utm_medium: 11, utm_campaign: 12,
  utm_content: 13, referrer: 14, dispositivo: 15
};
var TOTAL_COLUMNAS_LEADS = 15;

var EVENTOS_VALIDOS = ['visita', 'video_play', 'video_50', 'video_completo',
  'formulario_iniciado', 'formulario_enviado', 'click_comprar'];

function doPost(e) {
  var datos;
  try {
    datos = JSON.parse(e.postData.contents);
  } catch (err) {
    return respuesta('json invalido');
  }

  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var libro = SpreadsheetApp.getActiveSpreadsheet();
    if (datos.tipo === 'evento') {
      guardarEvento(libro.getSheetByName(HOJA_VISITAS), datos);
    } else if (datos.tipo === 'lead') {
      guardarLead(libro.getSheetByName(HOJA_LEADS), datos);
    } else {
      return respuesta('tipo desconocido');
    }
    return respuesta('ok');
  } finally {
    lock.releaseLock();
  }
}

// Permite comprobar desde el navegador que el conector está publicado.
function doGet() {
  return respuesta('Conector Drop Bicapa activo');
}

function guardarEvento(hoja, d) {
  var evento = EVENTOS_VALIDOS.indexOf(d.evento) >= 0 ? d.evento : 'otro';
  var utm = d.utm || {};
  hoja.appendRow([
    new Date(), limpiar(d.vid), evento, limpiar(d.fase),
    limpiar(utm.utm_source), limpiar(utm.utm_medium), limpiar(utm.utm_campaign), limpiar(utm.utm_content),
    limpiar(d.referrer), limpiar(d.dispositivo), limpiar(d.pagina)
  ]);
}

function guardarLead(hoja, d) {
  var vid = limpiar(d.vid);
  var formulario = limpiar(d.formulario) || 'lista';
  if (!vid) return;

  var completo = d.estado === 'completo';
  var fila = buscarFila(hoja, vid, formulario);
  var ahora = new Date();
  var utm = d.utm || {};

  if (fila === -1) {
    var nueva = [];
    for (var i = 0; i < TOTAL_COLUMNAS_LEADS; i++) nueva.push('');
    nueva[COL.alta - 1] = ahora;
    nueva[COL.actualizacion - 1] = ahora;
    nueva[COL.vid - 1] = vid;
    nueva[COL.estado - 1] = completo ? 'completo' : 'parcial';
    nueva[COL.nombre - 1] = limpiar(d.nombre);
    nueva[COL.email - 1] = limpiar(d.email);
    nueva[COL.whatsapp - 1] = limpiar(d.whatsapp);
    nueva[COL.consentimiento - 1] = completo && d.consentimiento === true ? 'Sí' : 'No';
    nueva[COL.formulario - 1] = formulario;
    nueva[COL.utm_source - 1] = limpiar(utm.utm_source);
    nueva[COL.utm_medium - 1] = limpiar(utm.utm_medium);
    nueva[COL.utm_campaign - 1] = limpiar(utm.utm_campaign);
    nueva[COL.utm_content - 1] = limpiar(utm.utm_content);
    nueva[COL.referrer - 1] = limpiar(d.referrer);
    nueva[COL.dispositivo - 1] = limpiar(d.dispositivo);
    hoja.appendRow(nueva);
    return;
  }

  var rango = hoja.getRange(fila, 1, 1, TOTAL_COLUMNAS_LEADS);
  var valores = rango.getValues()[0];
  valores[COL.actualizacion - 1] = ahora;
  // Solo pisa un dato si llega uno nuevo no vacío: borrar un campo no borra lo que ya se guardó.
  ['nombre', 'email', 'whatsapp'].forEach(function (campo) {
    var nuevo = limpiar(d[campo]);
    if (nuevo) valores[COL[campo] - 1] = nuevo;
  });
  // Un lead completo no vuelve a "parcial".
  if (completo) {
    valores[COL.estado - 1] = 'completo';
    if (d.consentimiento === true) valores[COL.consentimiento - 1] = 'Sí';
  }
  rango.setValues([valores]);
}

function buscarFila(hoja, vid, formulario) {
  var ultima = hoja.getLastRow();
  if (ultima < 2) return -1;
  var datos = hoja.getRange(2, 1, ultima - 1, TOTAL_COLUMNAS_LEADS).getValues();
  for (var i = datos.length - 1; i >= 0; i--) {
    if (String(datos[i][COL.vid - 1]) === vid && String(datos[i][COL.formulario - 1]) === formulario) {
      return i + 2;
    }
  }
  return -1;
}

// Recorta el texto y evita que algo escrito en el formulario se interprete como fórmula en la planilla.
function limpiar(valor) {
  if (valor === undefined || valor === null) return '';
  var texto = String(valor).trim().slice(0, MAX_LARGO);
  if (/^[=+\-@]/.test(texto)) texto = "'" + texto;
  return texto;
}

function respuesta(texto) {
  return ContentService.createTextOutput(texto).setMimeType(ContentService.MimeType.TEXT);
}
