from fastapi import APIRouter, Depends
from database import get_db, engine
from sqlalchemy.orm import Session
from models import Students, Courses, Professors, Enrollments
from pydantic_schemas import Students as StudentsSchema, Courses as CoursesSchema, Professors as ProfessorsSchema, Enrollments as EnrollmentsSchema
router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.get("/students")
def get_students():
    with Session(engine) as session:
        students = session.query(Students).all()
        return students
    
@router.post("/add_student")
def add_student(student: StudentsSchema, db: Session = Depends(get_db)):
    new_student = Students(
        name=student.name,
        email=student.email,
        major=student.major,
        year=student.year,
        gpa=student.gpa
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student


@router.get("/student/{student_id}")
def get_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Students).filter(Students.id == student_id).first()
    if not student:
        return {"error": "Student not found"}
    return student