from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI()
db_resultados: Dict[str, float] = {}

class ResultadoItem(BaseModel):
    tienda: str
    promedio: float

@app.get("/")
def root():
    return {"status": "ok", "matricula": "125053792"}

@app.get("/resultados")
def get_resultados():
    return db_resultados

@app.post("/resultados")
def add_resultado(item: ResultadoItem):
    db_resultados[item.tienda] = item.promedio
    return {"message": "Guardado exitosamente", "data": item}
