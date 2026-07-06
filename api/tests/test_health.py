def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "UP"
    assert body["service"] == "Platform Insights API"
    assert body["version"] == "1.0.0"
    assert body["environment"] == "local"