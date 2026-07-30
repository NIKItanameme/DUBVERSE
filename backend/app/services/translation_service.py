import google.generativeai as genai
from app.config import GEMINI_API_KEY


class TranslationService:
    def __init__(self):
        if not GEMINI_API_KEY:
            raise ValueError("GEMINI_API_KEY is not configured.")

        genai.configure(api_key=GEMINI_API_KEY)

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def translate_segments(self, segments):
        """
        Translate all transcript segments in ONE Gemini request.
        """

        if not segments:
            return []

        # Combine all English sentences
        english_text = "\n".join(
            [f"{i+1}. {seg['english']}" for i, seg in enumerate(segments)]
        )

        prompt = f"""
You are an expert translator.

Translate the following English transcript into natural conversational Hindi.

Rules:
- Return ONLY the Hindi translations.
- Keep exactly the same numbering.
- Return exactly {len(segments)} lines.
- Do not add explanations.
- Do not skip any line.

Transcript:

{english_text}
"""

        response = self.model.generate_content(prompt)

        output = response.text.strip()

        # Split into lines
        lines = [
            line.strip()
            for line in output.split("\n")
            if line.strip()
        ]

        translated = []

        for i, seg in enumerate(segments):

            if i < len(lines):

                hindi = lines[i]

                # Remove numbering like "1."
                if "." in hindi:
                    hindi = hindi.split(".", 1)[1].strip()

            else:
                # Fallback if Gemini returns fewer lines
                hindi = seg["english"]

            translated.append({
                "start": seg["start"],
                "end": seg["end"],
                "english": seg["english"],
                "hindi": hindi
            })

        return translated