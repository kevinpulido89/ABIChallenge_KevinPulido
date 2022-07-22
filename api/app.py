from fastapi import FastAPI
from pydantic import BaseModel

_VERSION = '1.2.0'

class RandomNumber(BaseModel):
    rand_number: int


app = FastAPI(title='API Challenge AB InBev',
              version=_VERSION)

@app.post('/random')
def predict(number: RandomNumber):
    ''' Recibe un número entero aleatorio y lo devuelve en el response'''
    return number.rand_number

@app.get('/health', status_code=200, tags=['Health'])
def health_msg():
    ''' Devuelve un mensaje de status predeterminado si y solo si la API está arriba. Endpoint de health para monitoreo.'''
    return {'status':'Service UP'}

@app.get('/', status_code=200, tags=['Health'])
def index():
    '''Devuelve un mensaje predeterminado en el Endpoint raíz.'''
    return {'MSG':'Para ver la documentación vaya a la url /redoc'}

# uvicorn app:app