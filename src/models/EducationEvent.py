from pydantic import BaseModel
from models.Event import Event

from typing import Optional, Any

class EducationEvent(Event):
    assesses: Optional[Any] = None
    educationalLevel: Optional[Any] = None
    teaches: Optional[Any] = None

