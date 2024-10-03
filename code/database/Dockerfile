FROM alpine:latest

RUN apk update && apk add sqlite && apk add python3 py3-pip

WORKDIR /database/movies

#RUN (Script stuff to create db file)

COPY start_movies.py /database/movies/start_movies.py
COPY create_movies_db.py /database/movies/create_movies_db.py
COPY create_movies_db_tables.py /database/movies/create_movies_db_tables.py
COPY load_movies_db_data.py /database/movies/load_movies_db_data.py
COPY db_test_data.py /database/movies/db_test_data.py

CMD ["sh", "-c", "sqlite3 && python3 /database/movies/start_movies.py"]