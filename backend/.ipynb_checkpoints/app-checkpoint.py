
from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Load dataset
dataset = pd.read_csv('backend/dataset.csv')

# Function to get suggestion based on input
def get_suggestion(user_input):
    for index, row in dataset.iterrows():
        if row['Symptom'].lower() in user_input.lower():
            return row['Suggestion']
    return "Sorry, I couldn't find a suggestion for your symptoms. Please consult a healthcare professional."

@app.route('/get_suggestion', methods=['POST'])
def get_suggestion_endpoint():
    data = request.get_json()
    user_input = data.get('input', '')
    suggestion = get_suggestion(user_input)
    return jsonify({'suggestion': suggestion})

if __name__ == '__main__':
    app.run(debug=True)
