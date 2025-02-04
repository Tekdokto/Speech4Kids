#### `app/main.py`
```python
from fastapi import FastAPI
from app.routes.transcription import transcription_router
from app.routes.websocket import websocket_router
from app.utils.logger import setup_logger
from app.utils.error_handlers import register_error_handlers

# Initialize logger
setup_logger()

# Create FastAPI instance
app = FastAPI(title="Speech4Kids Gateway")

# Register routes
app.include_router(transcription_router, prefix="/transcription", tags=["Transcription"])
app.include_router(websocket_router, prefix="/ws", tags=["WebSocket"])

# Register global error handlers
register_error_handlers(app)

@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "ok"}
```