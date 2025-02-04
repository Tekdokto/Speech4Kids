#### `app/config/settings.py`
```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "ASR Service"
    debug: bool = True

settings = Settings()
```