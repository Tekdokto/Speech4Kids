
#### `README.md`
```markdown
# Gateway Service for Speech4Kids

## Overview
The Gateway service acts as the entry point for handling HTTP and WebSocket requests. It routes incoming transcription requests to the appropriate services and provides WebSocket support for real-time transcription.

### Features
- Handles HTTP API requests for speech-to-text transcription.
- Supports WebSocket for real-time streaming transcription.
- Integrates with Google Speech-to-Text API for transcription services.
- Centralized configuration and robust error handling.

---

## Description
This service serves as the main entry point for handling transcription requests and real-time speech-to-text processing. It integrates with the Google Speech-to-Text API and provides REST and WebSocket endpoints.

## Setup
### Prerequisites
- Python 3.9+
- Google Cloud credentials configured

### Installation
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd gateway
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the service:
    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

## Endpoints
- **POST** `/transcription`: Handles audio transcription requests.
- **WebSocket** `/ws`: Supports real-time transcription.

## Docker
Build and run the Docker container:
```bash
docker build -t speech4kids-gateway .
docker run -p 8000:8000 speech4kids-gateway

1. **Error Handlers (`error_handlers.py`)**:
   - Handles global exceptions and specific errors like `ValueError`.
   - Logs errors for monitoring and debugging.

2. **Security (`security.py`)**:
   - Implements a JWT authentication middleware.
   - Verifies Bearer tokens and handles token-related errors.

3. **Tests**:
   - `test_transcription.py`: Unit tests for the transcription API.
   - `test_websocket.py`: Tests the WebSocket endpoint for real-time transcription.
```
```

### Directory Structure
```plaintext
├── app/
│   ├── __init__.py
│   ├── main.py               # Gateway entry point
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── transcription.py  # Transcription API routes
│   │   └── websocket.py      # WebSocket routes
│   ├── services/
│   │   ├── __init__.py
│   │   └── google_stt.py     # Google Speech-to-Text abstraction
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── transcription.py  # Request/Response models
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── logger.py         # Logging utilities
│   │   ├── error_handlers.py # Global error handling
│   │   └── security.py       # Security middleware (JWT/Auth)
│   └── config/
│       ├── __init__.py
│       └── settings.py       # Centralized configuration
├── tests/                    # Gateway unit/integration tests
├── Dockerfile                # Containerization setup
├── requirements.txt          # Python dependencies
└── README.md                 # Gateway-specific documentation