from contextlib import asynccontextmanager
from pathlib import Path
from typing import Literal

import joblib
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from fastapi.middleware.cors import CORSMiddleware

RUTA_MODELO = Path(__file__).resolve().parent.parent / "modelo" / "modelo.joblib"

# NUEVO: mismas columnas y mismo orden que en el entrenamiento
COLUMNAS = ["edad", "imc", "hijos", "sexo", "fumador", "region"]

estado = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Cargando modelo desde", RUTA_MODELO)
    estado["modelo"] = joblib.load(RUTA_MODELO)
    print("Modelo cargado ✔")
    yield
    estado.clear()


app = FastAPI(title="API Costo de Seguro Médico", lifespan=lifespan)
# Orígenes (páginas) que pueden llamar a esta API desde el navegador
ORIGENES_PERMITIDOS = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGENES_PERMITIDOS,
    allow_methods=["GET", "POST"],
    allow_headers=["Content-Type"],
)


# NUEVO: el "molde" que tiene que cumplir el JSON de entrada
class Persona(BaseModel):
    edad: int = Field(..., ge=18, le=64, description="Edad en años (18 a 64)")
    sexo: Literal["female", "male"]
    imc: float = Field(..., ge=10, le=60, description="Índice de masa corporal")
    hijos: int = Field(..., ge=0, le=5, description="Cantidad de hijos a cargo")
    fumador: Literal["yes", "no"]
    region: Literal["northeast", "northwest", "southeast", "southwest"]


# NUEVO: el "molde" de la respuesta
class Prediccion(BaseModel):
    costo_estimado: float


@app.get("/health")
def health():
    return {"estado": "ok"}


# NUEVO: el endpoint de predicción
@app.post("/predecir", response_model=Prediccion)
def predecir(persona: Persona):
    modelo = estado.get("modelo")
    if modelo is None:
        raise HTTPException(status_code=500, detail="El modelo no está cargado.")
    try:
        datos = pd.DataFrame([persona.model_dump()], columns=COLUMNAS)
        costo = float(modelo.predict(datos)[0])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al predecir: {e}")
    return {"costo_estimado": round(costo, 2)}