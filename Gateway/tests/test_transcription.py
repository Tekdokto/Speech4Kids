#### `tests/test_transcription.py`
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_transcription_success():
    audio_data = "<base64-encoded-audio-data>"
    response = client.post("/transcription/", json={"audio_data": audio_data})
    assert response.status_code == 200
    assert "transcription" in response.json()
    assert "confidence" in response.json()

def test_transcription_failure():
    response = client.post("/transcription/", json={})
    assert response.status_code == 422
```