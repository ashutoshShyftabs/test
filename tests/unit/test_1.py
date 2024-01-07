# test_your_fastapi_app.py
from fastapi.testclient import TestClient
import pytest
from src.main import app

client = TestClient(app)


@pytest.mark.unit
def test_api():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "OK", "version": "CONFIG.BUILD_TAG"}
