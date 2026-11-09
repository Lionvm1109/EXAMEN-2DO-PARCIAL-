#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("id,"):
        continue

    parts = line.split(",")
    if len(parts) == 8:
        tienda = parts[2]
        try:
            cantidad = float(parts[5])
            precio = float(parts[6])
            ingreso = cantidad * precio
            print("%s\t%.2f" % (tienda, ingreso))
        except ValueError:
            continue
