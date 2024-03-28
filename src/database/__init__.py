"""
This module is the entry point for the database package.
"""

from .connection import get_db, init_db
from .handlers.users import get_user_by_username, create_user

__version__ = "v1.0.0-phoenix-release"


__annotations__ = {
    "version": __version__,
    "get_db": "Function to get the database session",
    "init_db": "Function to initialize the database",
    "get_user_by_username": "Get a user by their username",
    "create_user": "Create a new user in the database and return the user"
}


__all__ = [
    "get_user_by_username",
    "create_user",
    "get_db",
    "init_db"
]
