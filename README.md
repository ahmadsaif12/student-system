# Student System

## Overview
Student Management System built with **Django** and **FastAPI**.  
Supports **SQLite database** and optional **Docker setup**.

---also setup postgressql in docker-compose.yaml file
POSTGRES_USER: postgres
POSTGRES_PASSWORD: postgres
POSTGRES_DB: fastapi_db

## Setup & Run

### 1. Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate
python manage.py runserver
# Access at: http://127.0.0.1:8000/

#for fastapi
uvicorn fastapi_app.main:app --reload
# Access at: http://127.0.0.1:8000/
