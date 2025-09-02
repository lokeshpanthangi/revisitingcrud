from fastapi import APIRouter
from pydantic_schemas import Students as StudentsSchema, Courses as CourseSchema,Professors as ProfessorSchema
from supabase_client import supabase
course_router = APIRouter()




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
def create_course(course : CourseSchema):
    data = course.dict()
    response = supabase.table("courses").insert(data).execute()
    return response.data

@course_router.get("/get_course/{course_id}")
def read_course(course_id : int):
    response = supabase.table("courses").select("*").eq("id", course_id).single().execute()
    return response.data

@course_router.put("/update_course/{course_id}")
def update_course(course_id: int, course: CourseSchema):
    data = course.dict()
    response = supabase.table("courses").update(data).eq("id", course_id).execute()
    return response.data

@course_router.delete("/delete_course/{course_id}")
def delete_course(course_id: int):
    response = supabase.table("courses").delete().eq("id", course_id).execute()
    return {"message": "Course deleted successfully"}