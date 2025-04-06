from fastapi.testclient import TestClient
from api.routes.course_routes import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

def test_create_course():
    response = client.post("/courses/", json={
        "title": "Intro to AI",
        "description": "A beginner-friendly course on AI fundamentals.",
        "level": "Beginner",
        "tags": ["AI", "ML"]
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Intro to AI"

def test_list_courses():
    response = client.get("/courses/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)