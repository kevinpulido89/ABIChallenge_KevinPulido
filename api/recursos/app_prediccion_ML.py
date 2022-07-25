from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .data_structure import Tuits, RespuestaModelo
from .DB_handler import DataBaseActions
from .ml_model import ModelPipeline


app_prediccion = APIRouter()
modelo_pipeline = ModelPipeline()


@app_prediccion.post('/predict', status_code=200, response_model=RespuestaModelo, tags=['ML'])
async def get_prediction(tweets: Tuits) -> JSONResponse:
    """
    Endpoint de predicción que recibe Tuits y responde con un JSON (respuesta válida o error)

        Args:
            tweets (Tuits): Objeto cuya estructura tiene los textos que se desean clasificar

        Returns:
            JSONResponse: JSON con infomación de la respuesta. Si la respuesta es correcta la estructura es del tipo 'RespuestaModelo'. Si la respuesta es inválida es un 'JSONResponse' con status code y texto del error.
    """

    try:
        # Extrae los textos de la instancia tweets en formato lista
        samples = tweets.textos
    except KeyError:
        return JSONResponse(content="No hay texto para predecir", status_code=400)
    
    try:
        # Clasifica el batch de textos
        prediccion = modelo_pipeline.predict_pipeline(samples)

        #Almacena en Mongo la prediccion
        try:
            await DataBaseActions.insert(prediccion)
            return JSONResponse(content = {
                    "MongoDB": "✅ Datos almacenados con éxito!",
                    "Response_Predict": prediccion})
        except Exception as e:
            print(e)
            return JSONResponse(content = {
                        "MongoDB": "❌ Datos NO almacenados. Error en la conexión",
                        "Response_Predict": prediccion})
        
    except ValueError as e:
        return JSONResponse(content=f"Error: {e}", status_code=422)