#### `app/main.py`
```python
from fastapi import FastAPI
from app.routes.transcribe import transcribe_router
from app.utils.logger import setup_logger
from app.config.settings import settings

# Initialize application
app = FastAPI(title="ASR Service", version="1.0.0")

# Setup logger
logger = setup_logger()

# Include routes
app.include_router(transcribe_router, prefix="/transcribe", tags=["Transcription"])

@app.on_event("startup")
async def startup_event():
    logger.info("ASR Service is starting...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("ASR Service is shutting down...")
```