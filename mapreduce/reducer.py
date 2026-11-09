#!/usr/bin/env python3
import sys

current_tienda = None
total_ingreso = 0.0
count = 0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split("\t")
    if len(parts) != 2:
        continue

    tienda, ingreso_str = parts
    try:
        ingreso = float(ingreso_str)
    except ValueError:
        continue

    if current_tienda == tienda:
        total_ingreso += ingreso
        count += 1
    else:
        if current_tienda is not None:
            ticket_promedio = total_ingreso / count
            print("%s\t%.2f" % (current_tienda, ticket_promedio))
        current_tienda = tienda
        total_ingreso = ingreso
        count = 1

if current_tienda is not None and count > 0:
    ticket_promedio = total_ingreso / count
    print("%s\t%.2f" % (current_tienda, ticket_promedio))
