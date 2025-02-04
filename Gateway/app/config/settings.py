#### `app/config/settings.py`
```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    google_project_id: str = "your-google-project-id"
    environment: str = "development"

    class Config:
        env_file = ".env"

settings = Settings()
```
