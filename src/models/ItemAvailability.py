from pydantic import BaseModel
from typing import Optional, Any

class ItemAvailability(BaseModel):
    availability: Optional[Any] = None

