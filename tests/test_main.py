# tests/test_main.py
from fastapi.testclient import TestClient

# import pytest

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from app.database import Base, engine
from src.main import app

# Use an in-memory SQLite database for testing
# TESTING_DATABASE_URL = "sqlite:///:memory:"
# engine = create_engine(TESTING_DATABASE_URL)
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base.metadata.create_all(bind=engine)

# # Override the database dependency for testing
# app.dependency_overrides[get_db] = get_testing_db

# def get_testing_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# Actual tests
def test_read_item():
    with TestClient(app) as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "OK", "version": "CONFIG.BUILD_TAG"}
