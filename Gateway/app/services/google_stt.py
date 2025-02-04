#### `app/services/google_stt.py`
```python
from google.cloud import speech_v1p1beta1 as speech
from app.schemas.transcription import TranscriptionResponse

class GoogleSpeechToText:
    def __init__(self):
        self.client = speech.SpeechClient()

    def transcribe(self, audio_content: bytes, language_code="en-US") -> TranscriptionResponse:
        audio = speech.RecognitionAudio(content=audio_content)
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code=language_code,
            enable_automatic_punctuation=True,
        )

        response = self.client.recognize(config=config, audio=audio)
        if not response.results:
            raise Exception("No transcription results.")

        result = response.results[0]
        return TranscriptionResponse(
            transcription=result.alternatives[0].transcript,
            confidence=result.alternatives[0].confidence,
        )
```