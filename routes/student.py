from fastapi import APIRouter
from pydantic_schemas import Students as StudentsSchema, Courses as CourseSchema,Professors as ProfessorSchema
from supabase import create_client, Client
student_router = APIRouter()

# Supabase config
SUPABASE_URL = "https://gdxywhapqlaifkqfuxdj.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImdkeHl3aGFwcWxhaWZrcWZ1eGRqIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc1Njc5MTI1OCwiZXhwIjoyMDcyMzY3MjU4fQ.X9E_bkm362lD5Nq7u9oY7JmO71psO9WUgc7MfAd1Dnw"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)



@student_router.get("/get_all_students")
def get_all_students():
    response = supabase.table("students").select("*").execute()
    return response.data

@student_router.post("/new_student")
def create_student(new_student: StudentsSchema):
    data = new_student.dict()
    response = supabase.table("students").insert(data).execute()
    return response.data

@student_router.get("/get_student/{student_id}")
def read_student(student_id: int):
    response = supabase.table("students").select("*").eq("id", student_id).single().execute()
    return response.data

@student_router.put("/update_student/{student_id}")
def update_student(student_id: int, new_data: StudentsSchema):
    data = {k: v for k, v in new_data.dict().items() if v is not None}
    response = supabase.table("students").update(data).eq("id", student_id).execute()
    return response.data

@student_router.delete("/delete_student/{student_id}")
def delete_student(student_id: int):
    response = supabase.table("students").delete().eq("id", student_id).execute()
    return {"message": "Student deleted successfully"}
