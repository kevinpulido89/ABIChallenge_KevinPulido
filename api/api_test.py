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
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status':'Service UP'}
    print("✅ Test Done!")

def test_get_prediction():
    response = client.post('/predict', json=msg)
    assert response.status_code == 200
    assert response.json() == out