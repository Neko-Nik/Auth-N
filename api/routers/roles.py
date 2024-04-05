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

More information can be found at https://auth-n.nekonik.com/docs/Contribute/db-concepts/user-roles-and-permissions
Reference:
    - https://www.keycloak.org/docs/latest/server_admin/index.html
    - https://stackoverflow.com/questions/27726066/jwt-refresh-token-flow
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


"""
There will be system defined roles and permissions for this API to work
- System defined roles:
    - Super Admin (Super User) - Can do anything only one user can have this role (system defined) [will be created by the system]
- System defined permissions:
    - Super Admin Permissions:
        - Can do anything

Super Admin can create another user where the user can have limited permissions can be treated as an admin 
if required the super admin can create another super admin as well
The only part where the super admin can't do anything is the super admin can't delete itself and can't change its own permissions (can't remove super admin permissions)
"""

# Anything that is created by the system can't be deleted or modified in any way
# These are the default permissions that will be created by the system
"""
Used to do some basic operations on the roles and permissions
| Roles | Permissions | User_Roles | Role_Permissions |

"""
default_auth_permissions = {
    # Users
    "read_all_users": "Read all the users in the system",
    "create_user": "Create a new user",
    "update_user": "Update any existing user in the system",
    "delete_user": "Delete user from the system",

    # Roles
    "read_all_roles": "Read all the roles in the system",
    "create_role": "Create a new role",
    "update_role": "Update any existing role in the system",
    "delete_role": "Delete role from the system",

    # Permissions
    "read_all_permissions": "Read all the permissions in the system",
    "create_permission": "Create a new permission",
    "update_permission": "Update any existing permission in the system",
    "delete_permission": "Delete permission from the system",

    # Assign Roles to Users
    "assign_role_to_user": "Assign role to a user",
    "remove_role_from_user": "Remove role from a user",
    "read_all_relationships_between_users_and_roles": "Read all the relationships between users and roles",

    # Assign Permissions to Role
    "assign_permissions_to_role": "Assign permissions to a role",
    "remove_permissions_from_role": "Remove permissions from a role",
    "read_all_relationships_between_role_and_permissions": "Read all the relationships between role and permissions",

    # Miscellaneous
    "read_all_logs": "Read all the logs in the system",
    "read_all_audit_logs": "Read all the audit logs in the system",
    "read_all_system_logs": "Read all the system logs in the system",
    "read_all_security_logs": "Read all the security logs in the system, which includes login attempts, etc.",

    # System
    "read_system_info": "Read system information",
    
    "read_all_sessions": "Read all the users sessions in the system including the device information",
    "manage_all_sessions": "Manage all the users sessions with the device information in the system, including deleting the sessions",
    
    "read_all_jwt_tokens": "Read all the JWT refresh tokens in the system",
    "create_any_jwt_token": "Create any JWT refresh token for any user in the system",
    "manage_all_jwt_tokens": "Manage all the JWT refresh tokens in the system, including deleting the tokens",
    
    "read_all_api_keys": "Read all the API keys in the system",
    "create_any_api_key": "Create any API key for any user in the system",
    "manage_all_api_keys": "Manage all the API keys in the system, like extending the expiry, deleting the keys, etc.",
    
    "read_all_ip_restrictions": "Read all the IP restrictions in the system (if any)",
    "create_any_ip_restriction": "Create any IP restriction for any user in the system",
    "manage_all_ip_restrictions": "Manage all the IP restrictions in the system, like editing restrictions, deleting the restrictions, etc."
}
