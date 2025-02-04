#### `app/routes/tts.py`
```python
from fastapi import APIRouter, HTTPException
from app.schemas.tts_request import TTSRequest
from app.services.tacotron_hifigan import TacotronHiFiGAN

# Initialize router
tts_router = APIRouter()

# Initialize TTS Service
tts_service = TacotronHiFiGAN()

@tts_router.post("/generate-audio")
async def generate_audio(request: TTSRequest):
    try:
        audio = tts_service.synthesize_speech(request.text, request.voice)
        return {"audio_base64": audio}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```