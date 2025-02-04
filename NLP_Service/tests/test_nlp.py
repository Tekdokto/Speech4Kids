## File: tests/test_nlp.py
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "NLP Service is running."}

def test_generate_response():
    response = client.post(
        "/nlp/generate",
        json={"prompt": "What is AI?"},
    )
    assert response.status_code == 200
    assert "response" in response.json()
```
