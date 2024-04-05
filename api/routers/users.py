"""
User Authentication Router for /users endpoints

The routers in this file are responsible for handling the users related endpoints

Note that the users list will be based on the permissions of the user
if the user has the hierarchy permission, then the user can see all the users
if not then list only the users under the user's permission

    - `/{user_id}` (GET): Get all users id and username and count
        - Get all users id and username and count
        - Get single user information by user ID
        - Do the pagination
    - `/{user_id}` (PUT): Update user information
        - Update user information by user ID
        - Should also be able to update the hidden fields like is_active, is_email_verified, etc
    - `/{user_id}` (DELETE): Delete user
        - Delete user by user ID and also bulk delete
    - `/import` (POST): Import users from a CSV file / etc and create users
        - Background task to import users from a CSV file
    - `/export` (GET): Export users to a CSV file / etc

Reference: https://auth-n.nekonik.com/docs/category/role-based-access-control
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
from src.utils.models import Error
from src.database import get_db
from src.main import get_current_user_id

# Router
router = APIRouter()

