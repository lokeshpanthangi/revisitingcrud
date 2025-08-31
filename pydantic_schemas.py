from pydantic import BaseModel
from typing import Optional



class Students(BaseModel):
    name: str
    email: str
    major : str
    year : int
    gpa : float
    
class Courses(BaseModel):
    name: str
    code: str
    credits: int
    professor_id : int
    max_capacity : int

class Professors(BaseModel):
    name: str
    email: str
    department: str
    hire_date : str

class Enrollments(BaseModel):
    student_id: int
    course_id: int
    enrollment_date: str
    grade : str


class UpdateStudents(BaseModel):
    name: Optional[str]
    email: Optional[str]
    major : Optional[str]
    year : Optional[int]
    gpa : Optional[float]

