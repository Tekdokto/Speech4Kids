#### `app/routes/transcription.py`

from fastapi import APIRouter, HTTPException
from app.services.google_stt import GoogleSpeechToText
from app.schemas.transcription import TranscriptionRequest, TranscriptionResponse

transcription_router = APIRouter()

# Initialize Google Speech-to-Text service
stt_service = GoogleSpeechToText()

@transcription_router.post("/", response_model=TranscriptionResponse)
def transcribe_audio(request: TranscriptionRequest):
    try:
        audio_data = request.audio_data.encode("utf-8")
        response = stt_service.transcribe(audio_content=audio_data)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
