#### `app/routes/transcribe.py`
```python
from fastapi import APIRouter, HTTPException
from app.schemas.transcribe import TranscriptionRequest, TranscriptionResponse
from app.services.wav2vec2_model import Wav2Vec2ASR

transcribe_router = APIRouter()

# Initialize ASR model
asr_model = Wav2Vec2ASR()

@transcribe_router.post("/", response_model=TranscriptionResponse)
async def transcribe_audio(request: TranscriptionRequest):
    try:
        audio_text, confidence = asr_model.transcribe(request.audio_file_path)
        return TranscriptionResponse(transcription=audio_text, confidence=confidence)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```