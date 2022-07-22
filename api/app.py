from fastapi import FastAPI

_VERSION = '1.1.0'

app = FastAPI(title='API Challenge AB InBev',
              version=_VERSION)

@app.get('/health', status_code=200, tags=['Health'])
def health_msg():
    ''' Devuelve un mensaje de status predeterminado si y solo si la API está arriba. Endpoint de health para monitoreo.'''
    return {'status':'Service UP'}

@app.get('/', status_code=200, tags=['Health'])
def index():
    '''Devuelve un mensaje predeterminado en el Endpoint raíz.'''
    return {'MSG':'Para ver la documentación vaya a la url /redoc'}

# uvicorn app:app