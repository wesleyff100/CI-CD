import pytest
from fastapi.testclient import TestClient
from main import app
from datetime import datetime

client = TestClient(app)

def test_root_status_code():
    response = client.get("/")
    assert response.status_code == 200

def test_root_message():
    response = client.get("/")
    data = response.json()
    assert "message" in data
    assert data["message"] == "Hello World"

def test_root_timestamp_exists():
    response = client.get("/")
    data = response.json()
    assert "timestamp" in data

def test_root_timestamp_format():
    response = client.get("/")
    data = response.json()
    timestamp = data.get("timestamp")
    try:
        datetime.fromisoformat(timestamp)
    except (ValueError, TypeError):
        pytest.fail("Timestamp is not in ISO format")

def test_root_method_not_allowed():
    response = client.post("/")
    assert response.status_code == 405

    # Check if timestamp is ISO format
    from datetime import datetime
    try:
        datetime.fromisoformat(data["timestamp"])
    except ValueError:
        pytest.fail("Timestamp is not in ISO format")
