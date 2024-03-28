"""
Authentication related functions for creating and managing users
"""

from src.utils.base.libraries import (
    status,
    Session,
    base64,
    bcrypt
)
from src.utils.models import BaseUser, Error
from src.database import create_user, get_user_by_username


def create_new_user(session: Session, user: BaseUser) -> Error | str:
    """
    Create a new user in the database
    param: session: Session: Database session
    param: user: BaseUser: User object
    return: Error | str (Success message)
    """
    # Password hash is base64 encoded from the frontend
    base64_password_hash = user.password_hash

    # Decode the base64 encoded password hash
    decoded_password_hash = base64.b64decode(base64_password_hash)

    # Generate a salt
    salt = bcrypt.gensalt()

    # Hash the password with the generated salt
    hashed_password = bcrypt.hashpw(decoded_password_hash, salt)

    # Store the salt and hashed password in the user object
    user.password_salt = salt
    user.password_hash = hashed_password

    # If user already exists, return an error
    if get_user_by_username(session, user.username):
        return Error(
            message="User already exists",
            status_code=status.HTTP_409_CONFLICT,
            info={
                "note": "Please try logging in instead or use a different username to register",
                "source": "While creating a new user in the database"
            }
        )

    # If user does not exist, create a new user
    create_user(session, user)
    return "User created successfully"
