from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from recursos import app_prediccion, app_db_handler

_VERSION = '3.1.0'

app = FastAPI(title='API Challenge AB InBev',
              description="API para disponibilizar modelo de ML que hace Sentiment Classification de texto escrito en inglés.",
              version=_VERSION)

# Añade los endpoint del api router de app_prediccion_ML
app.include_router(app_prediccion)

# Añade los endpoint del api router de app_db
app.include_router(app_db_handler)


@app.get('/health', status_code=200, tags=['Info'])
def health_msg():
    ''' Devuelve un mensaje de status predeterminado si y solo si la API está arriba. Endpoint de health para monitoreo.'''
    
    return {'status':'Service UP'}


@app.get('/', status_code=200, tags=['Info'])
def index() -> HTMLResponse:
    '''Devuelve un mensaje predeterminado en el Endpoint raíz.'''

    content = """
        <body>
        <h2> API del challenge de AB InBev</h2>
        <p> La siguiente API es el resultado del desarrollo según los lineamientos dados en la documentación de la prueba técnica: </p>
        <p> Para ver y probar los endpoints que componen la API se puede hacer através de la URL: localhost:8108/docs </p>
        <p> Para probar la API se creó un front (UI) con Streamlit que hace peticiones a esta API.</p>
        </body>
    """

    return HTMLResponse(content=content)
