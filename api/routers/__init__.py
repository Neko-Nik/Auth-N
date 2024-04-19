"""
All Routers are imported here and are exposed to the main app file
"""

from .logs import router as logs_router
from .user import router as user_router
from .users import router as users_router
from .authorize import router as authorize_router


__version__ = "v1.0.0-phoenix-release"


__annotations__ = {
    "version": __version__,
    "logs_router": "Logs of API",
    "users_router": "Users of API",
    "user_router": "User of API",
    "authorize_router": "All Authorization from other services"
}


__all__ = [
    "logs_router",
    "user_router",
    "users_router",
    "authorize_router"
]
