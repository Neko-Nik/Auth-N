"""
All the models used in the project are defined here.
"""

from .generic import All_Exceptions
from .database import (
    User,
    Role,
    Permission,
    UserRoles,
    RolePermissions,
    LoginAttempt,
    AuditLog,
    Session,
    JWTToken,
    APIKey,
    PasswordResetToken,
    IPRestriction,
    CSRFToken,
    OTPToken,
    Device,
    Base
)


__version__ = "v1.0.0-phoenix-release"


__annotations__ = {
    "version": __version__,
    "All_Exceptions": "Class for handling wrong input exceptions",
    "User": "User model",
    "Role": "Role model",
    "Permission": "Permission model",
    "UserRoles": "UserRoles model",
    "RolePermissions": "RolePermissions model",
    "LoginAttempt": "LoginAttempt model",
    "AuditLog": "AuditLog model",
    "Session": "Session model",
    "JWTToken": "JWTToken model",
    "APIKey": "APIKey model",
    "PasswordResetToken": "Password Reset Token model",
    "IPRestriction": "IPRestriction model",
    "CSRFToken": "CSRFToken model",
    "OTPToken": "OTPToken model",
    "Device": "Device model",
    "Base": "Declarative base for the database models"
}


__all__ = [
    "All_Exceptions",
    "User",
    "Role",
    "Permission",
    "UserRoles",
    "RolePermissions",
    "LoginAttempt",
    "AuditLog",
    "Session",
    "JWTToken",
    "APIKey",
    "PasswordResetToken",
    "IPRestriction",
    "CSRFToken",
    "OTPToken",
    "Device",
    "Base"
]
