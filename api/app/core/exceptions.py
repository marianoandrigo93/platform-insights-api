from fastapi import Request
from fastapi.responses import JSONResponse


class ResourceNotFoundException(Exception):
    def __init__(self, resource: str, resource_id: str):
        self.resource = resource
        self.resource_id = resource_id


async def resource_not_found_handler(
    request: Request,
    exc: ResourceNotFoundException,
) -> JSONResponse:
    return JSONResponse(
        status_code=404,
        content={
            "error": {
                "code": 404,
                "message": f"{exc.resource} '{exc.resource_id}' not found",
            }
        },
    )