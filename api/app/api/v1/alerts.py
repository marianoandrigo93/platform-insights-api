from fastapi import APIRouter

from app.schemas.alert import AlertResponse
from app.services.platform_service import platform_service

router = APIRouter(prefix="/api/v1/alerts", tags=["Alerts"])


@router.get(
    "",
    response_model=list[AlertResponse],
    summary="Listar alertas",
    description="Devuelve las alertas operacionales activas o reconocidas.",
)
def list_alerts() -> list[AlertResponse]:
    return platform_service.get_alerts()