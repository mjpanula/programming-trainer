from google import genai
from google.genai import types

class LLMService:
    def __init__(self):
        self.client = genai.Client()
        self.system_instruction = (
            "You are a drill instructor for learning typing and basic Python coding. "
            "Be very dry and use as few word as possible."
        )

    def ask(self, contents):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(system_instruction=self.system_instruction),
            contents=contents
        )
        return response.candidates[0].content.parts[0].text