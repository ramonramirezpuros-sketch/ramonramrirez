# -*- coding: utf-8 -*-
"""Resumen de remitos / notas de venta en Excel (Fecha, Cliente, Importe)."""

from datetime import date
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# (fecha, cliente, importe)
REMITOS = [
    (date(2026, 9, 28),  "Gonzalo Muriel",                                 73210.00),
    (date(2026, 10, 8),  "Barga y Perez Sofia (Cultura Humo)",            626349.80),
    (date(2026, 10, 8),  "Fernando Guidoli",                             1000000.00),
    (date(2026, 10, 9),  "Munoz Mauro Oscar",                             784949.84),
    (date(2026, 10, 19), "Tabaqueria El Faro",                            186083.25),
    (date(2026, 10, 21), "Tabaqueria Tigre",                              182449.99),
    (date(2026, 10, 21), "Digi Fora",                                     117866.60),
    (date(2026, 10, 27), "Digi Fora (60 Petit Purito)",                   249600.00),
    (date(2026, 10, 27), "Sin cliente - convertido de imagen",            483816.61),
    (date(2026, 10, 27), "La Tabaqueria (Abril Peralta Celaya)",          129133.30),
    (date(2026, 10, 30), "Daniela Victoria Perez (Almacen de Tabacos)",   269099.95),
    (date(2026, 11, 3),  "Sebastian Cruzado",                             870345.00),
]

OUT = "Remitos_Resumen.xlsx"

NAVY = "14264F"
GOLD = "C8A24A"
LIGHT = "F2F3F7"
WHITE = "FFFFFF"

wb = Workbook()
ws = wb.active
ws.title = "Remitos"

thin = Side(style="thin", color="BBBBBB")
border = Border(left=thin, right=thin, top=thin, bottom=thin)

# Titulo
ws.merge_cells("A1:C1")
t = ws["A1"]
t.value = "RESUMEN DE REMITOS / NOTAS DE VENTA  -  RAMON RAMIREZ"
t.font = Font(name="Arial", size=13, bold=True, color=WHITE)
t.fill = PatternFill("solid", fgColor=NAVY)
t.alignment = Alignment(horizontal="center", vertical="center")
ws.row_dimensions[1].height = 26

# Encabezados
headers = ["Fecha", "Cliente", "Importe"]
for j, h in enumerate(headers, start=1):
    cell = ws.cell(row=2, column=j, value=h)
    cell.font = Font(name="Arial", size=11, bold=True, color=WHITE)
    cell.fill = PatternFill("solid", fgColor=GOLD)
    cell.alignment = Alignment(horizontal="center", vertical="center")
    cell.border = border
ws.row_dimensions[2].height = 20

# Datos
first_data = 3
for i, (f, cliente, importe) in enumerate(REMITOS):
    r = first_data + i
    fill = LIGHT if i % 2 == 0 else WHITE
    cf = ws.cell(row=r, column=1, value=f)
    cf.number_format = "DD/MM/YYYY"
    cf.alignment = Alignment(horizontal="center")
    cc = ws.cell(row=r, column=2, value=cliente)
    ci = ws.cell(row=r, column=3, value=importe)
    ci.number_format = '"$"#,##0.00'
    for col in (1, 2, 3):
        cell = ws.cell(row=r, column=col)
        cell.font = Font(name="Arial", size=10)
        cell.fill = PatternFill("solid", fgColor=fill)
        cell.border = border
    cc.alignment = Alignment(horizontal="left")
    ci.alignment = Alignment(horizontal="right")

last_data = first_data + len(REMITOS) - 1

# Total
tr = last_data + 1
lbl = ws.cell(row=tr, column=2, value="TOTAL")
lbl.font = Font(name="Arial", size=11, bold=True, color=WHITE)
lbl.fill = PatternFill("solid", fgColor=NAVY)
lbl.alignment = Alignment(horizontal="right")
lbl.border = border
tot = ws.cell(row=tr, column=3, value="=SUM(C%d:C%d)" % (first_data, last_data))
tot.number_format = '"$"#,##0.00'
tot.font = Font(name="Arial", size=11, bold=True, color=WHITE)
tot.fill = PatternFill("solid", fgColor=NAVY)
tot.alignment = Alignment(horizontal="right")
tot.border = border
empty = ws.cell(row=tr, column=1, value=None)
empty.fill = PatternFill("solid", fgColor=NAVY)
empty.border = border

# Anchos de columna
ws.column_dimensions["A"].width = 14
ws.column_dimensions["B"].width = 42
ws.column_dimensions["C"].width = 18

# Freeze encabezados
ws.freeze_panes = "A3"

wb.save(OUT)
print("Excel generado:", OUT, "| filas:", len(REMITOS))
