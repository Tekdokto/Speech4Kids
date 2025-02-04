#### `app/schemas/transcribe.py`
```python
from pydantic import BaseModel

class TranscriptionRequest(BaseModel):
    audio_file_path: str  # Path to the audio file for transcription

class TranscriptionResponse(BaseModel):
    transcription: str
    confidence: float
```