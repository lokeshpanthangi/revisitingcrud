from fastapi import APIRouter
from pydantic_schemas import Students as StudentsSchema, Courses as CourseSchema,Professors as ProfessorSchema
from supabase_client import supabase

enrollment_router = APIRouter()

