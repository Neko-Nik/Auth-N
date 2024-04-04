"""
All the dependencies are defined here
"""

from src.utils.base.libraries import (
    OAuth2PasswordBearer,
    Annotated,
    Depends,
    jwt
)
from src.utils.base.constants import JWT_TOKEN_KEY, DEPENDENCY_ERROR_MESSAGES
from src.utils.models import Error


reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"user/login/access-token")
TokenDep = Annotated[str, Depends(reusable_oauth2)]


def get_current_user_id(token: TokenDep) -> dict | Error:
    try:
        return jwt.decode(jwt=token, key=JWT_TOKEN_KEY, algorithms=["HS512"], verify=True)["user_id"]
    except jwt.ExpiredSignatureError:
        return Error(**DEPENDENCY_ERROR_MESSAGES["token_expired"])
    except jwt.InvalidTokenError:
        return Error(**DEPENDENCY_ERROR_MESSAGES["invalid_token"])
    except Exception as e:
        return Error(message="Internal Server Error", error=str(e), status_code=500)
