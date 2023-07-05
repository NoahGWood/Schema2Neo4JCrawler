from pydantic import BaseModel
from models.Thing import Thing

from typing import Optional, Any

class OpeningHoursSpecification(Thing):
    closes: Optional[Any] = None
    dayOfWeek: Optional[Any] = None
    opens: Optional[Any] = None
    validFrom: Optional[Any] = None
    validThrough: Optional[Any] = None

