"""
Logs of API are stored in a file and can be viewed in a web page
Use the password "neko-nik" to view the logs
"""

from src.utils.base.libraries import (
    Jinja2Templates,
    JSONResponse,
    HTMLResponse,
    APIRouter,
    Request,
    status,
    json
)
from src.utils.base.constants import NUMBER_OF_LOGS_TO_DISPLAY, LOG_FILE_PATH


# Load templates
templates = Jinja2Templates(directory="templates")


# Router
router = APIRouter()


# Logs of API
@router.get("/logs", response_class=HTMLResponse, tags=["Logs"], summary="Logs of API")
def view_logs(request: Request, passwd: str="") -> HTMLResponse:
    """
    This endpoint is used to view the logs of the API in a web page
    Just go to /logs to view the logs
    """
    if passwd != "neko-nik":
        return JSONResponse(
            content={"detail": "Not Found"},
            status_code=status.HTTP_404_NOT_FOUND
        )

    logs = []
    with open(LOG_FILE_PATH, 'r') as file:
        for line in file:
            try:
                log_entry = json.loads(line)
                logs.append(log_entry)
            except json.JSONDecodeError:
                pass

    logs.reverse()  # To show the latest logs first

    # To show only the latest 100 logs
    logs = logs[:NUMBER_OF_LOGS_TO_DISPLAY]
    response = {"request": request, "logs": logs}

    return templates.TemplateResponse("logs.html", response)
