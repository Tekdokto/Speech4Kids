from fastapi import FastAPI
from app.routes.iot_connection import router as iot_router
from app.utils.logger import setup_logger

logger = setup_logger(__name__)
app = FastAPI(title="Connection Service")

app.include_router(iot_router, prefix="/connection", tags=["IoT Connection"])

@app.on_event("startup")
async def startup_event():
    logger.info("Connection Service is starting...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Connection Service is shutting down...")

@app.get("/")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "Connection Service is running"}
