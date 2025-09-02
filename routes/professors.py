
from fastapi import APIRouter
from pydantic_schemas import Students as StudentsSchema, Courses as CourseSchema,Professors as ProfessorSchema
from supabase_client import supabase
professor_router = APIRouter()


@professor_router.get("/get_all_professors")
def get_all_professors():
    response = supabase.table("professors").select("*").execute()
    return response.data

@professor_router.post("/create_new_professor")
def create_professor(professor: ProfessorSchema):
    data = professor.dict()
    response = supabase.table("professors").insert(data).execute()
    return response.data

@professor_router.get("/get_professor/{professor_id}")
def read_professor(professor_id: int):
    response = supabase.table("professors").select("*").eq("id", professor_id).execute()
    return response.data

@professor_router.put("/update_professor/{professor_id}")
def update_professor(professor_id: int, professor: ProfessorSchema):
    data = professor.dict()
    response = supabase.table("professors").update(data).eq("id", professor_id).execute()
    return response.data

@professor_router.delete("/delete_professor/{professor_id}")
def delete_professor(professor_id: int):
    response = supabase.table("professors").delete().eq("id", professor_id).execute()
    return response.data