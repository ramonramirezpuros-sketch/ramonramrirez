# -*- coding: utf-8 -*-
"""Remito / Nota de Venta membretado - Daniela Victoria Perez (Almacen de Tabacos)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas

EMISOR = {"nombre": "RAMON RAMIREZ", "tagline": "Cigarros Artesanales", "web": "www.ramonramirez.com.ar"}
NAVY = colors.HexColor("#14264f")
GOLD = colors.HexColor("#c8a24a")

CLIENTE = {
    "nombre": "Daniela Victoria Perez",
    "cuit": "27-35754543-4",
    "iva": "",
    "domicilio": "Bernardino Rivadavia 394 - Pilar (CP 1629), Bs. As.",
    "email": "almacendetabacos@gmail.com",
}
NUMERO = "0001-00000013"
FECHA = "30/10/2026"
CONDICION = "Contado - Precios Mayoristas"

ITEMS = [
    (15, "U", "Cigarrito I",                       1733.33),
    (10, "U", "Cigarrito II",                      2123.33),
    (10, "U", "Long Cigarrito",                    2426.67),
    (10, "U", "Petit Purito",                      4160.00),
    (10, "U", "Corona Ramirez",                    8233.33),
    (10, "U", "1/2 Corona Ramirez (Media Corona)", 7366.67),
]
OUT = "Remito_Daniela_Perez.pdf"

W, H = A4
c = canvas.Canvas(OUT, pagesize=A4)

def money(v):
    return "$ {:,.2f}".format(v).replace(",", "X").replace(".", ",").replace("X", ".")

margin = 15 * mm
box_l = margin; box_r = W - margin

# ---------- MEMBRETE ----------
band_h = 26 * mm
band_top = H - margin
c.setFillColor(NAVY); c.rect(box_l, band_top - band_h, box_r - box_l, band_h, fill=1, stroke=0)
c.setFillColor(GOLD); c.rect(box_l, band_top - band_h - 1.6*mm, box_r - box_l, 1.6*mm, fill=1, stroke=0)
c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 26)
c.drawString(box_l + 6*mm, band_top - 12*mm, EMISOR["nombre"])
c.setFillColor(colors.white); c.setFont("Helvetica-Oblique", 10)
c.drawString(box_l + 6*mm, band_top - 18*mm, EMISOR["tagline"])
c.setFont("Helvetica", 9); c.drawString(box_l + 6*mm, band_top - 23*mm, EMISOR["web"])
c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 17)
c.drawRightString(box_r - 6*mm, band_top - 11*mm, "REMITO / NOTA DE VENTA")
c.setFont("Helvetica", 9)
c.drawRightString(box_r - 6*mm, band_top - 17*mm, "N " + NUMERO)
c.drawRightString(box_r - 6*mm, band_top - 22*mm, "Fecha: " + FECHA)

# ---------- CLIENTE ----------
cy = band_top - band_h - 10*mm
c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10); c.drawString(box_l, cy, "CLIENTE")
c.setFillColor(colors.black); c.setFont("Helvetica", 10)
c.drawString(box_l, cy - 6*mm,  "Nombre:     " + CLIENTE["nombre"])
c.drawString(box_l, cy - 11*mm, "CUIT:       " + (CLIENTE["cuit"] or "____________________"))
c.drawString(box_l, cy - 16*mm, "Cond. IVA:  " + (CLIENTE["iva"] or "____________________"))
c.drawString(box_l, cy - 21*mm, "Domicilio:  " + (CLIENTE["domicilio"] or "______________________________"))
c.drawRightString(box_r, cy - 6*mm, CONDICION)
if CLIENTE.get("email"):
    c.drawRightString(box_r, cy - 11*mm, "Email: " + CLIENTE["email"])

# ---------- TABLA ----------
col_cant = box_l; col_desc = box_l + 25*mm; col_pu = box_l + 120*mm; col_imp = box_l + 150*mm
head_y = cy - 28*mm
row_h = 9 * mm
c.setFillColor(NAVY); c.rect(box_l, head_y, box_r - box_l, 7*mm, fill=1, stroke=0)
c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 9)
c.drawCentredString((col_cant + col_desc)/2, head_y + 2*mm, "CANT.")
c.drawString(col_desc + 2*mm, head_y + 2*mm, "DESCRIPCION")
c.drawCentredString((col_pu + col_imp)/2, head_y + 2*mm, "P. UNIT.")
c.drawCentredString((col_imp + box_r)/2, head_y + 2*mm, "IMPORTE")
c.setFillColor(colors.black)

y = head_y
total = 0.0
n_rows = 9
for i in range(n_rows):
    y -= row_h
    if i % 2 == 0:
        c.setFillColor(colors.HexColor("#f2f3f7")); c.rect(box_l, y, box_r - box_l, row_h, fill=1, stroke=0); c.setFillColor(colors.black)
    c.setLineWidth(0.3); c.setStrokeColor(colors.HexColor("#cccccc")); c.line(box_l, y, box_r, y); c.setStrokeColor(colors.black)
    if i < len(ITEMS):
        qty, unit, desc, pu = ITEMS[i]
        imp = round(qty * pu, 2); total += imp
        c.setFont("Helvetica", 9.5)
        c.drawCentredString((col_cant + col_desc)/2, y + 2.6*mm, "%d %s" % (qty, unit))
        c.drawString(col_desc + 2*mm, y + 2.6*mm, desc)
        c.drawRightString(col_imp - 3*mm, y + 2.6*mm, money(pu))
        c.drawRightString(box_r - 3*mm, y + 2.6*mm, money(imp))

c.setLineWidth(0.6); c.setStrokeColor(NAVY)
c.rect(box_l, y, box_r - box_l, head_y + 7*mm - y, fill=0, stroke=1)
for xx in (col_desc, col_pu, col_imp):
    c.line(xx, head_y, xx, y)
c.setStrokeColor(colors.black)

total = round(total, 2)
ty = y - 12*mm
c.setFillColor(NAVY); c.rect(col_imp - 35*mm, ty, box_r - (col_imp - 35*mm), 10*mm, fill=1, stroke=0)
c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 12)
c.drawString(col_imp - 33*mm, ty + 3*mm, "TOTAL")
c.drawRightString(box_r - 3*mm, ty + 3*mm, money(total))
c.setFillColor(colors.black)

fy = margin + 18*mm
c.setLineWidth(0.5)
c.line(box_l + 10*mm, fy, box_l + 70*mm, fy); c.line(box_r - 70*mm, fy, box_r - 10*mm, fy)
c.setFont("Helvetica", 8)
c.drawCentredString(box_l + 40*mm, fy - 4*mm, "Firma y aclaracion (Vendedor)")
c.drawCentredString(box_r - 40*mm, fy - 4*mm, "Recibi conforme (Cliente)")

c.setFillColor(NAVY); c.rect(box_l, margin - 2*mm, box_r - box_l, 5*mm, fill=1, stroke=0)
c.setFillColor(colors.white); c.setFont("Helvetica", 7.5)
c.drawCentredString(W/2, margin - 0.5*mm, "%s  ·  %s  ·  Documento no valido como factura" % (EMISOR["nombre"], EMISOR["web"]))

c.showPage(); c.save()
print("PDF:", OUT, "| TOTAL:", money(total))
