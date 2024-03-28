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
    Session,
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm
)
from src.utils.models import BaseUser, Error
from src.database import get_db
from src.authentication import create_new_user, generate_access_token

# Load templates
templates = Jinja2Templates(directory="templates")


# Router
router = APIRouter()

# - Login User
# - Logout User

# Register User - Create a new user in the database
@router.post("/register", response_class=JSONResponse, tags=["Authorization"], summary="Register User")
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

# Login User - Login an existing user
@router.post("/login/access-token", response_class=JSONResponse, tags=["Authentication"], summary="Login and generate a new JWT token")
def login_access_token(request: Request, session: Session=Depends(get_db), form_data: OAuth2PasswordRequestForm=Depends()) -> JSONResponse:
    """
    This endpoint is used to generate a new JWT token for the user to access the application
    param: grant_type: str: Grant type
    param: username: str: Username
    param: password: str: Password
    param: scope: str: Scope of the token
    param: client_id: str: Client ID for the token
    param: client_secret: str: Client secret for the token
    return: JSONResponse: JSON response of Access Token and Token Type
    """
    try:
        access_token = generate_access_token(session=session, username=form_data.username, password=form_data.password)
        if isinstance(access_token, Error):
            return JSONResponse(
                content=access_token.model_dump(),
                status_code=access_token.status_code
            )
        return JSONResponse(
            content={"access_token": access_token, "token_type": "bearer"},
            status_code=status.HTTP_200_OK
        )

    except Exception as e:
        return JSONResponse(
            content={"message": "Internal Server Error", "error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
