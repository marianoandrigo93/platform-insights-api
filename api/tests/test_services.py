def test_get_services(client):
    response = client.get("/api/v1/services")

    assert response.status_code == 200

    services = response.json()

    assert isinstance(services, list)
    assert len(services) == 3


def test_get_existing_service(client):
    response = client.get("/api/v1/services/payments-api")

    assert response.status_code == 200

    service = response.json()

    assert service["id"] == "payments-api"
    assert service["name"] == "Payments API"
    assert service["status"] == "healthy"


def test_service_not_found(client):
    response = client.get("/api/v1/services/no-existe")

    assert response.status_code == 404

    error = response.json()

    assert error["error"]["code"] == 404
    assert error["error"]["message"] == "Service 'no-existe' not found"