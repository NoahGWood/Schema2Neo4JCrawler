from pydantic import BaseModel
from typing import Optional, Any

class GenderType(BaseModel):
    gender: Optional[Any] = None
    suggestedGender: Optional[Any] = None

