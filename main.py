from fastapi import FastAPI
from models import Students, Professors, Courses, Enrollments
from routes import router
from database import Base, engine, SessionLocal
from sqlalchemy.orm import Session


Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(router)


