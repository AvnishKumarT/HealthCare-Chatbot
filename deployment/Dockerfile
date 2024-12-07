
FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install -r deployment/requirements.txt
CMD ["python", "backend/app.py"]
