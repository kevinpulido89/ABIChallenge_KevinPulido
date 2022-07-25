from pydantic import BaseModel

class Tuits(BaseModel):
    textos: list[str]
