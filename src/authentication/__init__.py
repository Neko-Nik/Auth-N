"""
All the models used in the project are defined here.
"""

from .users import create_new_user


__version__ = "v1.0.0-phoenix-release"


__annotations__ = {
    "version": __version__,
    "create_new_user": "Create a new user in the database"
}


__all__ = [
    "create_new_user"
]
