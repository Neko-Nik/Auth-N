"""
This module is the entry point for the database package.
"""

from .connection import get_db, init_db

__version__ = "v1.0.0-phoenix-release"


__annotations__ = {
    "version": __version__,
    "get_db": "Function to get the database session",
    "init_db": "Function to initialize the database"
}


__all__ = [
    "get_db",
    "init_db"
]
