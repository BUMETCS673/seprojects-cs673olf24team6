FROM python:3.11-slim

# Allows use to access database from shell
RUN apt-get update && apt-get install -y sqlite3

WORKDIR /app

COPY . /app

# Copy requirements file first to leverage Docker cache if requirements haven't changed
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH environment variable
#ENV PYTHONPATH=/app

RUN python /app/src/start_movies.py

CMD [ "tail", "-f", "/dev/null"]
