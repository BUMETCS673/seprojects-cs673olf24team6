FROM python:3.11-slim

WORKDIR /app

COPY . /app

# Copy requirements file first to leverage Docker cache if requirements haven't changed
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH environment variable
ENV PYTHONPATH=/app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "src/backend.py"]
