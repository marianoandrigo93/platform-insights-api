from pydantic import BaseModel


class DeploymentResponse(BaseModel):
    id: str
    service_id: str
    version: str
    environment: str
    status: str
    deployed_at: str
    deployed_by: str