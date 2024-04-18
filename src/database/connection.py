"""
This file contains the database connection and session creation functions
"""

from src.utils.base.libraries import create_engine, sessionmaker, event
from src.utils.base.constants import POSTGRES_DB_DATABASE, POSTGRES_DB_HOST, POSTGRES_DB_PASSWORD, POSTGRES_DB_PORT, POSTGRES_DB_USERNAME
from src.utils.models import Base, User
from .events import handle_failed_login_attempts, handle_email_changes


# For SQLite local database
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# For Postgres database (production)
# engine = create_engine(url=f"postgresql://{POSTGRES_DB_USERNAME}:{POSTGRES_DB_PASSWORD}@{POSTGRES_DB_HOST}:{POSTGRES_DB_PORT}/{POSTGRES_DB_DATABASE}")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """
    Function to initialize the database
    """
    Base.metadata.create_all(bind=engine, checkfirst=True)
    # Registering event listeners on specific models
    event.listen(User, "after_insert", handle_failed_login_attempts)
    event.listen(User, "after_insert", handle_email_changes)


def get_db():
    """
    Function to get the database session
    Used in the FastAPI dependency injection system
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
