#### `app/services/wav2vec2_model.py`
```python
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import torch
import librosa

class Wav2Vec2ASR:
    def __init__(self):
        self.processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
        self.model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

    def transcribe(self, audio_path: str):
        # Load audio
        speech, rate = librosa.load(audio_path, sr=16000)
        input_values = self.processor(speech, sampling_rate=rate, return_tensors="pt", padding=True).input_values

        # Perform inference
        logits = self.model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = self.processor.decode(predicted_ids[0])
        confidence = logits.max().item()
        return transcription, confidence
```