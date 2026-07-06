from fastapi import APIRouter

from app.schemas.deployment import DeploymentResponse
from app.services.platform_service import platform_service

router = APIRouter(prefix="/api/v1/deployments", tags=["Deployments"])


@router.get(
    "",
    response_model=list[DeploymentResponse],
    summary="Listar despliegues",
    description="Devuelve eventos recientes de despliegue de servicios.",
)
def list_deployments() -> list[DeploymentResponse]:
    return platform_service.get_deployments()