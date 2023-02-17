FROM python:3.6-slim

WORKDIR /app

RUN pip install flask 

COPY app.py /app

ENTRYPOINT FLASK_APP=/app/app.py flask run --host=0.0.0.0 --port=8080
