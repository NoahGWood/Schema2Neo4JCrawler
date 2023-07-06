from pydantic import BaseModel
from typing import Optional, Any

class EventStatusType(BaseModel):
    eventStatus: Optional[Any] = None
    status: Optional[Any] = None

