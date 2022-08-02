from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

msg = {
        "textos": ["it's OK my friend"]
      }

out = {
        "MongoDB": "❌ Datos NO almacenados. Error en la conexión",
        "Response_Predict": [
            {
            "tweet": "it's OK my friend",
            "pred": 1,
            "label": "Positive"
            }
        ]
      }

def test_health_msg():
    "funcion de test para el endpoint root"
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status':'Service UP'}


def test_get_prediction():
    "funcion de test para el endpoint predict"
    response = client.post('/predict', json=msg)
    assert response.status_code == 200
    assert response.json() == out