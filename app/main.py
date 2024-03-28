"""
This is the main app file which contains all the endpoints of the API
This file is used to run the API
"""

from src.utils.base.libraries import (
    CORSMiddleware,
    JSONResponse,
    FastAPI,
    Request,
    uvicorn
)
from .routers import logs_router
from src.utils.models import All_Exceptions
from src.database import init_db


# Initialization
app = FastAPI(
    title="Auth N",
    description="This is the API for Authentication and Authorization",
    version="1.0.0",
    # docs_url=None,
    # redoc_url=None,
    docs_url="/docs",
    redoc_url="/redoc",
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


if __name__ == '__main__':
    # reload=True - server will automatically restart after code changes
    uvicorn.run('app:app', host='0.0.0.0', port=8086, reload=True)
