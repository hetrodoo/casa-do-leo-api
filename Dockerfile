FROM python:3.8-slim

WORKDIR /app

ARG PORT

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

ENV PORT=$PORT

EXPOSE $PORT

ENV GOOGLE_APPLICATION_CREDENTIALS /app/datastore_sa.json

CMD ["python", "main.py"]
