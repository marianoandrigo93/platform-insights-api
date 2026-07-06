SERVICES = [
    {
        "id": "payments-api",
        "name": "Payments API",
        "environment": "production",
        "status": "healthy",
        "version": "2.4.1",
        "replicas": 8,
        "availability": 99.98,
        "latency_ms": 42,
    },
    {
        "id": "orders-api",
        "name": "Orders API",
        "environment": "production",
        "status": "degraded",
        "version": "1.18.0",
        "replicas": 4,
        "availability": 99.72,
        "latency_ms": 120,
    },
    {
        "id": "platform-workers",
        "name": "Platform Workers",
        "environment": "production",
        "status": "healthy",
        "version": "3.1.5",
        "replicas": 6,
        "availability": 99.95,
        "latency_ms": 55,
    },
]

DEPLOYMENTS = [
    {
        "id": "dep-001",
        "service_id": "payments-api",
        "version": "2.4.1",
        "environment": "production",
        "status": "succeeded",
        "deployed_at": "2026-07-05T13:30:00Z",
        "deployed_by": "platform-team",
    },
    {
        "id": "dep-002",
        "service_id": "orders-api",
        "version": "1.18.0",
        "environment": "production",
        "status": "succeeded",
        "deployed_at": "2026-07-05T11:10:00Z",
        "deployed_by": "orders-team",
    },
]

ALERTS = [
    {
        "id": "alert-001",
        "service_id": "orders-api",
        "severity": "high",
        "status": "open",
        "message": "Latency above threshold",
        "created_at": "2026-07-05T14:05:00Z",
    },
    {
        "id": "alert-002",
        "service_id": "payments-api",
        "severity": "medium",
        "status": "acknowledged",
        "message": "CPU usage above 70%",
        "created_at": "2026-07-05T14:20:00Z",
    },
]

METRICS_SUMMARY = {
    "total_services": 3,
    "healthy_services": 2,
    "degraded_services": 1,
    "active_alerts": 2,
    "deployments_today": 2,
    "average_availability": 99.88,
    "average_latency_ms": 72,
}