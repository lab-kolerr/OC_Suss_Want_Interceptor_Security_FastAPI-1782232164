import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_create_user():
    response = await client.post('/users/', json={'email': 'test@example.com', 'password': 'strongpassword'})
    assert response.status_code == 200
    assert response.json()['email'] == 'test@example.com'