from fastapi import APIRouter
from pydantic_schemas import Students as StudentsSchema, Courses as CourseSchema,Professors as ProfessorSchema
from supabase_client import supabase

student_router = APIRouter()




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
