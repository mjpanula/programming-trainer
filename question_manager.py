from llm_service import LLMService

class QuestionManager:
    def __init__(self):
        self.llm = LLMService()
        self.initial_question = (
            "Question:\nVariables fname and sname contain a first name and a last name. "
            "Write a python code that prints the whole name separated by a space"
        )
        self.current_question = self.initial_question

    def get_current_question(self):
        return self.current_question

    def get_feedback(self, user_input):
        prompt = (
            f"User was asked the following question:\n{self.current_question}\n"
            f"The user's answer was:\n{user_input}\n"
            "Provide feedback from the answer. Also, respond with a JSON object on a new line: "
            "{'acceptable': true/false} indicating if the answer is correct."
        )
        response_text = self.llm.ask(prompt)
        lines = response_text.strip().split('\n')
        feedback = '\n'.join([line for line in lines if not line.strip().startswith('{')])
        json_line = next((line for line in lines if line.strip().startswith('{')), '{}')
        return feedback, json_line

    def next_question(self):
        prompt = (
            f"This is an example af a python quiz question:\n{self.current_question}\nCreate another similar question."
        )
        self.current_question = self.llm.ask(prompt)
        return self.current_question