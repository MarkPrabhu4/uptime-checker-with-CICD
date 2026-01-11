from app import app

def test_health_no_url():
    client = app.test_client()
    response = client.post("/health", json={})
    assert response.status_code == 400
