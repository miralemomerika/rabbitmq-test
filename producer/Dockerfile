FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
COPY setup.py .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./producer/producer.py .

CMD ["python", "producer.py"]