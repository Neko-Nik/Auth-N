"""
This module contains event listeners that are triggered when certain events occur in the database.
"""

from src.utils.base.libraries import listens_for
from src.utils.models import User

# Define an event listener to handle failed login attempts
@listens_for(target=User, identifier='after_update')
def handle_failed_login_attempts(mapper, connection, target: User) -> None:
    if ("failed_login_attempts" in target.__modified__) and (target.failed_login_attempts >= 3):
        target.is_locked = True
