"""
Authorization Router
"""

from src.utils.base.libraries import (
    Jinja2Templates,
    JSONResponse,
    APIRouter,
    Request,
    status,
    Depends,
    Session
)
from src.utils.models import BaseUser, Error
from src.database import get_db
from src.authentication import create_new_user

# Load templates
templates = Jinja2Templates(directory="templates")


# Router
router = APIRouter()

# - Login User
# - Logout User

# Register User - Create a new user in the database
@router.post("/", response_class=JSONResponse, tags=["Authorization"], summary="Register User")
def register_user(request: Request, user: BaseUser, session: Session=Depends(get_db)) -> JSONResponse:
    """
    This endpoint is used to register a user
    param: request: Request: Request object
    param: user: BaseUser: User object
    param: session: Session: Database session
    return: JSONResponse: JSON response
    """
    try:
        user_creation_status = create_new_user(session=session, user=user)
        if isinstance(user_creation_status, Error):
            return JSONResponse(
                content=user_creation_status.model_dump(),
                status_code=user_creation_status.status_code
            )
        return JSONResponse(
            content={"message": user_creation_status},
            status_code=status.HTTP_201_CREATED
        )

    except Exception as e:
        return JSONResponse(
            content={"message": "Internal Server Error", "error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
