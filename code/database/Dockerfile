#FROM alpine:latest

#RUN apk update && apk add sqlite && apk add python3 py3-pip
FROM python:3.9-slim

# Installing SQLite3 and other necessary system libraries
RUN apt-get update && apt-get install -y \
    sqlite3 \
    libsqlite3-dev \
    build-essential \
    gcc \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install pandas

WORKDIR /database/movies
COPY IMDB_Top_250_Movies.csv /database/movies/IMDB_Top_250_Movies.csv
COPY start_movies.py /database/movies/start_movies.py
COPY create_movies_db.py /database/movies/create_movies_db.py
COPY create_movies_db_tables.py /database/movies/create_movies_db_tables.py
COPY load_movies_db_data.py /database/movies/load_movies_db_data.py
COPY db_test_data.py /database/movies/db_test_data.py
COPY test_querry.sql /database/movies/test_querry.sql


RUN chmod +x /database/movies/start_movies.py

CMD ["sh", "-c", "python3 /database/movies/start_movies.py && sqlite3 movies.db"]