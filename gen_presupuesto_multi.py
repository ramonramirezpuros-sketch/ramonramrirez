# -*- coding: utf-8 -*-
"""Presupuestos membretados mayoristas (variedad: vitolario + EMA + Oro + bolsas)."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.pdfgen import canvas

EMISOR = {"nombre": "RAMON RAMIREZ", "tagline": "Cigarros Artesanales", "web": "www.ramonramirez.com.ar"}
NAVY = colors.HexColor("#14264f")
GOLD = colors.HexColor("#c8a24a")
FECHA = "30/10/2026"
VALIDEZ = "10 dias"
CONDICION = "Precios Mayoristas"
CLIENTE = {"nombre": "", "cuit": "", "domicilio": ""}

def build_items(pp, bo, sr, hc):
    """pp=Petit Purito, bo=Bolsas, sr=Super Robusto, hc=1/2 Corona Ramirez"""
    return [
        (10, "U", "Cigarrito I",                 1733.33),
        (10, "U", "Cigarrito II",                2123.33),
        (10, "U", "Long Cigarrito",              2426.67),
        (pp, "U", "Petit Purito",                4160.00),
        (10, "U", "Mini Short Robusto",          5200.00),
        (15, "U", "Petit Robusto",               6500.00),
        (10, "U", "Robusto Ramirez",             9360.00),
        (sr, "U", "Super Robusto",              10313.33),
        (12, "U", "Toro Ramirez",                9360.00),
        ( 8, "U", "Petit Corona",                7713.33),
        (hc, "U", "1/2 Corona Ramirez",          7366.67),
        (12, "U", "Corona Ramirez",              8233.33),
        ( 6, "U", "Ramon Ramirez I",            10053.33),
        ( 6, "U", "Ramon Ramirez II",           13000.00),
        ( 8, "U", "Churchill Ramirez",          14300.00),
        ( 6, "U", "Petit Robusto E.M.A",         9750.00),
        ( 5, "U", "Robusto Ramirez E.M.A",      13866.67),
        ( 5, "U", "Toro Ramirez E.M.A",         14040.00),
        ( 4, "U", "Ramon Ramirez E.M.A",        14300.00),
        ( 5, "U", "Petit Robusto Oro",          13000.00),
        ( 5, "U", "1/2 Corona Oro",             14733.33),
        ( 4, "U", "Don Ramon Oro",              28600.00),
        (bo, "U", "Bolsas Humidoras PocketBag",  5800.00),
    ]

def money(v):
    return "$ {:,.2f}".format(v).replace(",", "X").replace(".", ",").replace("X", ".")

def generate(out, numero, items):
    W, H = A4
    c = canvas.Canvas(out, pagesize=A4)
    margin = 12 * mm
    box_l = margin; box_r = W - margin

    # Membrete
    band_h = 23 * mm
    band_top = H - margin
    c.setFillColor(NAVY); c.rect(box_l, band_top - band_h, box_r - box_l, band_h, fill=1, stroke=0)
    c.setFillColor(GOLD); c.rect(box_l, band_top - band_h - 1.3*mm, box_r - box_l, 1.3*mm, fill=1, stroke=0)
    c.setFillColor(GOLD); c.setFont("Helvetica-Bold", 23)
    c.drawString(box_l + 6*mm, band_top - 10.5*mm, EMISOR["nombre"])
    c.setFillColor(colors.white); c.setFont("Helvetica-Oblique", 9)
    c.drawString(box_l + 6*mm, band_top - 15.5*mm, EMISOR["tagline"])
    c.setFont("Helvetica", 8); c.drawString(box_l + 6*mm, band_top - 19.5*mm, EMISOR["web"])
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 16)
    c.drawRightString(box_r - 6*mm, band_top - 9.5*mm, "PRESUPUESTO")
    c.setFont("Helvetica", 8)
    c.drawRightString(box_r - 6*mm, band_top - 14.5*mm, "N " + numero)
    c.drawRightString(box_r - 6*mm, band_top - 18.5*mm, "Fecha: " + FECHA)
    c.setFillColor(colors.black)

    # Cliente
    cy = band_top - band_h - 7*mm
    c.setFillColor(NAVY); c.setFont("Helvetica-Bold", 9)
    c.drawString(box_l, cy, "CLIENTE")
    c.setFillColor(colors.black); c.setFont("Helvetica", 9)
    c.drawString(box_l, cy - 5*mm,  "Nombre:    " + (CLIENTE["nombre"] or "____________________"))
    c.drawString(box_l, cy - 9.5*mm,"CUIT:      " + (CLIENTE["cuit"] or "____________________"))
    c.drawRightString(box_r, cy - 5*mm,  "Validez: " + VALIDEZ)
    c.drawRightString(box_r, cy - 9.5*mm, CONDICION)

    # Tabla
    col_cant = box_l; col_desc = box_l + 22*mm; col_pu = box_l + 122*mm; col_imp = box_l + 152*mm
    head_y = cy - 15*mm
    n = len(items)
    # alto de fila adaptativo para entrar en una pagina
    bottom_needed = margin + 30*mm
    avail = (head_y) - bottom_needed
    row_h = min(6.0*mm, avail / n)

    c.setFillColor(NAVY); c.rect(box_l, head_y, box_r - box_l, 6*mm, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 8)
    c.drawCentredString((col_cant + col_desc)/2, head_y + 1.7*mm, "CANT.")
    c.drawString(col_desc + 2*mm, head_y + 1.7*mm, "DESCRIPCION")
    c.drawCentredString((col_pu + col_imp)/2, head_y + 1.7*mm, "P. UNIT.")
    c.drawCentredString((col_imp + box_r)/2, head_y + 1.7*mm, "IMPORTE")
    c.setFillColor(colors.black)

    y = head_y
    total = 0.0
    for i, (qty, unit, desc, pu) in enumerate(items):
        y -= row_h
        if i % 2 == 0:
            c.setFillColor(colors.HexColor("#f2f3f7")); c.rect(box_l, y, box_r - box_l, row_h, fill=1, stroke=0); c.setFillColor(colors.black)
        c.setLineWidth(0.25); c.setStrokeColor(colors.HexColor("#d0d0d0")); c.line(box_l, y, box_r, y); c.setStrokeColor(colors.black)
        imp = round(qty * pu, 2); total += imp
        c.setFont("Helvetica", 8.2)
        c.drawCentredString((col_cant + col_desc)/2, y + 1.6*mm, "%d %s" % (qty, unit))
        c.drawString(col_desc + 2*mm, y + 1.6*mm, desc)
        c.drawRightString(col_imp - 3*mm, y + 1.6*mm, money(pu))
        c.drawRightString(box_r - 3*mm, y + 1.6*mm, money(imp))

    c.setLineWidth(0.6); c.setStrokeColor(NAVY)
    c.rect(box_l, y, box_r - box_l, head_y + 6*mm - y, fill=0, stroke=1)
    for xx in (col_desc, col_pu, col_imp):
        c.line(xx, head_y, xx, y)
    c.setStrokeColor(colors.black)

    total = round(total, 2)
    ty = y - 11*mm
    c.setFillColor(NAVY); c.rect(col_imp - 35*mm, ty, box_r - (col_imp - 35*mm), 9*mm, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica-Bold", 12)
    c.drawString(col_imp - 33*mm, ty + 2.7*mm, "TOTAL")
    c.drawRightString(box_r - 3*mm, ty + 2.7*mm, money(total))
    c.setFillColor(colors.black)

    ny = ty - 7*mm
    c.setFont("Helvetica-Oblique", 7.5)
    c.drawString(box_l, ny, "Presupuesto valido por %s. Precios mayoristas sujetos a modificacion sin previo aviso. Documento no valido como factura." % VALIDEZ)

    fy = margin + 11*mm
    c.setLineWidth(0.5); c.line(box_r - 70*mm, fy, box_r - 6*mm, fy)
    c.setFont("Helvetica", 8); c.drawCentredString(box_r - 38*mm, fy - 4*mm, "Firma y aclaracion")
    c.setFillColor(NAVY); c.rect(box_l, margin - 3*mm, box_r - box_l, 5*mm, fill=1, stroke=0)
    c.setFillColor(colors.white); c.setFont("Helvetica", 7.5)
    c.drawCentredString(W/2, margin - 1.5*mm, "%s  ·  %s" % (EMISOR["nombre"], EMISOR["web"]))

    c.showPage(); c.save()
    return total

if __name__ == "__main__":
    # ---- 1.700.000 ----
    it17 = build_items(pp=18, bo=21, sr=8, hc=11)
    t17 = generate("Presupuesto_Mayorista_1700000.pdf", "PRES-0001-00000014", it17)
    # ---- 1.800.000 ----
    it18 = build_items(pp=18, bo=23, sr=8, hc=23)
    t18 = generate("Presupuesto_Mayorista_1800000.pdf", "PRES-0001-00000015", it18)
    print("1.7M ->", money(t17))
    print("1.8M ->", money(t18))
