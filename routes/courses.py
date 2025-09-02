from fastapi import APIRouter
from pydantic_schemas import Students as StudentsSchema, Courses as CourseSchema,Professors as ProfessorSchema
from supabase import create_client, Client
course_router = APIRouter()

# Supabase config
SUPABASE_URL = "https://gdxywhapqlaifkqfuxdj.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdkeHl3aGFwcWxhaWZrcWZ1eGRqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1Njc5MTI1OCwiZXhwIjoyMDcyMzY3MjU4fQ.X9E_bkm362lD5Nq7u9oY7JmO71psO9WUgc7MfAd1Dnw"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)



@course_router.get("/student/{student_id}/courses")
def get_student_courses(student_id: int):
    # This assumes you have an enrollments table with student_id and course_id, and a courses table
    enrollments_resp = supabase.table("enrollments").select("course_id").eq("student_id", student_id).execute()
    course_ids = [e["course_id"] for e in enrollments_resp.data]
    if not course_ids:
        return []
    courses_resp = supabase.table("courses").select("*").in_("id", course_ids).execute()
    return courses_resp.data


@course_router.get("/get_all_courses")
def get_courses():
    response = supabase.table("courses").select("*").execute()
    return response.data

@course_router.post("/create_new_course")
def new_course(course : CourseSchema):
    data = course.dict()
    response = supabase.table("courses").insert(data).execute()
    return response.data
