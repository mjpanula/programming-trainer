from flask import Flask, render_template, request

import gemini_test as g

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        # Process the input as needed
        return render_template('index.html', user_input=user_input)
    return render_template('index.html', user_input=g.response.text)

if __name__ == '__main__':
    app.run(debug=True)