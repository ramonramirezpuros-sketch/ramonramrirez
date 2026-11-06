# -*- coding: utf-8 -*-
"""Presupuesto / Cotizacion membretado - Tandil (RAMON RAMIREZ)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas

EMISOR = {"nombre": "RAMON RAMIREZ", "tagline": "Cigarros Artesanales", "web": "www.ramonramirez.com.ar"}
NAVY = colors.HexColor("#14264f")
GOLD = colors.HexColor("#c8a24a")

CLIENTE = "Tandil"
NUMERO = "Cotizacion N 001"
FECHA = "02/11/2026"
VALIDEZ = "10 dias"

SECCIONES = [
    ("1. Mobiliario y Accesorios", [
        ("1 Mueble humidor de cedro",   473000.00),
        ("20 Sobres humidor",           100000.00),
        ("10 Tubos",                     88000.00),
        ("5 Cortador guillotina",        54500.00),
        ("1 Petaca Ramon Ramirez",       13800.00),
    ]),
    ("2. Pocket Boxes", [
        ("5 Pocket Box Cigarrito I",     51566.65),
        ("2 Pocket Box 1/2 Corona RR",   59800.00),
        ("2 Pocket Box Ramon Ramirez I", 61533.34),
        ("2 Pocket Box Toro Ramirez",    58066.66),
    ]),
    ("3. Puros y Cigarritos Individuales", [
        ("20 Cigarrito II",              42466.60),
        ("20 Long Cigarrito",            48533.40),
        ("20 Petit Purito Anejado",      83200.00),
        ("10 Corona Ramirez Anejado",    82333.40),
        ("15 Petit Robusto Anejado",     97500.00),
        ("10 Robusto Ramirez Anejado",   93600.00),
        ("10 Mini Short Robusto Anejado",52000.00),
        ("5 Churchill Ramirez Anejado",  71500.00),
        ("2 Toro Ramirez Anejado",       18720.00),
    ]),
]
OUT = "Presupuesto_Tandil.pdf"

W, H = A4
c = canvas.Canvas(OUT, pagesize=A4)

def money(v):
    return "$ {:,.2f}".format(v).replace(",", "X").replace(".", ",").replace("X", ".")

margin = 15 * mm
box_l = margin; box_r = W - margin
col_imp = box_l + 130*mm

# Membrete
band_h = 26 * mm
band_top = H - margin
c.setFillColor(NAVY); c.rect(box_l, band_top - band_h, box_r - box_l, band_h, fill=1, stroke=0)
c.setFillColor(GOLD); c.rect(box_l, band_top - band_h - 1.6*mm, box_r - box_l, 1.6*mm, fill=1, stroke=0)
c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 26)
c.drawString(box_l + 6*mm, band_top - 12*mm, EMISOR["nombre"])
c.setFillColor(colors.white); c.setFont("Helvetica-Oblique", 10)
c.drawString(box_l + 6*mm, band_top - 18*mm, EMISOR["tagline"])
c.setFont("Helvetica", 9); c.drawString(box_l + 6*mm, band_top - 23*mm, EMISOR["web"])
c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 18)
c.drawRightString(box_r - 6*mm, band_top - 11*mm, "PRESUPUESTO")
c.setFont("Helvetica", 9)
c.drawRightString(box_r - 6*mm, band_top - 17*mm, NUMERO)
c.drawRightString(box_r - 6*mm, band_top - 22*mm, "Fecha: " + FECHA)

# Cliente
cy = band_top - band_h - 9*mm
c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 10); c.drawString(box_l, cy, "CLIENTE:")
c.setFillColor(colors.black); c.setFont("Helvetica", 10)
c.drawString(box_l + 22*mm, cy, CLIENTE)
c.drawRightString(box_r, cy, "Validez: " + VALIDEZ)

# Secciones
y = cy - 9*mm
total = 0.0
for titulo, items in SECCIONES:
    # header de seccion
    c.setFillColor(NAVY); c.rect(box_l, y - 6.5*mm, box_r - box_l, 6.5*mm, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 9.5)
    c.drawString(box_l + 3*mm, y - 4.6*mm, titulo.upper())
    c.drawRightString(box_r - 3*mm, y - 4.6*mm, "IMPORTE")
    c.setFillColor(colors.black)
    y -= 6.5*mm
    sub = 0.0
    for i, (concepto, imp) in enumerate(items):
        y -= 6.0*mm
        if i % 2 == 0:
            c.setFillColor(colors.HexColor("#f2f3f7")); c.rect(box_l, y, box_r - box_l, 6.0*mm, fill=1, stroke=0); c.setFillColor(colors.black)
        c.setFont("Helvetica", 9.3)
        c.drawString(box_l + 3*mm, y + 1.7*mm, concepto)
        c.drawRightString(box_r - 3*mm, y + 1.7*mm, money(imp))
        sub += imp; total += imp
    # subtotal de seccion
    y -= 5.4*mm
    c.setFont("Helvetica-Oblique", 8.8)
    c.drawRightString(col_imp - 2*mm, y + 1.4*mm, "Subtotal seccion:")
    c.setFont("Helvetica-Bold", 9)
    c.drawRightString(box_r - 3*mm, y + 1.4*mm, money(sub))
    c.setStrokeColor(colors.HexColor("#cccccc")); c.setLineWidth(0.3); c.line(box_l, y, box_r, y); c.setStrokeColor(colors.black)
    y -= 3*mm

# Total general
total = round(total, 2)
ty = y - 6*mm
c.setFillColor(NAVY); c.rect(col_imp - 20*mm, ty, box_r - (col_imp - 20*mm), 11*mm, fill=1, stroke=0)
c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 12)
c.drawString(col_imp - 18*mm, ty + 3.3*mm, "TOTAL GENERAL")
c.drawRightString(box_r - 3*mm, ty + 3.3*mm, money(total))
c.setFillColor(colors.black)

# Nota
ny = ty - 8*mm
c.setFont("Helvetica-Oblique", 8)
c.drawString(box_l, ny, "Presupuesto valido por %s. Precios sujetos a modificacion sin previo aviso. Documento no valido como factura." % VALIDEZ)

# Pie
c.setFillColor(NAVY); c.rect(box_l, margin - 2*mm, box_r - box_l, 5*mm, fill=1, stroke=0)
c.setFillColor(colors.white); c.setFont("Helvetica", 7.5)
c.drawCentredString(W/2, margin - 0.5*mm, "%s  ·  %s" % (EMISOR["nombre"], EMISOR["web"]))

c.showPage(); c.save()
print("PDF:", OUT, "| TOTAL:", money(total))
