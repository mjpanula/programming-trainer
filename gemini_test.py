from google import genai
from google.genai import types

client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="You are a drill instructor for learning typing and basic Python coding. Be very dry and use as few word as possible."),
    contents="Request me to type a python code that can be used to combine two string into a new string"
)

