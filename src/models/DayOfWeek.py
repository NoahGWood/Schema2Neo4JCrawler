from pydantic import BaseModel
from typing import Optional, Any

class DayOfWeek(BaseModel):
    byDay: Optional[Any] = None
    dayOfWeek: Optional[Any] = None

