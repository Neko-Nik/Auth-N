"""
Authentication related functions for creating and managing users
"""

from src.utils.base.libraries import (
    Session,
    base64,
    bcrypt,
    hashlib,
    datetime,
    timedelta,
    timezone,
    jwt
)
from src.utils.models import BaseUser, Error
from src.database import create_user, get_user_by_username
from src.utils.base.constants import JWT_TOKEN_KEY, DB_ERROR_MESSAGES


def create_new_user(session: Session, user: BaseUser) -> Error | str:
    """
    Create a new user in the database
    param: session: Session: Database session
    param: user: BaseUser: User object
    return: Error | str (Success message)
    """
    # If user already exists, return an error
    if get_user_by_username(db=session, username=user.username):
        return Error(**DB_ERROR_MESSAGES["user_already_exists"])

    # Password hash is base64 encoded from the frontend
    base64_password_hash = user.password_hash

    # Decode the base64 encoded password hash
    decoded_password_hash: bytes = base64.b64decode(s=base64_password_hash)

    # Generate a salt
    salt: bytes = bcrypt.gensalt()

    # Hash the password with the generated salt
    hashed_password: bytes = bcrypt.hashpw(password=decoded_password_hash, salt=salt)

    # Store the salt and hashed password in the user object
    user.password_salt = salt.decode(encoding="utf-8")
    user.password_hash = hashed_password.decode(encoding="utf-8")

    # Generate unique user ID for the user using the username
    user.user_id = hashlib.sha256(user.username.encode(encoding="utf-8")).hexdigest()

    # If user does not exist, create a new user
    create_user(db=session, user=user)
    return "User created successfully"


def generate_access_token(session: Session, username: str, password: str) -> str | Error:
    """
    Generate an access token for the user
    Operation Steps:
        - Verify the user credentials
        - Check if the user is present in the database
        - Check if the user is active
        - Check if the user is locked
        - Verify the password
        - Generate the JWT token for the user
    param: session: Session: Database session
    param: username: str: Username
    param: password: str: Password
    return: str: Access token | Error
    """
    # Verify the user credentials
    user = get_user_by_username(db=session, username=username)
    if isinstance(user, Error):
        return user

    # Verify the password
    salt = user.password_salt.encode(encoding="utf-8")  # Convert the salt to bytes
    hashed_password = bcrypt.hashpw(password=password.encode(encoding="utf-8"), salt=salt)  # Hash the password

    if hashed_password != user.password_hash.encode(encoding="utf-8"):  # Compare the hashed password
        return Error(**DB_ERROR_MESSAGES["incorrect_password"]) # Return an error if the password is incorrect

    # Generate the JWT token for the user
    return jwt.encode(key=JWT_TOKEN_KEY, algorithm="HS512",
        payload={
            "exp": datetime.now(timezone.utc) + timedelta(days=1),
            "exp_seconds": timedelta(days=1).total_seconds(),
            "user_id": user.user_id
        }
    )
