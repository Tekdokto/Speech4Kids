#### `app/config/settings.py`
```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "TTS Service"
    debug: bool = False

    class Config:
        env_file = ".env"
```