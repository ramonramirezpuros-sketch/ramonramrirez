# -*- coding: utf-8 -*-
"""Presupuesto / Nota de Venta membretado - Tabaqueria 430 San Pedro - objetivo $1.300.000."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas

EMISOR = {"nombre": "RAMON RAMIREZ", "tagline": "Cigarros Artesanales", "web": "www.ramonramirez.com.ar"}
NAVY = colors.HexColor("#14264f")
GOLD = colors.HexColor("#c8a24a")

CLIENTE = {"nombre": "Tabaqueria 430 - San Pedro", "cuit": "", "iva": "", "domicilio": ""}

NUMERO = "PRES-0001-00000013"
FECHA = "28/10/2026"
VALIDEZ = "10 dias"
CONDICION = "Precios Mayoristas"

# (cantidad, unidad, descripcion, precio_unitario)
ITEMS = [
    (12, "U", "Cigarrito I",                 1733.33),
    (19, "U", "Petit Purito",                4160.00),
    (12, "U", "Mini Short Robusto",          5200.00),
    (15, "U", "Petit Robusto",               6500.00),
    (23, "U", "Super Robusto",              10313.33),
    (14, "U", "Toro Ramirez",                9360.00),
    (10, "U", "Petit Corona",                7713.33),
    (25, "U", "1/2 Corona Ramirez",          7366.67),
    (14, "U", "Corona Ramirez",              8233.33),
    ( 5, "U", "Petit Robusto Oro",          13000.00),
    ( 4, "U", "Don Ramon Oro",              28600.00),
    (20, "U", "Bolsas Humidoras PocketBag",  5800.00),
]
AJUSTE_LABEL = "Ajuste de redondeo"
TARGET = None  # sin redondeo: total = suma real

OUT = "Presupuesto_Tabaqueria_430.pdf"
# -----------------------------------------------------

W, H = A4
c = canvas.Canvas(OUT, pagesize=A4)

def money(v):
    return "$ {:,.2f}".format(v).replace(",", "X").replace(".", ",").replace("X", ".")

margin = 12 * mm
box_l = margin; box_r = W - margin

# ---------- MEMBRETE ----------
band_h = 24 * mm
band_top = H - margin
c.setFillColor(NAVY)
c.rect(box_l, band_top - band_h, box_r - box_l, band_h, fill=1, stroke=0)
c.setFillColor(GOLD)
c.rect(box_l, band_top - band_h - 1.4*mm, box_r - box_l, 1.4*mm, fill=1, stroke=0)
c.setFillColor(GOLD)
c.setFont("Helvetica-Bold", 24)
c.drawString(box_l + 6*mm, band_top - 11*mm, EMISOR["nombre"])
c.setFillColor(colors.white)
c.setFont("Helvetica-Oblique", 9.5)
c.drawString(box_l + 6*mm, band_top - 16.5*mm, EMISOR["tagline"])
c.setFont("Helvetica", 8.5)
c.drawString(box_l + 6*mm, band_top - 21*mm, EMISOR["web"])
c.setFillColor(colors.white)
c.setFont("Helvetica-Bold", 17)
c.drawRightString(box_r - 6*mm, band_top - 10*mm, "PRESUPUESTO")
c.setFont("Helvetica", 8.5)
c.drawRightString(box_r - 6*mm, band_top - 15.5*mm, "N " + NUMERO)
c.drawRightString(box_r - 6*mm, band_top - 20*mm, "Fecha: " + FECHA)
c.setFillColor(colors.black)

# ---------- CLIENTE ----------
cy = band_top - band_h - 8*mm
c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 9.5)
c.drawString(box_l, cy, "CLIENTE")
c.setFillColor(colors.black); c.setFont("Helvetica", 9.5)
c.drawString(box_l, cy - 5.5*mm,  "Nombre:     " + (CLIENTE["nombre"] or "____________________"))
c.drawString(box_l, cy - 10.5*mm, "CUIT:       " + (CLIENTE["cuit"] or "____________________"))
c.drawString(box_l, cy - 15.5*mm, "Domicilio:  " + (CLIENTE["domicilio"] or "______________________________"))
c.drawRightString(box_r, cy - 5.5*mm,  "Validez: " + VALIDEZ)
c.drawRightString(box_r, cy - 10.5*mm, CONDICION)

# ---------- TABLA ----------
col_cant = box_l; col_desc = box_l + 22*mm; col_pu = box_l + 122*mm; col_imp = box_l + 152*mm
head_y = cy - 22*mm
row_h = 6.2 * mm

c.setFillColor(NAVY)
c.rect(box_l, head_y, box_r - box_l, 6.2*mm, fill=1, stroke=0)
c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 8.5)
c.drawCentredString((col_cant + col_desc)/2, head_y + 1.8*mm, "CANT.")
c.drawString(col_desc + 2*mm, head_y + 1.8*mm, "DESCRIPCION")
c.drawCentredString((col_pu + col_imp)/2, head_y + 1.8*mm, "P. UNIT.")
c.drawCentredString((col_imp + box_r)/2, head_y + 1.8*mm, "IMPORTE")
c.setFillColor(colors.black)

y = head_y
subtotal = 0.0
for i, (qty, unit, desc, pu) in enumerate(ITEMS):
    y -= row_h
    if i % 2 == 0:
        c.setFillColor(colors.HexColor("#f2f3f7"))
        c.rect(box_l, y, box_r - box_l, row_h, fill=1, stroke=0)
        c.setFillColor(colors.black)
    c.setLineWidth(0.3); c.setStrokeColor(colors.HexColor("#d0d0d0"))
    c.line(box_l, y, box_r, y)
    c.setStrokeColor(colors.black)
    imp = round(qty * pu, 2); subtotal += imp
    c.setFont("Helvetica", 8.7)
    c.drawCentredString((col_cant + col_desc)/2, y + 1.9*mm, "%d %s" % (qty, unit))
    c.drawString(col_desc + 2*mm, y + 1.9*mm, desc)
    c.drawRightString(col_imp - 3*mm, y + 1.9*mm, money(pu))
    c.drawRightString(box_r - 3*mm, y + 1.9*mm, money(imp))

c.setLineWidth(0.6); c.setStrokeColor(NAVY)
c.rect(box_l, y, box_r - box_l, head_y + 6.2*mm - y, fill=0, stroke=1)
for xx in (col_desc, col_pu, col_imp):
    c.line(xx, head_y, xx, y)
c.setStrokeColor(colors.black)

# ---------- SUBTOTAL / AJUSTE / TOTAL ----------
subtotal = round(subtotal, 2)
if TARGET is not None:
    ajuste = round(TARGET - subtotal, 2)
    total = round(subtotal + ajuste, 2)
    yy = y - 6*mm
    c.setFont("Helvetica", 9.5)
    c.drawRightString(col_imp - 3*mm, yy, "Subtotal"); c.drawRightString(box_r - 3*mm, yy, money(subtotal))
    yy -= 5.2*mm
    c.drawRightString(col_imp - 3*mm, yy, AJUSTE_LABEL); c.drawRightString(box_r - 3*mm, yy, money(ajuste))
    ty = yy - 10*mm
else:
    ajuste = 0.0
    total = subtotal
    ty = y - 12*mm
c.setFillColor(NAVY)
c.rect(col_imp - 35*mm, ty, box_r - (col_imp - 35*mm), 9*mm, fill=1, stroke=0)
c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 12)
c.drawString(col_imp - 33*mm, ty + 2.7*mm, "TOTAL")
c.drawRightString(box_r - 3*mm, ty + 2.7*mm, money(total))
c.setFillColor(colors.black)

# ---------- NOTAS / FIRMA ----------
ny = ty - 8*mm
c.setFont("Helvetica-Oblique", 8)
c.drawString(box_l, ny, "Presupuesto valido por %s. Precios mayoristas sujetos a modificacion sin previo aviso. Documento no valido como factura." % VALIDEZ)

fy = margin + 12*mm
c.setLineWidth(0.5)
c.line(box_r - 70*mm, fy, box_r - 6*mm, fy)
c.setFont("Helvetica", 8)
c.drawCentredString(box_r - 38*mm, fy - 4*mm, "Firma y aclaracion")

c.setFillColor(NAVY)
c.rect(box_l, margin - 3*mm, box_r - box_l, 5*mm, fill=1, stroke=0)
c.setFillColor(colors.white); c.setFont("Helvetica", 7.5)
c.drawCentredString(W/2, margin - 1.5*mm, "%s  ·  %s" % (EMISOR["nombre"], EMISOR["web"]))

c.showPage(); c.save()
print("PDF:", OUT, "| renglones:", len(ITEMS), "| subtotal:", money(subtotal), "| ajuste:", money(ajuste), "| TOTAL:", money(total))
EOF_GUARD = None
