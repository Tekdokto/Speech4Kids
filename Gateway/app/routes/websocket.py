#### `app/routes/websocket.py`

from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.google_stt import GoogleSpeechToText

websocket_router = APIRouter()

# Initialize Google Speech-to-Text service
stt_service = GoogleSpeechToText()

@websocket_router.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_bytes()
            transcription = stt_service.transcribe(audio_content=data)
            await websocket.send_json(transcription.dict())
    except WebSocketDisconnect:
        print("WebSocket connection closed.")