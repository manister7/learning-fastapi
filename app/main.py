from fastapi import Depends, FastAPI, HTTPException 
from sqlalchemy import select 
from sqlalchemy.orm import Session 
 
from .database import Base, engine, get_db 
from .models import Student 
from .schemas import StudentCreate, StudentResponse 
 
 
Base.metadata.create_all(bind=engine) 
 
app = FastAPI( 
    title="Learning FastAPI Student API", 
    version="1.0.0", 
    root_path= '/api'
) 
 
 
@app.get("/health") 
def health(): 
    return { 
        "status": "healthy" 
    } 
 
 
@app.post( 
    "/students", 
    response_model=StudentResponse 
) 
def create_student( 
    student: StudentCreate, 
    db: Session = Depends(get_db) 
): 
    existing = db.scalar( 
        select(Student).where(Student.email == student.email) 
    ) 
 
    if existing: 
        raise HTTPException( 
            status_code=409, 
            detail="Email already exists" 
        ) 
 
    new_student = Student( 
        name=student.name, 
        email=student.email, 
        course=student.course 
    ) 
 
    db.add(new_student) 
    db.commit() 
    db.refresh(new_student) 
 
    return new_student 
 
 
@app.get( 
    "/students", 
    response_model=list[StudentResponse] 
) 
def get_students( 
    db: Session = Depends(get_db) 
): 
    return db.scalars( 
        select(Student) 
    ).all() 
 
 
@app.get( 
    "/students/{student_id}", 
    response_model=StudentResponse 
) 
def get_student( 
    student_id: int, 
    db: Session = Depends(get_db) 
): 
    student = db.get(Student, student_id) 
 
    if not student: 
        raise HTTPException( 
            status_code=404, 
            detail="Student not found" 
        ) 
 
    return student 
 
 
@app.delete("/students/{student_id}") 
def delete_student( 
    student_id: int, 
    db: Session = Depends(get_db) 
): 
    student = db.get(Student, student_id) 
 
    if not student: 
        raise HTTPException( 
            status_code=404, 
            detail="Student not found" 
        ) 
 
    db.delete(student) 
    db.commit() 
 
    return { 
        "message": "Student deleted" 
    } 

 
