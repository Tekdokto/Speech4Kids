#### `app/schemas/transcription.py`
```python
from pydantic import BaseModel

class TranscriptionRequest(BaseModel):
    audio_data: str  # Base64-encoded audio data

class TranscriptionResponse(BaseModel):
    transcription: str
    confidence: float
```