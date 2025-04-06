from fastapi.testclient import TestClient
from api.routes.auth_routes import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_login_success():
    response = client.post("/auth/login", json={"email": "test@example.com", "password": "password"})
    assert response.status_code == 200
    assert "access_token" in response.json()

def test_login_failure():
    response = client.post("/auth/login", json={"email": "wrong@example.com", "password": "wrongpass"})
    assert response.status_code == 401
