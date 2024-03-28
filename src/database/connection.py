"""
This file contains the database connection and session creation functions
"""

from src.utils.base.libraries import create_engine, sessionmaker
from src.utils.models import Base
from .events import handle_failed_login_attempts


# For SQLite local database
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
engine = create_engine(url=SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# For Postgres
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"
# engine = create_engine(url=SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db():
    """
    Function to initialize the database
    """
    Base.metadata.create_all(bind=engine, checkfirst=True)


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
