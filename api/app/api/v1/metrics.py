from fastapi import APIRouter

from app.schemas.metrics import MetricsSummaryResponse
from app.services.platform_service import platform_service

router = APIRouter(prefix="/api/v1/metrics", tags=["Metrics"])


@router.get(
    "/summary",
    response_model=MetricsSummaryResponse,
    summary="Resumen de métricas",
    description="Devuelve un resumen agregado de métricas operacionales de la plataforma.",
)
def get_metrics_summary() -> MetricsSummaryResponse:
    return platform_service.get_metrics_summary()