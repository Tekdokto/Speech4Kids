#### `tests/test_transcribe.py`
```python
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_transcribe_audio():
    response = client.post(
        "/transcribe/",
        json={"audio_file_path": "sample.wav"}
    )
    assert response.status_code == 200
    assert "transcription" in response.json()
    assert "confidence" in response.json()
```