"""
This file contains Global constants
Also storing all the env and config variables here
"""

from src.utils.base.libraries import os

# environment variables
POSTGRES_DB_USERNAME = os.environ.get("POSTGRES_DB_USERNAME", "postgres")
POSTGRES_DB_PASSWORD = os.environ.get("POSTGRES_DB_PASSWORD", "postgres")
POSTGRES_DB_HOST = os.environ.get("POSTGRES_DB_HOST", "0.0.0.0")
POSTGRES_DB_PORT = os.environ.get("POSTGRES_DB_PORT", "5432")
POSTGRES_DB_DATABASE = os.environ.get("POSTGRES_DB_DATABASE", "postgres")


## log variables
LOG_LEVEL = int(os.environ.get("LOG_LEVEL", 20))
LOG_FILE_PATH = "/var/log/api/logs.jsonl"
# LOG_LEVEL = 10
# LOG_FILE_PATH = "logs/logs.jsonl"
NUMBER_OF_LOGS_TO_DISPLAY = int(os.environ.get("NUMBER_OF_LOGS_TO_DISPLAY", 100))

# Other constants
NEKO_NIK = "Neko Nik"
