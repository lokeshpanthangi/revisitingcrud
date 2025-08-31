from sqlalchemy import Column, Integer, String, Float
from database import Base



class Students(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    major = Column(String)
    year = Column(Integer)
    gpa = Column(Float)

class Courses(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    code = Column(String)
    credits = Column(Integer)
    professor_id = Column(Integer)
    max_capacity = Column(Integer)

class Professors(Base):
    __tablename__ = "professors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    department = Column(String)
    hire_date = Column(String)

class Enrollments(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer)
    course_id = Column(Integer)
    enrollment_date = Column(String)
    grade = Column(String)