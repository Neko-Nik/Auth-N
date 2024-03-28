"""
This file contains Global constants
Also storing all the env and config variables here
"""

from src.utils.base.libraries import os, status

# environment variables
POSTGRES_DB_USERNAME = os.environ.get("POSTGRES_DB_USERNAME", "postgres")
POSTGRES_DB_PASSWORD = os.environ.get("POSTGRES_DB_PASSWORD", "postgres")
POSTGRES_DB_HOST = os.environ.get("POSTGRES_DB_HOST", "0.0.0.0")
POSTGRES_DB_PORT = os.environ.get("POSTGRES_DB_PORT", "5432")
POSTGRES_DB_DATABASE = os.environ.get("POSTGRES_DB_DATABASE", "postgres")
JWT_TOKEN_KEY = os.environ.get("JWT_TOKEN_KEY", "86nekonik7f21f32d94564b26e0edf48fed32d9059af807e89b3260d4eeca67619ec60b156521bc4b")


## log variables
# TODO: Uncomment the below lines in production
# LOG_LEVEL = int(os.environ.get("LOG_LEVEL", 20))
# LOG_FILE_PATH = "/var/log/api/logs.jsonl"
LOG_LEVEL = 10
LOG_FILE_PATH = "logs/logs.jsonl"
NUMBER_OF_LOGS_TO_DISPLAY = int(os.environ.get("NUMBER_OF_LOGS_TO_DISPLAY", 100))


# Database error messages
DB_ERROR_MESSAGES = {
    "user_not_found": {
        "message": "User not found",
        "status_code": status.HTTP_404_NOT_FOUND,
        "info": {
            "note": "Please register before logging in",
            "source": "While generating an access token"
        }
    },
    "user_inactive": {
        "message": "User is inactive",
        "status_code": status.HTTP_403_FORBIDDEN,
        "info": {
            "note": "Please contact the administrator to activate your account",
            "source": "While generating an access token"
        }
    },
    "user_locked": {
        "message": "User is locked",
        "status_code": status.HTTP_403_FORBIDDEN,
        "info": {
            "note": "Please contact the administrator to unlock your account",
            "source": "While generating an access token"
        }
    },
    "incorrect_password": {
        "message": "Incorrect password",
        "status_code": status.HTTP_401_UNAUTHORIZED,
        "info": {
            "note": "Please check the password and try again",
            "source": "While generating an access token"
        }
    },
    "user_already_exists": {
        "message": "User already exists",
        "status_code": status.HTTP_409_CONFLICT,
        "info": {
            "note": "Please try logging in instead or use a different username to register",
            "source": "While creating a new user in the database"
        }
    }
}