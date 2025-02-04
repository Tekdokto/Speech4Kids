#### `README.md`
```markdown
# TTS Service for Speech4Kids

This is the Text-to-Speech (TTS) service for the Speech4Kids project. It uses Tacotron and HiFi-GAN for high-quality speech synthesis.

## Features
- Accepts text input and generates audio.
- Supports multiple voices.

# Tacotron + HiFi-GAN TTS Service Implementation

## Directory Structure
```
tts_service/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── tts.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── tts_request.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── tacotron_hifigan.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── logger.py
│   └── config/
│       ├── __init__.py
│       └── settings.py
├── tests/
│   ├── __init__.py
│   └── test_tts.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Setup
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the service:
   ```bash
   uvicorn app.main:app --reload
   ```

## API Endpoints
### POST `/api/v1/tts/generate-audio`
**Request Body**:
```json
{
  "text": "Hello, world!",
  "voice": "default"
}
```

**Response**:
```json
{
  "audio_base64": "..."
}
```

## Testing
Run the tests using pytest:
```bash
pytest
```

## Docker
Build and run the service with Docker:
```bash
docker build -t tts-service .
docker run -p 8000:8000 tts-service
```
```
