"""
This file has all the necessary libraries for the project to run
any new library should be added here and imported in the respective files
"""

# FastAPI libraries
from fastapi import FastAPI, File, UploadFile , Form, Request, status, Response, Depends, APIRouter
from fastapi.responses import JSONResponse , PlainTextResponse , HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.security import APIKeyHeader
import uvicorn

# Object data modeling libraries
from pydantic import BaseModel, Field, validator


# other libraries
import json
import re
from functools import wraps
from deprecated import deprecated
from datetime import datetime
import subprocess

# read env variables
import os


# Getting some constants from the constants.py file
from src.utils.base.constants import LOG_LEVEL, LOG_FILE_PATH

# Configure logging 
from src.utils.base.log_utils import configure_return_logger
logging = configure_return_logger(LOG_LEVEL=LOG_LEVEL, LOG_FILE_PATH=LOG_FILE_PATH)
