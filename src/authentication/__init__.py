"""
All the models used in the project are defined here.
"""

from .users import create_new_user, generate_access_token, update_user_metadata


__version__ = "v1.0.0-phoenix-release"


__annotations__ = {
    "version": __version__,
    "create_new_user": "Create a new user in the database",
    "generate_access_token": "Generate an access token for the user",
    "update_user_metadata": "Update the metadata of the user with the new metadata"
}


__all__ = [
    "create_new_user",
    "generate_access_token",
    "update_user_metadata"
]
