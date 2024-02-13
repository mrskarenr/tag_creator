from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntity

def handler_errors(error:Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntity):
        # enviar para um log
        # enviar um email de notificação
        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors":[{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        )
    return HttpResponse(
        status_code=500,
        body={
            "errors":[{
                "title": "Server Error",
                "detail": str(error)
            }]
        }
    )
