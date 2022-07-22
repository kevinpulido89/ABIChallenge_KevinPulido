from fastapi import FastAPI

_VERSION = '1.0.1'

app = FastAPI(title='API Challenge AB InBev',
              version=_VERSION)

@app.get('/health', status_code=200, tags=['Health'])
def health_msg():
    ''' Devuelve un mensaje de status predeterminado si y solo si la API está arriba. Endpoint de health para monitoreo.'''
    return {'status':'Service UP'}

# uvicorn app:app