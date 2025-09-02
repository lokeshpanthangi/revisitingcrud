from fastapi import APIRouter
from pydantic_schemas import Students as StudentsSchema, Courses as CourseSchema,Professors as ProfessorSchema
from supabase import create_client, Client
professor_router = APIRouter()

# Supabase config
SUPABASE_URL = "https://gdxywhapqlaifkqfuxdj.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdkeHl3aGFwcWxhaWZrcWZ1eGRqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1Njc5MTI1OCwiZXhwIjoyMDcyMzY3MjU4fQ.X9E_bkm362lD5Nq7u9oY7JmO71psO9WUgc7MfAd1Dnw"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)


@professor_router.post("/create_new_professor")
def new_professor(professor: ProfessorSchema):
    data = professor.dict()
    response = supabase.table("professors").insert(data).execute()
    return response.data

@professor_router.get("/get_all_professors")
def get_all_professors():
    response = supabase.table("professors").select("*").execute()
    return response.data