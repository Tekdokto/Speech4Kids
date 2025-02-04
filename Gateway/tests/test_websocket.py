#### `tests/test_websocket.py`
```python
import asyncio
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

async def test_websocket_transcription():
    with client.websocket_connect("/ws/") as websocket:
        audio_data = b"<binary-audio-data>"
        websocket.send_bytes(audio_data)
        response = websocket.receive_json()
        assert "transcription" in response
        assert "confidence" in response

asyncio.run(test_websocket_transcription())
```