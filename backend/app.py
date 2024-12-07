
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
try:
    dataset = pd.read_csv('backend/dataset.csv')
except pd.errors.ParserError as e:
    print("Error reading the dataset:", e)
    exit(1)
from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# Function to get suggestion based on input
def get_suggestion(user_input):
    for index, row in dataset.iterrows():
        if row['Symptom'].lower() in user_input.lower():
            return row['Suggestion']
    return "Sorry, I couldn't find a suggestion for your symptoms. Please consult a healthcare professional."

# Route for the homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle symptom suggestion
@app.route('/get_suggestion', methods=['POST'])
def get_suggestion_endpoint():
    data = request.get_json()
    user_input = data.get('input', '')
    suggestion = get_suggestion(user_input)
    return jsonify({'suggestion': suggestion})

if __name__ == '__main__':
    app.run(debug=True)
