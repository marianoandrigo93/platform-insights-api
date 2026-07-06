from pydantic import BaseModel


class AlertResponse(BaseModel):
    id: str
    service_id: str
    severity: str
    status: str
    message: str
    created_at: str