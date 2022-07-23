from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .data_structure import Tuits, RespuestaModelo
from .ml_model import ModelPipeline


api_router = APIRouter()
modelo_pipeline = ModelPipeline()


@api_router.post('/predict', status_code=200, response_model=RespuestaModelo, tags=['ML'])
def get_prediction(tweets: Tuits) -> JSONResponse:
    """
    Endpoint de predicción que recibe Tuits y responde con un JSON (respuesta válida o error)

        Args:
            tweets (Tuits): _description_

        Returns:
            JSONResponse: JSON con infomación de la respuesta. Si la respuesta es correcta la estructura es del tipo 'RespuestaModelo'. Si la respuesta es inválida es un 'JSONResponse' con status code y texto del error.
    """

    try:
        samples = tweets.textos
    except KeyError:
        return JSONResponse(content="No hay texto para predecir", status_code=400)
    
    try:
        prediccion = modelo_pipeline.predict_pipeline(samples)

        return JSONResponse(prediccion)
    except ValueError as e:
        return JSONResponse(content=f"Error: {e}", status_code=422)