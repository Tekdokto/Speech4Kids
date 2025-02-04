#### `app/schemas/tts_request.py`
```python
from pydantic import BaseModel

class TTSRequest(BaseModel):
    text: str
    voice: str
```