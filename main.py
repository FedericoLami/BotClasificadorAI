from pydantic import BaseModel
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

import clasificador
from database import guardarClasificacion, retornarConsultas

class MensajeRequest (BaseModel):
    mensaje: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/clasificar")
def clasificar_mensaje(request: MensajeRequest):
    try:
        datos = clasificador.clasicadorMensaje(request.mensaje)
        guardarClasificacion(request.mensaje, datos["categoria"], datos["idioma"], datos["sentimiento"], datos["resumen"])
        return datos
    except ValueError:
        raise HTTPException(status_code=500, detail="Error al procesar la respuesta de Claude")


@app.get("/clasificaciones")
def retorno_database():
    datos = retornarConsultas()
    return datos
    