from pydantic import BaseModel
from models.Event import Event

from typing import Optional, Any

class CourseInstance(Event):
    courseMode: Optional[Any] = None
    courseSchedule: Optional[Any] = None
    courseWorkload: Optional[Any] = None
    instructor: Optional[Any] = None

