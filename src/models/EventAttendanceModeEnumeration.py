from pydantic import BaseModel
from typing import Optional, Any

class EventAttendanceModeEnumeration(BaseModel):
    eventAttendanceMode: Optional[Any] = None

