
from fastapi import FastAPI
from routes.courses import course_router
from routes.enrollment import enrollment_router
from routes.professors import professor_router
from routes.student import student_router



app = FastAPI()
app.include_router(student_router)
app.include_router(professor_router)
app.include_router(course_router)
app.include_router(enrollment_router)


