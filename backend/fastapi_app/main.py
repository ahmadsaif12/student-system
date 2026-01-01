from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from .database import SessionLocal
from .schemas import ApplicationCreate

app = FastAPI(title="Applications API")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/applications")
def create_application(data: ApplicationCreate, db: Session = Depends(get_db)):
    if data.program not in ["CS", "IT", "AI"]:
        raise HTTPException(status_code=400, detail="Invalid program")

    db.execute(
        text("""
        INSERT INTO applications_application
        (full_name, email, program, status, created_at)
        VALUES (:full_name, :email, :program, 'pending', CURRENT_TIMESTAMP)
        """),
        data.dict()
    )
    db.commit()
    return {"message": "Application created"}

# get all applications routes
@app.get("/applications")
def list_applications(program: str = None, status: str = None, db: Session = Depends(get_db)):
    query = "SELECT * FROM applications_application WHERE 1=1"
    params = {}
    if program:
        query += " AND program=:program"
        params["program"] = program
    if status:
        query += " AND status=:status"
        params["status"] = status
    result = db.execute(text(query), params).mappings().all()
    return result

# GET single application routes
@app.get("/applications/{id}")
def get_application(id: int, db: Session = Depends(get_db)):
    app_data = db.execute(
        text("SELECT * FROM applications_application WHERE id=:id"),
        {"id": id}
    ).mappings().first()
    if not app_data:
        raise HTTPException(status_code=404, detail="Application not found")
    return app_data

