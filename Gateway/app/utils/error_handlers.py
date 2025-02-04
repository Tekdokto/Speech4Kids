#### `app/utils/error_handlers.py`
```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import logging

def register_error_handlers(app: FastAPI):
    logger = logging.getLogger("error_handler")

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled exception: {exc}")
        return JSONResponse(
            status_code=500,
            content={"detail": "An unexpected error occurred. Please try again later."}
        )

    @app.exception_handler(ValueError)
    async def value_error_handler(request: Request, exc: ValueError):
        logger.warning(f"Value error: {exc}")
        return JSONResponse(
            status_code=400,
            content={"detail": str(exc)}
        )
```