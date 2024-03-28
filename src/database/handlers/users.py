"""
Handles all the database operations related to users
"""


from src.utils.base.libraries import Session
from src.utils.models import User, BaseUser


def get_user_by_username(db: Session, username: str) -> User:
    """
    Get a user by their username
    """
    return db.query(User).filter(User.username == username).first()


def create_user(db: Session, user: BaseUser) -> None:
    """
    Create a new user in the database
    """
    db_user = User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return

