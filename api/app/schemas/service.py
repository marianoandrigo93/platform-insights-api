from pydantic import BaseModel


class ServiceResponse(BaseModel):
    id: str
    name: str
    environment: str
    status: str
    version: str
    replicas: int
    availability: float
    latency_ms: int