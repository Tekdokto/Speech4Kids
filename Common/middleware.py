## middleware.py
This module contains middleware for shared functionalities, such as error handling, request validation, and CORS.

# common/middleware.py
from fastapi import Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

async def add_cors_middleware(app):
    """
    Adds CORS support to the FastAPI application.
    
    Args:
        app: The FastAPI application instance.
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Update with production origins
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def handle_http_exceptions(request: Request, exc):
    """
    Custom HTTP exception handler for returning JSON responses.

    Args:
        request (Request): Incoming request object.
        exc: Raised exception.

    Returns:
        JSONResponse: Error response.
    """
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

def add_global_error_handlers(app):
    """
    Adds global error handlers to the FastAPI app.

    Args:
        app: The FastAPI application instance.
    """
    from fastapi.exceptions import RequestValidationError
    from starlette.exceptions import HTTPException as StarletteHTTPException

    app.add_exception_handler(RequestValidationError, handle_http_exceptions)
    app.add_exception_handler(StarletteHTTPException, handle_http_exceptions)