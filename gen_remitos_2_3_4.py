# -*- coding: utf-8 -*-
"""Regenera los remitos 2 (Cultura Humo), 3 (Guidoli) y 4 (Munoz) - estilo original."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas

def money(v):
    if v is None:
        return "____________"
    return "$ {:,.2f}".format(v).replace(",", "X").replace(".", ",").replace("X", ".")

def generate(cfg):
    W, H = A4
    c = canvas.Canvas(cfg["out"], pagesize=A4)
    margin = 15 * mm
    box_l = margin; box_r = W - margin; box_t = H - margin; box_b = margin
    cx = W / 2
    c.setLineWidth(1); c.rect(box_l, box_b, box_r - box_l, box_t - box_b)

    # Encabezado
    c.rect(cx - 9*mm, box_t - 18*mm, 18*mm, 16*mm)
    c.setFont("Helvetica-Bold", 26); c.drawCentredString(cx, box_t - 13*mm, "X")
    c.setFont("Helvetica", 6.5); c.drawCentredString(cx, box_t - 17*mm, "DOCUMENTO NO VALIDO COMO FACTURA")
    c.setFont("Helvetica-Bold", 18); c.drawCentredString(cx, box_t - 26*mm, "REMITO / NOTA DE VENTA")
    c.setFont("Helvetica-Bold", 11); c.drawRightString(box_r - 4*mm, box_t - 8*mm, "N deg  " + cfg["numero"])
    c.setFont("Helvetica", 10); c.drawRightString(box_r - 4*mm, box_t - 14*mm, "Fecha: " + cfg["fecha"])
    c.setFont("Helvetica-Bold", 11); c.drawString(box_l + 4*mm, box_t - 8*mm, "EMISOR / VENDEDOR")
    c.setFont("Helvetica", 9)
    c.drawString(box_l + 4*mm, box_t - 13*mm, "Ramon Ramirez")
    c.drawString(box_l + 4*mm, box_t - 18*mm, "ramonramirez.com.ar")

    sep_y = box_t - 31*mm
    c.setLineWidth(0.7); c.line(box_l, sep_y, box_r, sep_y)

    cl = cfg["cliente"]
    cy = sep_y - 7*mm
    c.setFont("Helvetica-Bold", 10); c.drawString(box_l + 4*mm, cy, "CLIENTE:")
    c.setFont("Helvetica", 10); c.drawString(box_l + 26*mm, cy, cl["nombre"])
    c.setFont("Helvetica-Bold", 10); c.drawString(box_l + 4*mm, cy - 6*mm, "Domicilio:")
    c.setFont("Helvetica", 10); c.drawString(box_l + 26*mm, cy - 6*mm, cl.get("domicilio") or "______________________________")
    c.setFont("Helvetica-Bold", 10); c.drawString(box_l + 4*mm, cy - 12*mm, "CUIT/DNI:")
    c.setFont("Helvetica", 10); c.drawString(box_l + 26*mm, cy - 12*mm, cl.get("cuit") or "____________________")
    c.setFont("Helvetica-Bold", 10); c.drawString(box_l + 95*mm, cy, "Condicion:")
    c.setFont("Helvetica", 9); c.drawString(box_l + 118*mm, cy, cfg["condicion"])
    if cl.get("iva"):
        c.setFont("Helvetica-Bold", 10); c.drawString(box_l + 95*mm, cy - 6*mm, "Cond. IVA:")
        c.setFont("Helvetica", 9); c.drawString(box_l + 118*mm, cy - 6*mm, cl["iva"])
    if cl.get("email"):
        c.setFont("Helvetica-Bold", 10); c.drawString(box_l + 95*mm, cy - 12*mm, "Email:")
        c.setFont("Helvetica", 9); c.drawString(box_l + 112*mm, cy - 12*mm, cl["email"])

    sep_y2 = cy - 18*mm
    c.line(box_l, sep_y2, box_r, sep_y2)

    col_cant = box_l; col_desc = box_l + 25*mm; col_pu = box_l + 120*mm; col_imp = box_l + 150*mm
    head_y = sep_y2 - 2*mm - 7*mm
    row_h = 8.5 * mm
    c.setFillColor(colors.HexColor("#e8e8e8")); c.rect(box_l, head_y, box_r - box_l, 7*mm, fill=1, stroke=0)
    c.setFillColor(colors.black); c.setFont("Helvetica-Bold", 9)
    c.drawCentredString((col_cant + col_desc)/2, head_y + 2*mm, "CANT.")
    c.drawString(col_desc + 2*mm, head_y + 2*mm, "DESCRIPCION")
    c.drawCentredString((col_pu + col_imp)/2, head_y + 2*mm, "P. UNIT.")
    c.drawCentredString((col_imp + box_r)/2, head_y + 2*mm, "IMPORTE")

    items = cfg["items"]
    y = head_y
    total = 0.0
    n_rows = max(len(items) + 1, 12)
    for i in range(n_rows):
        y -= row_h
        c.setLineWidth(0.3); c.line(box_l, y, box_r, y)
        if i < len(items):
            qty, unit, desc, pu = items[i]
            imp = round(qty * pu, 2); total += imp
            c.setFont("Helvetica", 9.5)
            c.drawCentredString((col_cant + col_desc)/2, y + 2.4*mm, "%d %s" % (qty, unit))
            c.drawString(col_desc + 2*mm, y + 2.4*mm, desc)
            c.drawRightString(col_imp - 3*mm, y + 2.4*mm, money(pu))
            c.drawRightString(box_r - 3*mm, y + 2.4*mm, money(imp))
    c.setLineWidth(0.5)
    for xx in (col_desc, col_pu, col_imp):
        c.line(xx, head_y, xx, y)
    c.line(box_l, head_y, box_l, y); c.line(box_r, head_y, box_r, y); c.line(box_l, y, box_r, y)

    subtotal = round(total, 2)
    ajuste = cfg.get("ajuste", 0.0)
    if ajuste:
        yy = y - 7*mm
        c.setFont("Helvetica", 10)
        c.drawRightString(col_imp - 3*mm, yy, "Subtotal"); c.drawRightString(box_r - 3*mm, yy, money(subtotal))
        yy -= 6*mm
        c.drawRightString(col_imp - 3*mm, yy, cfg.get("ajuste_label", "Ajuste de redondeo")); c.drawRightString(box_r - 3*mm, yy, money(ajuste))
        ty = yy - 11*mm
    else:
        ty = y - 12*mm
    gtotal = round(subtotal + ajuste, 2)
    c.setLineWidth(1); c.rect(col_imp - 35*mm, ty, box_r - (col_imp - 35*mm), 10*mm)
    c.setFont("Helvetica-Bold", 12); c.drawString(col_imp - 33*mm, ty + 3*mm, "TOTAL")
    c.drawRightString(box_r - 3*mm, ty + 3*mm, money(gtotal))

    fy = box_b + 18*mm
    c.setLineWidth(0.5)
    c.line(box_l + 15*mm, fy, box_l + 75*mm, fy); c.line(box_r - 75*mm, fy, box_r - 15*mm, fy)
    c.setFont("Helvetica", 8)
    c.drawCentredString(box_l + 45*mm, fy - 4*mm, "Firma y aclaracion (Vendedor)")
    c.drawCentredString(box_r - 45*mm, fy - 4*mm, "Recibi conforme (Cliente)")
    c.setFont("Helvetica-Oblique", 7); c.drawCentredString(cx, box_b + 3*mm, "Original - Documento no valido como factura")
    c.showPage(); c.save()
    print(cfg["out"], "-> TOTAL", money(gtotal))

# ---------- #2 Cultura Humo ----------
generate({
    "out": "Remito_Cultura_Humo.pdf", "numero": "0001-00000002", "fecha": "08/10/2026",
    "condicion": "Contado - Precios Mayoristas",
    "cliente": {"nombre": "Barga y Perez Sofia", "domicilio": "Independencia 925 - Zarate, Bs. As.",
                "cuit": "27-38433037-7", "email": "culturahumo@gmail.com"},
    "items": [
        (25, "U", "Purito N 1 / Cigarrito I  (5 cajas x 5 U)", 1733.33),
        (25, "U", "Purito N 2 / Cigarrito II", 2123.33),
        (10, "U", "Petit Robusto  (1 caja x 10 U)", 6500.00),
        (10, "U", "Toro Ramirez  (1 caja x 10 U)", 9360.00),
        (10, "U", "Corona Ramirez  (1 caja x 10 U)", 8233.33),
        (10, "U", "Churchill Ramirez  (1 caja x 10 U)", 14300.00),
        (10, "U", "Tubos", 8800.00),
        (10, "U", "Bolsas PocketBag", 5800.00),
    ],
})

# ---------- #3 Guidoli ----------
generate({
    "out": "Remito_Fernando_Guidoli.pdf", "numero": "0001-00000003", "fecha": "08/10/2026",
    "condicion": "Contado - Precios Mayoristas",
    "cliente": {"nombre": "Fernando Guidoli", "domicilio": "", "cuit": ""},
    "items": [
        (15, "U", "Petit Purito", 4160.00),
        (25, "U", "Petit Robusto", 6500.00),
        (24, "U", "Toro Ramirez", 9360.00),
        (15, "U", "1/2 Corona Ramirez", 7366.6667),
        (15, "U", "Churchill Ramirez", 14300.00),
        ( 5, "U", "Guillotina", 16499.00),
        ( 1, "U", "Zippo + Inserto", 143000.00),
    ],
    "ajuste": -35.00, "ajuste_label": "Ajuste de redondeo",
})

# ---------- #4 Munoz ----------
generate({
    "out": "Remito_Pedido_0004.pdf", "numero": "0001-00000004", "fecha": "09/10/2026",
    "condicion": "Contado - Precios Mayoristas",
    "cliente": {"nombre": "Munoz Mauro Oscar", "domicilio": "Tucuman 13 - General Pacheco (1617), Buenos Aires",
                "cuit": "20-32216831-5", "iva": "Responsable Inscripto"},
    "items": [
        (10, "U",   "Bolsas PocketBag", 5800.00),
        (10, "U",   "Tubos", 8800.00),
        (25, "U",   "Cigarrito I  (5 box x 5 U)", 1733.33),
        (20, "U",   "Cigarrito II", 2123.33),
        (20, "U",   "Long Cigarrito", 2426.67),
        ( 3, "box", "Pocket Box Petit Robusto (x3 U)", 19933.33),
        (10, "U",   "Petit Corona  (1 caja x 10 U)", 7713.33),
        (10, "U",   "Churchill Ramirez  (1 caja x 10 U)", 14300.00),
        (10, "U",   "Toro Ramirez  (1 caja x 10 U)", 9360.00),
        (10, "U",   "Corona Ramirez  (1 caja x 10 U)", 8233.33),
        ( 5, "U",   "Petit Robusto E.M.A", 9750.00),
    ],
})
