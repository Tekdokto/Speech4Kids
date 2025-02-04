#### `tests/test_tts.py`
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_audio():
    response = client.post("/api/v1/tts/generate-audio", json={"text": "Hello, world!", "voice": "default"})
    assert response.status_code == 200
    assert "audio_base64" in response.json()
```