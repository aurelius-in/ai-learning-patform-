from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    level: Optional[str] = "Intermediate"

class CourseCreate(CourseBase):
    tags: Optional[List[str]] = []

class CourseUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]
    level: Optional[str]
    tags: Optional[List[str]]

class CourseInDB(CourseBase):
    id: int
    tags: List[str]
    created_at: datetime
    updated_at: Optional[datetime] = None

class CourseOut(CourseBase):
    id: int
    tags: List[str]