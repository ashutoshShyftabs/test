# test_your_fastapi_app.py
from fastapi.testclient import TestClient
from src.main import app
import pytest


client = TestClient(app)


@pytest.mark.e2e
def test_api_integrations():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "OK", "version": "CONFIG.BUILD_TAG"}
