FROM python:latest

ENV OPENAI_API_KEY="sk-proj-9fQ2mZ8xN4kLpR7vT1wY3bH6dJ0aS5cE"

WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
