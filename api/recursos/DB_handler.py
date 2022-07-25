import uuid
import json
from datetime import datetime
import motor.motor_asyncio
from bson import json_util
from dataclasses import dataclass
# from .data_structure import Documento, RespuestaModelo

def db_connection(mongo_uri:str, data_base_name:str):
    """Genera la conexión a MongoDB a una base de datos en específico y retorna la base de datos como objeto instanciada

    Args:
        mongo_uri (str): URI (host y puerto) que apunta a MongoDB
        data_base_name (str): Nombre de la base de datos que se instancia

    Returns:
        Objeto DB: Objeto de la conexión a la base de datos estipulada.
    """
    
    cliente =  motor.motor_asyncio.AsyncIOMotorClient(mongo_uri)
    db = cliente[data_base_name]

    return db

@dataclass
class DataBaseActions:

    @staticmethod
    async def insert(prediccion):

        now = datetime.now()
       
        nuevo_documento = {
            "_id"       : f'AB_{uuid.uuid4()}',
            "ml_result" : prediccion,
            "date"      : now.strftime("%Y-%m-%d"),
            "time"      : now.strftime("%H:%M:%S")
        }
        await database.get_collection('predicciones').insert_one(nuevo_documento)

        return nuevo_documento

    @staticmethod
    async def retrieve_all():
        
        collection = database.get_collection('predicciones').find()

        
        _all_documentos = [json.loads(json_util.dumps(documento)) async for documento in collection]

        return _all_documentos

    @staticmethod
    async def retrieve_id(id: str):
        return await database.get_collection('predicciones').find_one({"_id": id})

    @staticmethod
    async def delete(id: str):
        await database.get_collection('predicciones').delete_one({"_id": id})

#! Instanciar y crear conexión a DB
database = db_connection(mongo_uri = 'mongodb://mongo:27017', data_base_name='ab_inbev')