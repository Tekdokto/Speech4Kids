## settings.py
This module provides centralized configuration management.

# common/settings.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    """
    Shared settings configuration for all microservices.
    """
    PROJECT_NAME: str = "Speech4Kids"
    ENVIRONMENT: str = "development"  # development, staging, production
    LOG_LEVEL: str = "INFO"
    DATABASE_URL: str = "sqlite:///./test.db"
    REDIS_URL: str = "redis://localhost:6379"

    # Google API keys
    GOOGLE_API_KEY: str = "your-google-api-key"

    # JWT Authentication Settings
    JWT_SECRET_KEY: str = "your-secret-key"
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"  # Load environment variables from .env file

# Instantiate shared settings
settings = Settings()