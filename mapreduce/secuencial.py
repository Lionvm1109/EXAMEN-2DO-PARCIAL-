import time

start_time = time.time()
totales = {}
conteos = {}

with open('ventas_125053792.csv', 'r') as f:
    for line in f:
        if line.startswith('id,'):
            continue
        parts = line.strip().split(',')
        if len(parts) == 8:
            tienda = parts[2]
            try:
                cantidad = float(parts[5])
                precio = float(parts[6])
                ingreso = cantidad * precio
                totales[tienda] = totales.get(tienda, 0.0) + ingreso
                conteos[tienda] = conteos.get(tienda, 0) + 1
            except ValueError:
                continue

for tienda in sorted(totales.keys()):
    promedio = totales[tienda] / conteos[tienda]
    print("%s\t%.2f" % (tienda, promedio))

print("\nTiempo ejecucion secuencial: %.2f segundos" % (time.time() - start_time))
