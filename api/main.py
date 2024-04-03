"""
This is the main app file which contains all the endpoints of the API
This file is used to run the API
"""

from src.utils.base.libraries import (
    get_swagger_ui_html,
    get_redoc_html,
    CORSMiddleware,
    JSONResponse,
    FastAPI,
    Request,
    uvicorn
)
from .routers import logs_router, users_router
from src.utils.models import All_Exceptions
from src.database import init_db


# Initialization
app = FastAPI(
    title="Auth N",
    description="This is the API for Authentication and Authorization",
    version="1.0.0",
    docs_url=None,
    redoc_url=None,
    include_in_schema=True,
)
init_db()

# Add CROCS middle ware to allow cross origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Exception handler for wrong input
@app.exception_handler(All_Exceptions)
async def input_data_exception_handler(request: Request, exc: All_Exceptions):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"Oops! {exc.message}"}
    )


#    Endpoints    #
app.include_router(router=logs_router)
app.include_router(router=users_router, prefix="/user")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html(request: Request):
    return get_swagger_ui_html(openapi_url="/openapi.json", title="Auth N - API", swagger_favicon_url="https://auth-n.nekonik.com/img/favicon.svg")

@app.get("/redoc", include_in_schema=False)
async def redoc_html(request: Request):
    return get_redoc_html(openapi_url="/openapi.json", title="Auth N - ReDocs", redoc_favicon_url="https://auth-n.nekonik.com/img/favicon.svg")
