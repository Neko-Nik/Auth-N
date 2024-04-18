"""
This module is the entry point for the database package.
"""

from .connection import get_db, init_db
from .handlers.users import get_user_by_username, create_user, get_user_by_user_id, replace_user_metadata
from .handlers.otp import add_new_otp_to_user, validate_otp_and_update_verification_flag

__version__ = "v1.0.0-phoenix-release"


__annotations__ = {
    "version": __version__,
    "get_db": "Function to get the database session",
    "init_db": "Function to initialize the database",
    "get_user_by_username": "Get a user by their username",
    "create_user": "Create a new user in the database and return the user",
    "get_user_by_user_id": "Get a user by their user_id",
    "add_new_otp_to_user": "Add a new OTP to the user",
    "validate_otp_and_update_verification_flag": "Validate the OTP entered by the user and update the email_verified flag",
    "replace_user_metadata": "Update the metadata of the user with the new metadata"
}


__all__ = [
    "get_user_by_username",
    "get_user_by_user_id",
    "create_user",
    "get_db",
    "init_db",
    "add_new_otp_to_user",
    "validate_otp_and_update_verification_flag",
    "replace_user_metadata"
]
