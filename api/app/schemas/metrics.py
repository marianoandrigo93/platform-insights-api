from pydantic import BaseModel


class MetricsSummaryResponse(BaseModel):
    total_services: int
    healthy_services: int
    degraded_services: int
    active_alerts: int
    deployments_today: int
    average_availability: float
    average_latency_ms: int