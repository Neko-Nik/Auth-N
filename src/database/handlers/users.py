"""
Handles all the database operations related to users
"""

from src.utils.base.libraries import Session
from src.utils.base.constants import DB_ERROR_MESSAGES
from src.utils.models import User, BaseUser, Error
from typing import Union


def check_user_status(user: User) -> Union[User, Error]:
    """
    Check the status of the user
    """
    match user:
        case None:
            return Error(**DB_ERROR_MESSAGES["user_not_found"])
        case user if not user.is_active:
            return Error(**DB_ERROR_MESSAGES["user_inactive"])
        case user if user.is_locked:
            return Error(**DB_ERROR_MESSAGES["user_locked"])
    
    return user


def get_user_by_username(db: Session, username: str) -> User | Error:
    """
    Get a user by their username
    """
    return check_user_status(user=db.query(User).filter(User.username == username).first())


def get_user_by_user_id(db: Session, user_id: str) -> Union[User, Error]:
    """
    Get a user by their user_id
    """
    return check_user_status(user=db.query(User).filter(User.user_id == user_id).first())


def create_user(db: Session, user: BaseUser) -> None:
    """
    Create a new user in the database
    """
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return None
