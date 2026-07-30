import base64
from pathlib import Path

import requests

from app.config import INWORLD_API_KEY, INWORLD_VOICE_ID


class TTSService:
    def __init__(self):
        if not INWORLD_API_KEY:
            raise ValueError("INWORLD_API_KEY is not configured.")

        self.api_key = INWORLD_API_KEY
        self.voice_id = INWORLD_VOICE_ID

    def generate_audio(self, text: str, output_file: Path) -> Path:
        """
        Generate Hindi speech using Inworld TTS.
        """

        output_file.parent.mkdir(parents=True, exist_ok=True)

        url = "https://api.inworld.ai/tts/v1/voice"

        headers = {
            "Authorization": f"Basic {self.api_key}",
            "Content-Type": "application/json",
        }

        payload = {
            "text": text,
            "voice_id": self.voice_id,
            "model_id": "inworld-tts-2",
        }

        response = requests.post(
            url,
            headers=headers,
            json=payload,
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()

        audio_b64 = data.get("audioContent")

        if not audio_b64:
            raise RuntimeError("No audioContent returned from Inworld.")

        audio_bytes = base64.b64decode(audio_b64)

        with open(output_file, "wb") as f:
            f.write(audio_bytes)

        return output_file

    def generate_segments(self, segments, output_dir: Path):
        """
        Generate one MP3 file for every translated segment.
        """

        output_dir.mkdir(parents=True, exist_ok=True)

        generated_files = []

        for index, segment in enumerate(segments):
            text = segment.get("hindi", "").strip()

            if not text:
                continue

            output_file = output_dir / f"chunk_{index}.mp3"

            self.generate_audio(text, output_file)

            generated_files.append(output_file)

        return generated_files