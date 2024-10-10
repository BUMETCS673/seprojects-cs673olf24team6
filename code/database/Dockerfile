FROM python:3.11-slim

RUN apt-get update && apt-get install -y sqlite3

WORKDIR /database

COPY . /database

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN python /database/src/start_movies.py

# Default command for running in production
CMD /bin/sh -c "sqlite3 /database/src/movies.db && tail -f /dev/null"

