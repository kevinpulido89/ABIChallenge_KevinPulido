from fastapi import FastAPI

_VERSION = '1.0.0'

app = FastAPI(title='API Challenge AB InBev',
              version=_VERSION)

@app.get('/health')
def health_msg():
    return {'status':'Service UP'}
