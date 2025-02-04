
## File: app/main.py
```python
from fastapi import FastAPI
from app.routes import nlp_router
from app.utils.logger import setup_logger

# Initialize FastAPI app
app = FastAPI(title="NLP Service", version="1.0")

# Setup logger
logger = setup_logger()

# Include routes
app.include_router(nlp_router, prefix="/nlp", tags=["NLP"])

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "NLP Service is running."}
```
