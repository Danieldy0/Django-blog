FROM python:3.10.4-slim-bullseye

WORKDIR /code

# Install postgresql-client for python manage.py dbshell support
RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

# Copy project
COPY . .


