from flask import Flask, render_template, request
import json

import gemini_test as g

app = Flask(__name__)

current_question = g.initial_question

@app.route('/', methods=['GET', 'POST'])
def index():
    global current_question  # Add this line
    if request.method == 'POST':
        user_input = request.form['user_input']

        response_text = g.ask_llm(f"User was asked the following question:\n\
                  {current_question}\n\
                  The user's answer was:\n\
                    {user_input}\n\
                        Provide feedback from the answer. \
                        Also, respond with a JSON object on a new line: \
                        {{'acceptable': true/false}} indicating if the answer is correct.")

        # Split response to get feedback and JSON
        lines = response_text.strip().split('\n')
        feedback = '\n'.join([line for line in lines if not line.strip().startswith('{')])
        json_line = next((line for line in lines if line.strip().startswith('{')), '{}')
        try:
            result = json.loads(json_line.replace("'", '"'))
            acceptable = result.get('acceptable', False)
        except Exception:
            acceptable = False

        if not acceptable:
            return render_template('index.html', user_input=feedback + "\n" + current_question, acceptable=acceptable)
        else:
            current_question = g.new_question(current_question)
        
            return render_template('index.html', user_input=current_question, acceptable=None)       
   
    return render_template('index.html', user_input=current_question, acceptable=None)

if __name__ == '__main__':
    app.run(debug=True)