from fastapi import FastAPI

from app.api.v1.alerts import router as alerts_router
from app.api.v1.deployments import router as deployments_router
from app.api.v1.health import router as health_router
from app.api.v1.metrics import router as metrics_router
from app.api.v1.services import router as services_router
from app.core.config import settings
from app.core.exceptions import ResourceNotFoundException, resource_not_found_handler


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="API REST para exponer información operacional de infraestructura.",
)

app.add_exception_handler(ResourceNotFoundException, resource_not_found_handler)
app.include_router(health_router)
app.include_router(services_router)
app.include_router(deployments_router)
app.include_router(alerts_router)
app.include_router(metrics_router)