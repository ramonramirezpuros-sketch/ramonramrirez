# -*- coding: utf-8 -*-
"""Presupuesto $1.800.000 version SIN E.M.A, con volumen trasladado a linea ORO."""

from gen_presupuesto_multi import generate, money

ITEMS = [
    (12, "U", "Cigarrito I",                 1733.33),
    (12, "U", "Cigarrito II",                2123.33),
    (12, "U", "Long Cigarrito",              2426.67),
    (25, "U", "Petit Purito",                4160.00),
    (12, "U", "Mini Short Robusto",          5200.00),
    (18, "U", "Petit Robusto",               6500.00),
    (12, "U", "Robusto Ramirez",             9360.00),
    (12, "U", "Super Robusto",              10313.33),
    (14, "U", "Toro Ramirez",                9360.00),
    (10, "U", "Petit Corona",                7713.33),
    (17, "U", "1/2 Corona Ramirez",          7366.67),
    (14, "U", "Corona Ramirez",              8233.33),
    (10, "U", "Petit Robusto Oro",          13000.00),
    (18, "U", "1/2 Corona Oro",             14733.33),
    ( 6, "U", "Don Ramon Oro",              28600.00),
    (24, "U", "Bolsas Humidoras PocketBag",  5800.00),
]

t = generate("Presupuesto_Mayorista_1800000.pdf", "PRES-0001-00000015", ITEMS)
print("1.8M (ORO, sin EMA) ->", money(t))
