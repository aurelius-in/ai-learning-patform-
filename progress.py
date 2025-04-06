from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ProgressBase(BaseModel):
    user_id: int
    course_id: int
    completed_lessons: int
    total_lessons: int

class ProgressCreate(ProgressBase):
    pass

class ProgressUpdate(BaseModel):
    completed_lessons: Optional[int] = None

class ProgressInDB(ProgressBase):
    id: int
    last_accessed: datetime

class ProgressOut(ProgressBase):
    id: int
    completion_rate: float