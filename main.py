from fastapi import FastAPI
from pydantic import BaseModel

import clasificador
from database import guardarClasificacion, retornarConsultas

class MensajeRequest (BaseModel):
    mensaje: str

app = FastAPI()

@app.post("/clasificar")
def clasificar_mensaje(request: MensajeRequest):
    datos = clasificador.clasicadorMensaje(request.mensaje)
    guardarClasificacion(request.mensaje, datos["categoria"], datos["idioma"], datos["sentimiento"], datos["resumen"])
    return datos

@app.get("/retornar")
def retorno_database():
    datos = retornarConsultas()
    return datos