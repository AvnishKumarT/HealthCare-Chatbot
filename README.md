
# Healthcare Chatbot

This is a simple chatbot to provide healthcare suggestions based on user symptoms.

## Features
- Symptom matching with a predefined dataset
- Healthcare suggestions for common symptoms
- Easy deployment with Flask

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r deployment/requirements.txt`
3. Run the app: `python backend/app.py`
4. Access the chatbot at `http://127.0.0.1:5000`.

## Deployment
- To deploy on Heroku, use the provided `Procfile` and `requirements.txt`.
- To deploy with Docker:
  ```bash
  docker build -t healthcare-chatbot .
  docker run -p 5000:5000 healthcare-chatbot
  ```
