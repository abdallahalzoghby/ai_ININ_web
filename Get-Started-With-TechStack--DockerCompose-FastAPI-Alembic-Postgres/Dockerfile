<<<<<<< HEAD
FROM python:3.11-slim AS base

WORKDIR /app

# Install dependencies and cache the apt packages
RUN apt-get update && apt-get install -y libpq-dev gcc && apt-get clean && rm -rf /var/lib/apt/lists/*

# Separate dependencies into layers for caching
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY app /app

EXPOSE 8000

CMD ["python", "app/run.py"]
=======
# Base image of python 3.11
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the contents of the 'app' directory from your local machine to the '/app' directory inside the container
COPY . /app  

# Install the dependencies listed in the requirements.txt file located inside the 'app' directory
RUN pip install --no-cache-dir --default-timeout=100 -r requirements.txt

RUN pip install --no-cache-dir scikit-learn joblib

# Expose the port that FastAPI server will run on
EXPOSE 80

# CMD pipeline running the server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]
>>>>>>> 965fb520131e29bb81daf4ecdef43a9464111929
