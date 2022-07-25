from fastapi import APIRouter
from fastapi.responses import JSONResponse
from .DB_handler import DataBaseActions


app_db_handler = APIRouter()

@app_db_handler.get("/retrieve_all_data/", status_code=201, response_model_exclude_none=True, tags=['DB'])
async def get_all():
    '''Endpoint para recopilar todos los documentos de la base de datos pertenecientes a la collección "Predicciones".'''
    _all_documentos = await DataBaseActions.retrieve_all()

    return JSONResponse(_all_documentos)


@app_db_handler.get("/find_one/{id}", status_code=201, response_model_exclude_none=True, tags=['DB'])
async def get_id(id: str):
    '''Endpoint para recopilar un documento de la base de datos perteneciente a la collección "Predicciones" a partir de su **id**.'''

    _found = await DataBaseActions.retrieve_id(id)

    return JSONResponse(_found)


@app_db_handler.delete("/delete/{id}", status_code=201, response_model_exclude_none=True, tags=['DB'])
async def delete(id: str):
    '''Endpoint para eliminar un documento de la base de datos perteneciente a la collección "Predicciones" a partir de su **id**.'''

    await DataBaseActions.delete(id)

    return JSONResponse(content=f"Documento con {id=} eliminado.")