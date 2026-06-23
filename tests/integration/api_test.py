from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_create_user():
    response = client.post('/users/', json={'email': 'test@example.com', 'password': 'strongpassword'})
    assert response.status_code == 201
    assert response.json()['email'] == 'test@example.com'


def test_get_user():
    response = client.get('/users/test@example.com')
    assert response.status_code == 200
    assert response.json()['email'] == 'test@example.com'