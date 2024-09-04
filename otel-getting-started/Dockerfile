FROM --platform=linux/amd64 python:3.9-slim-buster as build
WORKDIR /app
COPY requirements.txt /app/
COPY custom-metric.py /app/
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "custom-metric.py"]
