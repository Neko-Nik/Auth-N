"""
User Authentication Router for /authorize endpoint
"""

from src.utils.base.libraries import (
    RedirectResponse,
    Jinja2Templates,
    HTMLResponse,
    JSONResponse,
    APIRouter,
    Request,
    status,
    Depends,
    Session
)
from src.utils.models import BaseUser, Error, AuthorizationLogin
from src.database import get_db, get_user_by_username
from src.authentication import generate_authorization_code, verify_user_credentials


# Load templates
templates = Jinja2Templates(directory="templates")

# Router
router = APIRouter()


#   response_type=code
#   &client_id=4SCTFJEUJIXysLFHU528WEzF
#   &redirect_uri=https://www.oauth.com/playground/authorization-code.html
#   &scope=photo+offline_access
#   &state=vhxTkyFntgKGPmUv

# Authorization Code Flow
@router.get("/authorization-code", response_class=HTMLResponse, tags=["Authorization"], summary="Authorize a user with redirect URI")
def register_user(request: Request, client_id: str, redirect_uri: str, scope: str, state: str, response_type: str="code", session: Session=Depends(get_db)) -> HTMLResponse:
    """
    This endpoint is used to authorize a user
    param: request: Request: Request object
    param: client_id: str: Client ID
    param: redirect_uri: str: Redirect URI
    param: scope: str: Scope
    param: state: str: State
    param: response_type: str: Response type
    param: session: Session: Database session
    return: HTMLResponse: HTML response
    """
    try:
        data = {
            "request": request,
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "scope": scope,
            "state": state,
            "response_type": response_type
        }
        return templates.TemplateResponse(name="authorize.html", context=data)
    except Exception as e:
        return JSONResponse(
            content={"message": "Internal Server Error", "error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Authorization Login Flow
@router.post("/login", response_class=RedirectResponse, tags=["Authorization"], summary="Login a user with redirect URI")
async def auth_login_from_ui(request: Request, data: AuthorizationLogin, session: Session=Depends(get_db)) -> RedirectResponse:
    """
    This endpoint is used to login a user
    param: request: Request: Request object
    param: data: AuthorizationLogin: Authorization login object
    param: session: Session: Database session
    return: RedirectResponse: Redirect response
    """
    try:
        # TODO: Check if the client ID is valid
        user_exists = get_user_by_username(db=session, username=data.username)
        if isinstance(user_exists, Error):
            return JSONResponse(
                content={"message": user_exists.message},
                status_code=user_exists.status_code
            )

        print(f"Data: {data}")
        if not verify_user_credentials(session=session, user=user_exists, password=data.password):
            return JSONResponse(
                content={"message": "Invalid credentials"},
                status_code=status.HTTP_401_UNAUTHORIZED
            )

        # Generate authorization code and save it in the database
        auth_code: str = generate_authorization_code(user=user_exists)
        if isinstance(auth_code, Error):
            return JSONResponse(
                content={"message": auth_code.message},
                status_code=auth_code.status_code
            )

        return JSONResponse(
            content={
                "message": "Authorization code generated successfully",
                "redirect_uri": f"{data.redirect_uri}?code={auth_code}&state={data.state}"
            }
        )
    except Exception as e:
        return JSONResponse(
            content={"message": "Internal Server Error", "error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Authorization Token Access Flow
@router.post("/token", response_class=JSONResponse, tags=["Authorization"], summary="Get access token with authorization code")
async def get_access_token(request: Request, client_id: str, client_secret: str, code: str, redirect_uri: str, grant_type: str="authorization_code", session: Session=Depends(get_db)) -> JSONResponse:
    """
    This endpoint is used to get the access token
    param: request: Request: Request object
    param: client_id: str: Client ID
    param: client_secret: str: Client secret
    param: code: str: Authorization code
    param: redirect_uri: str: Redirect URI
    param: grant_type: str: Grant type
    param: session: Session: Database session
    return: JSONResponse: JSON response
    """
    try:
        # TODO: Check if the client ID and secret are valid
        # Check if the authorization code is valid (Simple JWT token verification)
        # Generate an access token for the user
        # Return the access token
        pass
    except Exception as e:
        return JSONResponse(
            content={"message": "Internal Server Error", "error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
