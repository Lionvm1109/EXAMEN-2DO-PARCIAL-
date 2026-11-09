import urllib.request
import json

url = "http://localhost:8000/resultados"

with open("resultado_125053792.txt", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) == 2:
            payload = json.dumps({"tienda": parts[0], "promedio": float(parts[1])}).encode("utf-8")
            req = urllib.request.Request(url, data=payload, headers={'Content-Type': 'application/json'})
            try:
                urllib.request.urlopen(req)
                print(f"Cargado: {parts[0]}")
            except Exception as e:
                print(f"Error cargando {parts[0]}: {e}")
