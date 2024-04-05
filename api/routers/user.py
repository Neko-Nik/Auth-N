"""
User Authentication Router for /user endpoints

The routers in this file are responsible for handling the user related endpoints
    - Register User: POST /register - Create a new user in the database
    - Login User JWT: POST /login/access-token - Login an existing user and generate a new JWT token
    - Get User: GET / - Get the user details
    - Update User: PUT / - Update the user details
    - Delete User: DELETE / - Delete the user from the database
    - Verify Email: POST /verify-email - Verify the email of the user
    - Resend Email Verification: POST /resend-verification-email - Resend the email verification link to the user
    - Change Password: PUT /change-password - Change the password of the user using the old password
    - Forgot Password: POST /forgot-password - Send a password reset link to the user email - generates a reset token
    - Reset Password: POST /reset-password - Reset the password of the user using the reset token
    - Logout User: POST /logout - Logout an existing user and invalidate the JWT token
    - Refresh Token: POST /login/refresh-token - Refresh the JWT token for an existing user
    - Generate API Key: POST /api-key - Generate a new API key for the user with the specified permissions
    - Delete API Key: DELETE /api-key - Delete the API key of the user
    - Revoke API Key: PUT /api-key - Revoke the API key of the user, the key will be invalidated and can't be used anymore
    - Get all API Keys: GET /api-keys - Get all the API keys of the user with the specified permissions (hides the secret key)
"""

from src.utils.base.libraries import (
    JSONResponse,
    APIRouter,
    Request,
    status,
    Depends,
    Session,
    OAuth2PasswordRequestForm
)
from src.utils.models import BaseUser, Error
from src.database import get_db, get_user_by_user_id
from src.authentication import create_new_user, generate_access_token
from src.main import get_current_user_id
from src.email import send_verification_email, verify_otp_for_user_email

# Router
router = APIRouter()


# Register User - Create a new user in the database
@router.post("/register", response_class=JSONResponse, tags=["User Authentication"], summary="Register User")
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
@router.post("/login/access-token", response_class=JSONResponse, tags=["User Authentication"], summary="Login and generate a new JWT token")
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


@router.post("/verify-email", response_class=JSONResponse, tags=["User Authentication"], summary="Send a verification email to the user")
def verify_email(request: Request, user_id: dict=Depends(get_current_user_id), session: Session=Depends(get_db)) -> JSONResponse:
    """
    This endpoint is used to send a verification email to the user
    param: request: Request: Request object
    param: session: Session: Database session
    param: token: str: JWT token
    return: JSONResponse: JSON response
    """
    if isinstance(user_id, Error):
        return JSONResponse(
            content=user_id.model_dump(),
            status_code=user_id.status_code
        )
    try:
        verify_email_status = send_verification_email(session=session, user_id=user_id)
        if isinstance(verify_email_status, Error):
            return JSONResponse(
                content=verify_email_status.model_dump(),
                status_code=verify_email_status.status_code
            )
        return JSONResponse(
            content={"message": verify_email_status},
            status_code=status.HTTP_200_OK
        )
    
    except Exception as e:
        return JSONResponse(
            content={"message": "Internal Server Error", "error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@router.put("/verify-email", response_class=JSONResponse, tags=["User Authentication"], summary="Verify the email of the user")
def verify_email(request: Request, otp: str, user_id: dict=Depends(get_current_user_id), session: Session=Depends(get_db)) -> JSONResponse:
    """
    This endpoint is used to verify the email of the user
    param: request: Request: Request object
    param: otp: str: OTP entered by the user
    param: session: Session: Database session
    return: JSONResponse: JSON response
    """
    if isinstance(user_id, Error):
        return JSONResponse(
            content=user_id.model_dump(),
            status_code=user_id.status_code
        )
    try:
        verify_email_status = verify_otp_for_user_email(session=session, user_id=user_id, otp=otp)
        if isinstance(verify_email_status, Error):
            return JSONResponse(
                content=verify_email_status.model_dump(),
                status_code=verify_email_status.status_code
            )
        return JSONResponse(
            content={"message": verify_email_status},
            status_code=status.HTTP_200_OK
        )

    except Exception as e:
        return JSONResponse(
            content={"message": "Internal Server Error", "error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@router.get("/data", response_class=JSONResponse, tags=["User Authentication"], summary="Get the user details")
def get_user(request: Request, user_id: dict=Depends(get_current_user_id), session: Session=Depends(get_db)) -> JSONResponse:
    """
    This endpoint is used to get the details of the user
    param: request: Request: Request object
    param: session: Session: Database session
    return: JSONResponse: JSON response
    """
    if isinstance(user_id, Error):
        return JSONResponse(
            content=user_id.model_dump(),
            status_code=user_id.status_code
        )
    try:
        user = get_user_by_user_id(db=session, user_id=user_id)
        if isinstance(user, Error):
            return JSONResponse(
                content=user.model_dump(),
                status_code=user.status_code
            )
        return JSONResponse(
            content={
                "user_id": user.user_id,
                "username": user.username,
                "email": user.email,
                "phone_number": user.phone_number,
                "profile_picture_url": user.profile_picture_url,
                "roles": [role.role_name for role in user.roles],
                "permissions": [{
                    "permission_name": permission.permission_name,
                    "description": permission.description,
                    "permission_data": permission.permission_data
                } for role in user.roles for permission in role.permissions]
            },
            status_code=status.HTTP_200_OK
        )

    except Exception as e:
        return JSONResponse(
            content={"message": "Internal Server Error", "error": str(e)},
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
