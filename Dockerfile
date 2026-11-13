FROM python:3.10.4-slim-bullseye

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .


