from flask import Flask, render_template, request
import json
from question_manager import QuestionManager

app = Flask(__name__)
question_manager = QuestionManager()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        feedback, json_line = question_manager.get_feedback(user_input)
        try:
            result = json.loads(json_line.replace("'", '"'))
            acceptable = result.get('acceptable', False)
        except Exception:
            acceptable = False
        if not acceptable:
            return render_template('index.html', user_input=feedback + "\n" + question_manager.get_current_question(), acceptable=acceptable)
        else:
            next_q = question_manager.next_question()
            return render_template('index.html', user_input=next_q, acceptable=None)
    return render_template('index.html', user_input=question_manager.get_current_question(), acceptable=None)

if __name__ == '__main__':
    app.run(debug=True)