from pydantic import BaseModel

class Tuits(BaseModel):
    textos: list[str] | None = []

class Prediccion(BaseModel):
    tweet:str
    pred:int
    label:str

class RespuestaModelo(BaseModel):
    respuesta: list[Prediccion]