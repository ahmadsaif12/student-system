# Use official Python slim image
FROM python:3.12-slim

WORKDIR /app

# Prevent .pyc files and unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y gcc libpq-dev && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project
COPY core/ ./core/

# Copy FastAPI app
COPY fastapi_app/ ./fastapi_app/

# Expose ports for Django and FastAPI
EXPOSE 8000 8001

# Default command (can be overridden in docker-compose)
CMD ["python", "core/manage.py", "runserver", "0.0.0.0:8000"]
