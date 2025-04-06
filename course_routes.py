from fastapi import APIRouter, HTTPException, status
from typing import List
from api.models.course import CourseCreate, CourseOut, CourseUpdate

router = APIRouter(
    prefix="/courses",
    tags=["courses"]
)

fake_courses_db = []

@router.post("/", response_model=CourseOut)
async def create_course(course: CourseCreate):
    new_course = {
        "id": len(fake_courses_db) + 1,
        "title": course.title,
        "description": course.description,
        "level": course.level,
        "tags": course.tags or [],
        "created_at": "2025-01-01T00:00:00",
        "updated_at": None
    }
    fake_courses_db.append(new_course)
    return new_course

@router.get("/", response_model=List[CourseOut])
async def list_courses():
    return fake_courses_db

@router.put("/{course_id}", response_model=CourseOut)
async def update_course(course_id: int, course: CourseUpdate):
    for c in fake_courses_db:
        if c["id"] == course_id:
            if course.title:
                c["title"] = course.title
            if course.description:
                c["description"] = course.description
            if course.level:
                c["level"] = course.level
            if course.tags is not None:
                c["tags"] = course.tags
            return c
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Course not found")