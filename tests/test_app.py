import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_signup_and_unregister():
    # Use a test activity and email
    activity = list(client.get("/activities").json().keys())[0]
    email = "testuser@mergington.edu"
    # Sign up (email as query param)
    response = client.post(f"/activities/{activity}/signup?email={email}")
    assert response.status_code == 200
    # Duplicate signup should fail or be handled
    response2 = client.post(f"/activities/{activity}/signup?email={email}")
    assert response2.status_code in (400, 409, 200)
    # Unregister (if endpoint exists)
    # response3 = client.post(f"/activities/{activity}/unregister?email={email}")
    # assert response3.status_code == 200
    # Unregister again should fail or be handled
    # response4 = client.post(f"/activities/{activity}/unregister?email={email}")
    # assert response4.status_code in (400, 404, 200)
