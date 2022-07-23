from pydantic import BaseModel

class Tuits(BaseModel):
    textos: list[str] | None = []

    class Config:
        schema_extra = {
            "example": {
                "textos": ["it's OK my friend", "That's bad!"]
                }
        }

class Prediccion(BaseModel):
    tweet:str
    pred:int
    label:str

    class Config:
        schema_extra = {
            "example":{
                    "tweet": "I like this code!",
                    "pred": 1,
                    "label": "Positive"
                    }
        }

class RespuestaModelo(BaseModel):

    respuesta: list[Prediccion]

    class Config:
        schema_extra = {
            "example": 
            [
                {
                    "tweet": "it's OK my friend",
                    "pred": 1,
                    "label": "Positive"
                },
                {
                    "tweet": "That's bad!",
                    "pred": 0,
                    "label": "Negative"
                }
            ]
        }