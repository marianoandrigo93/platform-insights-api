from fastapi import APIRouter

from app.core.exceptions import ResourceNotFoundException
from app.schemas.service import ServiceResponse
from app.services.platform_service import platform_service

router = APIRouter(prefix="/api/v1/services", tags=["Services"])


@router.get(
    "",
    response_model=list[ServiceResponse],
    summary="Listar servicios",
    description="Devuelve el estado operacional de los servicios monitoreados.",
)
def list_services() -> list[ServiceResponse]:
    return platform_service.get_services()


@router.get(
    "/{service_id}",
    response_model=ServiceResponse,
    summary="Obtener detalle de servicio",
    description="Devuelve el detalle operacional de un servicio específico.",
)
def get_service(service_id: str) -> ServiceResponse:
    service = platform_service.get_service_by_id(service_id)

    if service is None:
        raise ResourceNotFoundException("Service", service_id)

    return service