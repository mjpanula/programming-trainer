from google import genai
from google.genai import types

client = genai.Client()

system_instruction="You are a drill instructor for learning typing \
    and basic Python coding. Be very dry and use as few word as possible."

initial_question="Question:\nVariables fname and sname contain \
    a first name and a last name. Write a python code that prints\
        the whole name separated by a space"

second_question="Question:\nVariable age contains a number. Write a python code that prints 'You are X years old', where X is the value of age."

def ask_llm(contents):
    response=client.models.generate_content(
            model="gemini-2.5-flash",
            config=types.GenerateContentConfig(
                system_instruction=system_instruction),
            contents=contents
        )
    print(response)
    return response.candidates[0].content.parts[0].text

def new_question(current_question):
    return ask_llm(f"This is an example af a python quiz question:\n\
            {current_question}\n\
            Create another similar question.")