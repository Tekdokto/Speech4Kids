#### `app/main.py`
```python
from fastapi import FastAPI
from app.routes.tts import tts_router
from app.utils.logger import setup_logger
from app.config.settings import Settings

# Initialize app
app = FastAPI(title="TTS Service")
logger = setup_logger()
settings = Settings()

# Include routes
app.include_router(tts_router, prefix="/api/v1/tts", tags=["TTS"])

@app.get("/")
def read_root():
    return {"message": "TTS Service is running."}
```