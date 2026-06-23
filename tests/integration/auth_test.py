from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_login():
    response = client.post('/login/', json={'email': 'test@example.com', 'password': 'strongpassword'})
    assert response.status_code == 200
    assert 'access_token' in response.json()