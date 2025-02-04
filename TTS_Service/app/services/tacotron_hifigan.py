#### `app/services/tacotron_hifigan.py`
```python
import base64
import numpy as np
import torch
from tacotron2.tacotron2 import Tacotron2  # NVIDIA Tacotron2 implementation
from hifigan.hifigan import HiFiGAN  # NVIDIA HiFi-GAN implementation

class TacotronHiFiGAN:
    def __init__(self, tacotron_model_path: str, hifigan_model_path: str):
        """
        Initialize Tacotron2 and HiFi-GAN models.
        :param tacotron_model_path: Path to the pre-trained Tacotron2 model.
        :param hifigan_model_path: Path to the pre-trained HiFi-GAN model.
        """
        # Load Tacotron2 model
        self.tacotron = Tacotron2()
        self.tacotron.load_state_dict(torch.load(tacotron_model_path, map_location="cpu"))
        self.tacotron.eval()

        # Load HiFi-GAN model
        self.hifigan = HiFiGAN()
        self.hifigan.load_state_dict(torch.load(hifigan_model_path, map_location="cpu"))
        self.hifigan.eval()

    def synthesize_speech(self, text: str, voice: str = "default") -> str:
        """
        Synthesize speech from text using Tacotron2 and HiFi-GAN.
        :param text: Input text to synthesize.
        :param voice: Voice configuration (currently default placeholder).
        :return: Base64-encoded audio string.
        """
        if not text:
            raise ValueError("Input text cannot be empty.")

        # Step 1: Convert text to mel spectrogram using Tacotron2
        try:
            with torch.no_grad():
                mel_spectrogram = self.tacotron.infer(text)
        except Exception as e:
            raise RuntimeError(f"Error during Tacotron2 inference: {e}")

        # Step 2: Convert mel spectrogram to audio waveform using HiFi-GAN
        try:
            with torch.no_grad():
                audio_waveform = self.hifigan.infer(mel_spectrogram)
        except Exception as e:
            raise RuntimeError(f"Error during HiFi-GAN inference: {e}")

        # Step 3: Encode waveform to base64
        try:
            audio_waveform = audio_waveform.squeeze().cpu().numpy()
            audio_bytes = (audio_waveform * 32767).astype(np.int16).tobytes()
            audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
        except Exception as e:
            raise RuntimeError(f"Error encoding audio to base64: {e}")

        return audio_base64
```