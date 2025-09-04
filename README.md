# Flask Application for Programming Trainer

This project is a simple Flask web application designed to facilitate learning programming through interactive exercises.

## Project Structure

- **app.py**: The entry point of the Flask application. It sets up the Flask app, defines routes, and handles form submissions.
- **templates/index.html**: Contains the HTML structure for the user interface, including a text label, an input field, and a submit button.
- **static/style.css**: Contains the CSS styles for the application, allowing for customization of the UI appearance.
- **requirements.txt**: Lists the dependencies required for the project, including Flask and any other necessary libraries.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Run the application:
   ```
   python app.py
   ```
7. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage

The application provides a user interface where users can input their answers to programming exercises. Upon submission, the application processes the input and provides feedback.

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Your feedback and suggestions are welcome!