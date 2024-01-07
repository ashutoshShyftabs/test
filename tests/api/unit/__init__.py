# test_your_fastapi_app.py
from fastapi.testclient import TestClient
from main import app
from common.config import CONFIG

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "OK", "version": CONFIG.BUILD_TAG}
