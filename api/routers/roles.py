"""
User Roles Router for /role endpoints

Each role has a bunch of permissions associated with it

Available Tables:
    - Roles
    - Permissions
    - User_Roles
    - Role_Permissions

Explanation:

Roles:
    - Role is linked with User_Roles where each user can have multiple roles
    - Role is linked with Role_Permissions where each role can have multiple permissions
    - A role can have multiple permissions associated with it
    - A permission can be associated with multiple roles

Permissions:
    - Permission is linked with Role_Permissions where each permission can be associated with multiple roles
    - A permission can be associated with multiple roles
    - A role can have multiple permissions associated with it

User_Roles:
    - User_Roles is linked with Roles where each user can have multiple roles
    - A user can have multiple roles associated with it
    - A role can be associated with multiple users

Role_Permissions:
    - Role_Permissions is linked with Roles where each role can have multiple permissions
    - A role can have multiple permissions associated with it
    - A permission can be associated with multiple roles
"""

from src.utils.base.libraries import (
    JSONResponse,
    APIRouter,
    Request,
    status,
    Depends,
    Session
)
from src.utils.models import Error
from src.database import get_db
from src.main import get_current_user_id

# Router
router = APIRouter()


# - 