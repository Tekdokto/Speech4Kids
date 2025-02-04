## File: app/config/settings.py
```python
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    openai_api_key: str = os.getenv("OPENAI_API_KEY")

    class Config:
        env_file = ".env"

settings = Settings()
```