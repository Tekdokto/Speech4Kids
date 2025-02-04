#### `app/utils/preprocessing.py`
```python
import librosa

def preprocess_audio(audio_path: str, target_sr: int = 16000):
    speech, _ = librosa.load(audio_path, sr=target_sr)
    return speech
```